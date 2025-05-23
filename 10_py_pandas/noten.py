__author__ = "Fabian Ha, 4CN"

import os
import sys
import argparse
import pandas as pd
import re


def file_exists(path):
    """
    Prüft ob die Datei existiert und ob der angegebene Pfad ein gültiger ist.
    Gibt standardisierte Fehlermeldungen in stderr aus.
    :param path: Pfad zur Datei
    :return: True wenn Datei existiert und gültig ist, False wenn nicht
    """
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
    """
    Liste eine XML-Datei ein und extrahiert die relevanten Felder als DataFrame
    :param filename: Dateiname zu der XML-Datei
    :return: extrahierte Felder in einem DataFrame
    """
    file_exists(filename)
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"<Schueler>.*?<Nummer>(\d+)</Nummer>.*?<Anrede>(.*?)</Anrede>.*?<Vorname>(.*?)</Vorname>.*?<Nachname>(.*?)</Nachname>.*?<Geburtsdatum>(.*?)</Geburtsdatum>.*?</Schueler>",
        re.DOTALL)
    result = re.findall(pattern, content)

    return pd.DataFrame(result, columns=["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum"], dtype=str)


def read_csv(filename: str) -> pd.DataFrame:
    """
    List eine CSV-Datei mit Notendaten ein
    :param filename: Dateiname der CSV-Datei
    :return: extrahierte Felder in einem DataFrame
    """
    file_exists(filename)
    return pd.read_csv(filename, sep=";")


def main() -> None:
    """
    Hauptfunktion des Programms.
    """
    parser = argparse.ArgumentParser(description="noten.py by Fabian Ha / HTL Rennweg")
    parser.add_argument("outfile", help="Ausgabedatei (z.B. result.csv)")
    parser.add_argument("-n", help="csv-Datei mit den Noten")
    parser.add_argument("-s", help="xml-Datei mit den Schülerdaten")
    parser.add_argument("-m", default="Nummer", help="Name der Spalte, die zu verknüpfen ist (default = Nummer)")
    parser.add_argument("-f", help="Name des zu filternden Gegenstandes (z.B. SEW)")
    m = parser.add_mutually_exclusive_group(required=False)
    m.add_argument("-v", "--verbose", action="store_true", help="Gibt die Daten Kommandozeile")
    m.add_argument("-q", "--quiet", action="store_true", help="keine Textausgabe")
    args = parser.parse_args()

    df_xml = read_xml(args.s)
    df_csv = read_csv(args.n)

    df_xml[args.m] = df_xml[args.m].astype(str)
    df_csv[args.m] = df_csv[args.m].astype(str)
    df_xml.set_index(args.m, inplace=True)
    df_csv.set_index(args.m, inplace=True)

    df_joined = df_xml.join(df_csv)
    df_joined.reset_index(inplace=True)

    if args.f:
        subjects = args.f.split(",")
        cols = ["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum"] + subjects
        df_joined = df_joined[cols]
        if len(subjects) > 1:  # es gibt mehr als 1 Fach -> BONUS: Spalte Schnitt wird erstellt
            df_joined["Schnitt"] = df_joined[subjects].astype(float).mean(axis=1).round(2)

    df_joined.to_csv(args.outfile, index=False)

    if args.verbose and not args.quiet:
        sys.stdout.write("python " + " ".join(sys.argv))
        sys.stdout.write(f"\ncsv-Datei mit den Noten : {args.n}\n")
        sys.stdout.write(f"xml-Datei mit den Schülerdaten : {args.s}\n")
        sys.stdout.write(f"Name der Spalte, die zu verknüpfen ist : {args.m}\n")
        sys.stdout.write(f"Output-Datei : {args.outfile}")


if __name__ == '__main__':
    main()
