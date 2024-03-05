#!/bin/bash

sudo su
cp server-side.service /etc/systemd/system/
systemctl enable test.service
systemctl start test.service