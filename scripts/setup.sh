#!/bin/bash

# Setup
sudo mkdir -p /var/log/fastapi

# Install dependencies
sudo /usr/bin/python3 -m pip install -r /home/ubuntu/IsraeliTime/python-src/requirements.txt

# Setup service
sudo su
cp server-side.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable test.service
systemctl start test.service
su ubuntu
