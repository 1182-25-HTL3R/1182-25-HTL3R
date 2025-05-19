import os
import sys
import argparse
import pandas as pd
import re

def file_exists(path):
    if not os.path.exists(path):
        i = 2
        error = os.strerror(i)
        sys.stderr.write(f"Error code {i}: " + error)
        sys.exit(i)
    if os.path.isdir(path):
        i = 21
        error = os.strerror(21)
        sys.stderr.write(f"Error code {i}: " + error)
        sys.exit(i)
    return True

def read_xml(filename: str) -> pd.DataFrame:
    file_exists(filename)
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read

    pattern = re.compile(r"<Schueler>.*?<Nummer>(\d+)</Nummer>.*?<Anrede>(.*?)</Anrede>.*?<Vorname>(.*?)</Vorname>.*?<Nachname>(.*?)</Nachname>.*?<Geburtsdatum>(.*?)</Geburtsdatum>.*?</Schueler>", re.DOTALL)
    result = re.findall(pattern, content)

    return pd.DataFrame(result, columns=["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum"], dtype=str)

def main():
    parser = argparse.ArgumentParser(description="noten.py by Fabian Ha / HTL Rennweg")
    parser.add_argument("outfile", help="Ausgabedatei (z.B. result.csv)")
    parser.add_argument("-n", help="csv-Datei mit den Noten")
    parser.add_argument("-s", help="xml-Datei mit den Schülerdaten")
    parser.add_argument("-m", help="Name der Spalte, die zu verknüpfen ist (default = Nummer)")
    parser.add_argument("-f", help="Name des zu filternden Gegenstandes (z.B. SEW)")
    m = parser.add_mutually_exclusive_group(required=False)
    m.add_argument("-v", "--verbose", store_true=True, help="Gibt die Daten Kommandozeile")
    m.add_argument("-q", "--quiet", store_true=True, help="keine Textausgabe")
    args = parser.parse_args()


if __name__ == '__main__':
    main()
