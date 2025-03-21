sudo rm -r /etc/wifinotify
sudo rm /etc/systemd/system/wifinotify.service
sudo mkdir -p /etc/wifinotify
sudo apt install -y python3.11-venv || echo "venv already installed"
python3 -m venv .venv
source .venv/bin/activate
pip install requests discord
sudo apt install -y iproute2 || echo "iproute2 already installed"
git clone https://github.com/inquisitev/pub-ip.git /etc/wifinotify
cd /etc/wifinotify
sudo chmod +x /etc/wifinotify/run.sh
sudo cp wifinotify.service /etc/systemd/system/wifinotify.service

sudo chmod 644 /etc/systemd/system/wifinotify.service
sudo systemctl daemon-reload
sudo systemctl enable wifinotify.service
sudo systemctl start wifinotify.service
