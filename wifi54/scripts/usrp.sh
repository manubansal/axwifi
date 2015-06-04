#!/bin/bash

sudo ifconfig eth1 hw ether 00:01:01:01:01:01
sudo ifconfig eth1 192.168.10.1 netmask 255.255.255.0
echo "===Initializing USRP, wait a moment and switch Ethernet to TI EVM==="
./usrp.py
