"""
Class: 4CN
Program UE06_Adminscripting - pathlib-Modul
"""
__author__ = "Fabian Ha"

"""
Liest einen absoluten Pfad ein und gibt die in der Angabe definierten Verzeichnisteile aus
"""

from pathlib import Path

p = Path(input("Absoluten Pfad einer Datei angeben!"))
print(
    f"Dateiname: {p.name}\nDateiname ohne Dateierweiterung: {p.stem}\nDateierweiterung: {p.suffix}\nTeil des Pfades vor den Verzeichnissen: {p.anchor}\nParent Verzeichnis: {p.parent}")

if p.parent.parent:
    print(p.parent.parent)
else:
    print("Parent directory does not exist!")
