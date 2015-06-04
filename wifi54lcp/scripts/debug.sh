#!/bin/bash

sudo ifconfig eth0 10.10.10.2 netmask 255.255.255.0
sudo arp -s 10.10.10.1 00:01:01:01:01:01

sudo ./eth_send_samples.py /mnt/hgfs/aschulm/Dropbox/openradio_results/traces/txrx/signal_trace_spectesting_-65dBmTX_-74dBmRX_skip0_ns3000000.bin
