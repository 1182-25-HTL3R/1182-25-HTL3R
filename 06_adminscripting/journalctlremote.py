"""
Class: 4CN
Program UE06_Adminscripting - journalctlremote.py
"""
__author__ = "Fabian Ha"

import paramiko

time = input("Zeit in min: ")
host = "192.168.88.212"
username = "administrator"
keyfile = r"C:\Users\fabia\.ssh\id_ed25519"
pkey = paramiko.Ed25519Key.from_private_key_file(keyfile)
client = paramiko.SSHClient()
policy = paramiko.AutoAddPolicy()
client.set_missing_host_key_policy(policy)
client.connect(host, username=username, pkey=pkey)

stdin, stdout, stderr = client.exec_command('journalctl --since ' + '"' + time + ' minutes ago"')
print(stdout.read().decode())
client.close()