#!/usr/bin/env python

from pcap import pcap
from sys import stderr, stdout
from time import sleep
from socket import socket, PF_PACKET, SOCK_RAW
from sys import argv
from fcntl import ioctl
import ctypes

class ifreq(ctypes.Structure):
	_fields_ = [("ifr_ifrn", ctypes.c_char * 16), ("ifr_flags", ctypes.c_short)]

SAMPLE_SIZE = 4
SAMPLES_PER_SYMBOL = 80
ETH_INTERFACE = "eth1"

ETH_IP_UDP_VITA_HEADER = (\
	"\x00\x50\xc2\x85\x36\xb6"  # Dest MAC
	"\x00\x01\x01\x01\x01\x01"  # Src MAC
	"\x08\x00"                  # Ethertype
	"\x45\x00\x01\x64"          # IP version, services, total length
	"\x00\x00\x00\x00"          # IP ID, flags, fragment offset
	"\x05\x11\x00\x00"          # IP ttl, protocol (UDP), hdr checksum
 	"\xC0\xA8\x0A\x01"          # Source IP address
	"\xC0\xA8\x0A\x02"          # Destination IP address
	"\x00\x00\x00\x00"          # UDP source port, dest port
	"\x01\x50\x00\x00"          # UDP len, UDP checksum
	"\x04\x00\x00\x52")         # VRT header

VITA_TRAILER = (\
        "\x00\xC0\x00\x00")         # VRT trailer

stderr.write("Notice: Don't forget to update the source MAC address. Ethernet interface is \"%s\".\n" % ETH_INTERFACE)

samples = (\
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        "\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0\xF0") * 8000

# setup raw ethernet socket
s = socket(PF_PACKET, SOCK_RAW)
s.bind((ETH_INTERFACE,0))

# setup pcap
pc = pcap(name=ETH_INTERFACE)

# transmit each
for i in range(0,len(samples),SAMPLES_PER_SYMBOL*SAMPLE_SIZE):
	stderr.write("SEND\n")
	print "PACKET: ",
	for c in samples[i:i+(SAMPLES_PER_SYMBOL*SAMPLE_SIZE)]:
		print "{:02x}".format(ord(c)),
	print ""
	s.send(ETH_IP_UDP_VITA_HEADER + samples[i:i+(SAMPLES_PER_SYMBOL*SAMPLE_SIZE)] + VITA_TRAILER)
