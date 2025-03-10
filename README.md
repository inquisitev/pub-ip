If you are having issues with DHCP ip address changing, you can install this script and get your latest IP address posted to discord.
This was used (lightly) at the 2025 HackIllinois hackathon to manage hardwired connection issues. Students setup wifi once, installed this script, and were able to always have an up to date IP address. 

***

The original discord server has been decommissioned. 
Create a discord server, expose a webhook and update this link: https://github.com/inquisitev/pub-ip/blob/4b7258febe3d2b2e467ebaa9cb018c6c6e690d78/pub_ip.py#L8

Then on each raspberry pi, run this command to install
```bash
curl -H 'Cache-Control: no-cache' -s https://raw.githubusercontent.com/inquisitev/pub-ip/master/install.sh | sudo bash
```

Optionally, Update the team name by replacing MY_TEAM_NAME in the command with your team name:
```bash
sudo sed -i 's#TEAM_NAME = "default"#TEAM_NAME = "MY_TEAM_NAME"#' /etc/wifinotify/pub_ip.py 
```
