#!/bin/bash

# Setup
sudo mkdir -p /var/log/fastapi

# Install dependencies
sudo /usr/bin/python3 -m pip install -r /home/ubuntu/IsraeliTime/python-src/requirements.txt

# Setup service
sudo cp server-side.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable test.service
sudo systemctl start test.service
