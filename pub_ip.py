import subprocess
import requests

TEAM_NAME = "default"
with open(os.path.join("/","etc", "wifinotify", "TEAM_NAME"), "r+") as team_name_file:
    TEAM_NAME = team_name_file.read().strip()

webhook_url = "https://discord.com/api/webhooks/1345273501199896597/5BQjVDqQQQOQr-LWtPEpjnF2-XyxyRW6kfRhGRK5RG3TdfPEaIS3MZ6FcLausGVpvsaL"
hostname_cmd = "hostname"
ip_command = "hostname -I"


def clean_output(output):
    return output.decode("utf-8").strip()


hostname = clean_output(subprocess.check_output(hostname_cmd, shell=True))
ipaddrs = clean_output(subprocess.check_output(ip_command, shell=True))
DIVIDER = {"-" * 32}

data = {"content": f"{DIVIDER}\nid:\n\t{TEAM_NAME}|{hostname} \nip:\n\t{ipaddrs}\n{DIVIDER}"}

response = requests.post(webhook_url, json=data)
