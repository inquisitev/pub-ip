mkdir -p /etc/wifinotify
cp ./* /etc/wifinotify
python3 -m venv .venv
source .venv/bin/activate
pip install requests discord
cd /etc/wifinotify
cp wifinotify.service /etc/systemd/system/wifinotify.service

sudo chmod 644 /etc/systemd/system/wifinotify.service
sudo systemctl daemon-reload
sudo systemctl enable wifinotify.service
sudo systemctl start wifinotify.service

