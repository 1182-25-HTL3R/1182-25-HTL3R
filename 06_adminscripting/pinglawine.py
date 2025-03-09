"""
Class: 4CN
Program UE06_Adminscripting - pinglawine.py
"""
__author__ = "Fabian Ha"

import subprocess

"""
liest eine IP mit Netzwerk-Suffix ein und pingt alle gültigen Host-Adressen an - nicht Multigethreaded
"""

import ipaddress

ipa = input("Bitte eine IP-Adresse mit Netzwerk-Suffix in folgendem Format eingeben: x.x.x.x/x")

for host in ipaddress.ip_network(ipa).hosts():
    host = str(host)
    res = subprocess.run(['ping ', host], creationflags=subprocess.CREATE_NEW_CONSOLE)