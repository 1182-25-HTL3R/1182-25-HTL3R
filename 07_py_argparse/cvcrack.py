__author__ = "Fabian Ha"

import argparse
import sys, os
from Caesar import Caesar
from Kasiski import Kasiski

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

    args = parser.parse_args()

    if not os.path.isfile(args.infile):
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)

    with open(args.infile, "r", encoding="utf-8") as f:
        text = f.read()

    chiffre_typ = ""
    key = ""
    if args.cipher in ["caesar", "c"]:
        chiffre_typ = "Caesar"
        cipher = Caesar()
        key = cipher.crack(text, 1)[0]
    elif args.cipher in ["vigenere", "v"]:
        chiffre_typ = "Vigenere"
        cipher = Kasiski(text)
        key = cipher.crack_key(6)

    if args.verbose:
        print(f"Cracking {chiffre_typ}-encrypted file {args.infile}: Key = {key}")
    else:
        print(key)

if __name__ == "__main__":
    main()