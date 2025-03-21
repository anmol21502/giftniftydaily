#!/usr/bin/env bash

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt update
apt install -y ./google-chrome-stable_current_amd64.deb

CHROME_VERSION=$(google-chrome --version | grep -oP '[0-9.]+' | head -1 | cut -d. -f1)
CHROMEDRIVER_VERSION=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}")
wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
unzip /tmp/chromedriver.zip -d /usr/bin/
chmod +x /usr/bin/chromedriver
