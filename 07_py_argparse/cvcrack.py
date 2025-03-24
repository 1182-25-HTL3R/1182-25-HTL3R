__author__ = "Fabian Ha"

import argparse

def main() -> None:
    """
    argparse Programm für das Crackprogramm.
    :return: nichts
    """
    parser = argparse.ArgumentParser(
        description="Caesar und Vigenere Cracker"
    )
    parser.add_argument("infile", type=str, help="Zu verschlüsselnde Datei")
    parser.add_argument(
        "-c",
        "--cipher",
        choices=["caesar", "c", "vigenere", "v"],
        required=True,
        help="Zu verwendende Chiffre",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Ausführliche Ausgabe"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Keine Ausgabe"
    )
