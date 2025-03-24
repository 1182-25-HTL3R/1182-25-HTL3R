__author__ = "Fabian Ha"

import argparse
import sys
from Caesar import Caesar
from Vigènere import Vigenere
import os

def main() -> None:
    """
    argparse Programm für Caesar und Vigenere Ver- und Entschlüsselung
    :return: nichts
    """
    parser = argparse.ArgumentParser(
        description="Caesar und Vigenere Entschlüsselungs- und Verschlüsselungsprogramm",
    )
    parser.add_argument("infile", type=str, help="Zu verschlüsselnde Datei")
    parser.add_argument("outfile", type=str, help="Zieldatei")
    parser.add_argument(
        "-c",
        "--cipher",
        choices=["caesar", "c", "vigenere", "v"],
        help="Zu verwendende Chiffre"
    )
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument(
        "-v", "--verbose", action="store_true", help="Ausführliche Ausgabe"
    )
    verbosity_group.add_argument(
        "-q", "--quiet", action="store_true", help="Keine Ausgabe"
    )

    encryption_group = parser.add_mutually_exclusive_group()
    encryption_group.add_argument(
        "-d", "--decrypt", action="store_true", help="Entschlüsseln"
    )
    encryption_group.add_argument(
        "-e", "--encrypt", action="store_true", help="Verschlüsseln"
    )

    parser.add_argument(
        "-k", "--key", type=str, help="Encryption key"
    )

    args = parser.parse_args()


    if not args.encrypt and not args.decrypt:
        parser.error("Eines von --encrypt oder --decrypt muss angegeben werden .")


    if not os.path.isfile(args.infile):
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)

    with open(args.infile, "r", encoding="utf-8") as f:
        text = f.read()

    if args.cipher in ["caesar", "c"]:
        cipher = Caesar(args.key)
    else:
        cipher = Vigenere(args.key)

    if args.encrypt:
        ergebnis = cipher.encrypt(text)
        action = "Encrypting"
    else:
        ergebnis = cipher.decrypt(text)
        action = "Decrypting"

    with open(args.outfile, "w") as f:
        f.write(ergebnis)

    if not args.quiet and args.verbose:
        print(
            f"{action} {args.cipher} with key = {args.key} from file {args.infile} into file {args.outfile}"
        )

if __name__ == "__main__":
    main()