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

# in der cmd: ssh-keygen
# Welche Dateien werden erzeugt – wie lautet deren absoluter Pfad?
# id_ed25519 und id_ed25519.pub
# C:\Users\fabia\.ssh\id_ed25519(.pub)
# es wird ein randomart image zum key angezeigt

# in der cmd: type C:\Users\fabia\.ssh\id_ed25519.pub | ssh administrator@192.168.88.212 "cat >> .ssh/authorized_keys"
# Welche Daten werden kopiert (Quelle – Ziel)?
# der public key also id_ed25519.pub von meinem lokalen Rechner auf die Linux VM, um mich in Zukunft ohne Passwort anmelden zu können
# Warum darf der private-key die eigene Maschine NIEMALS verlassen?
# Mit dem private-key kann man sich in Kombination mit dem public key authentifizieren. Wer auch immer den private-key hat kann sich also einloggen. In falschen Händen kann das gefährlich werden.

# Was passiert jetzt beim Verbinden mit ssh user@IP-Adresse? Wird nach einem Passwort gefragt?
# Es wird eine SSH-Verbindung ohne Passwort aufgebaut.

# Warum gilt die Authentifizierung mittels Schlüsselpaar als sicherer als ein Login mittels herkömmlicher Passwörter?
# Passwörter können vergessen werden, Passwörter können einfacher geklaut werden weil meist mit ihnen unvorischtiger umgegangen wird, herkömmliche Passwörter sind weitaus knackbarer als die Keys welche z.B. durch SHA256 erstellt werden.