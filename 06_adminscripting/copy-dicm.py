"""
Class: 4CN
Program UE06_Adminscripting - copy-dicm.py
"""
__author__ = "Fabian Ha"

"""
Liest die Verzeichnisse SourcePath und DestinationPath ein und kopiert alle Dateien mit der Extension .jpg in eine datumsbasierte Ordnerstruktur
"""

from pathlib import Path
import shutil, os

source_path = Path(input("Gib den Source Pfad an!"))
dest_path = Path(input("Gib den Destination Pfad an!"))

if source_path.is_dir() and dest_path.is_dir():
    for path in source_path.glob("*.jpg"):
        if path.stem.split("_")[0].__len__() != 8 or not path.stem.split("_")[0].isdigit():
            print(path.stem.split("_")[0])
            print("Ungültige Datei: " + str(path))
            continue

        print(path.resolve())
        name = path.name
        full_dest_path = fr"{dest_path}\{name[:4]}\{name[4:6]}\{name[6:8]}"
        os.makedirs(full_dest_path, exist_ok=True)
        shutil.copy(path, full_dest_path)
else:
    print("Absoluter Pfad ist kein Verzeichnis!")
