"""
Class: 4CN
Program UE06_Adminscripting - pathlib-Modul
"""
__author__ = "Fabian Ha"
"""
Ein Programm welches alle absoluten Pfade der Dateien in dem Verzeichnis und Unterverzeichnissen ausgibt mit der angegebenen Dateiendung
"""

from pathlib import Path

p = Path(input("Absoluten Pfad eines Verzeichnisses angeben!"))
ext = input("Dateinamenserweiterung angeben!")

if p.is_dir():
    for path in p.rglob(f"*.{ext}"):
        print(path.resolve())
else:
    print("Absoluter Pfad ist kein Verzeichnis!")
