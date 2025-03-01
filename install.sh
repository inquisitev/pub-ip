mkdir -p /etc/wifinotify
apt install python3.11-venv
python3 -m venv .venv
source .venv/bin/activate
pip install requests discord
sudo apt install iproute2
git clone https://github.com/inquisitev/pub-ip.git /etc/wifinotify
cd /etc/wifinotify
cp wifinotify.service /etc/systemd/system/wifinotify.service

sudo chmod 644 /etc/systemd/system/wifinotify.service
sudo systemctl daemon-reload
sudo systemctl enable wifinotify.service
sudo systemctl start wifinotify.service
