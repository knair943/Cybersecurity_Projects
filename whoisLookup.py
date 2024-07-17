# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:33:16 2024

@author: knair
"""

import socket

def whois_lookup(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send("domain\r\n".encode())
    response = s.recv(4096).decode()
    s.close()
    return response

print(whois_lookup("google.com"))
    