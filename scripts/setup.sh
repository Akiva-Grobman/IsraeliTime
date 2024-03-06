#!/bin/bash

# Install dependencies
sudo /usr/bin/python3 -m pip install -r /home/ubuntu/IsraeliTime/python-src/requirements.txt

# Setup service
ORIGINAL_USER=`whoami`
sudo su
cp server-side.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable test.service
systemctl start test.service
su $ORIGINAL_USER
