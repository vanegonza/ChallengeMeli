#!/usr/bin/env python
import psutil
import socket
import json
import requests


# Get Hostname and Ip Address
def get_hostname():
    host_name = socket.gethostname()
    return host_name


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


#Disk space 
def calculate_disk():
    disk = psutil.disk_usage('/')._asdict()
    total_space = disk['total']
    used_space = disk['used']
    free_space = disk['free']
    por_used = used_space * 100 / total_space
    return 100 - por_used


# gives a single float value
def calculate_cpu():
    promedio = None
    acum = 0
    value = 3
    for x in range(value):
        acum += psutil.cpu_percent(interval=1)
    
    promedio = acum / value
    return promedio


def calculate_memory():
    data = psutil.virtual_memory()._asdict()
    return data['percent']


def get_running_process():
    process_arr = []
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            process = {
                'process' : processName,
                'process_id' : processID
            }
            process_arr.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    return process_arr


def get_all_users():
    return ([(u.name) for u in psutil.users()])



running_process = json.dumps(get_running_process())

response = {
    "hostname": get_hostname(),
    "users": get_all_users(),
    "ip": get_ip(),
    "disk_usage": calculate_disk(),
    "cpu_usage": calculate_cpu(),
    "ram_usage": calculate_memory(),
    "process" : running_process
}

print(response)

api = "http://127.0.0.1:5000/register/data"
req = requests.post(api, response)
