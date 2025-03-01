mkdir -p /etc/wifinotify
git clone https://github.com/inquisitev/pub-ip.git /etc/wifinotify
cd /etc/wifinotify
cp wifinotify.service /etc/systemd/system/wifinotify.service

sudo chmod 644 /etc/systemd/system/wifinotify.service
sudo systemctl daemon-reload
sudo systemctl enable wifinotify.service
sudo systemctl start wifinotify.service
