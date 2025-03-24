"""
Class: 4CN
Program UE05_Python_Kasiski - Caesar
"""
__author__ = "Fabian Ha"

import re, doctest
from typing import List


class Caesar:
    """
    Klasse dient zur Repräsentation der Caesar-Chiffre
    :param key: Schlüssel, mit welchem verschlüsselt wird, ein Buchstabe
    """
    key: str

    def __init__(self, key):
        self.key = key

    @staticmethod
    def to_lowercase_letter_only(plaintext: str) -> str:
        """
        Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
        Kleinbuchstaben aus dem Bereich [a..z] sind.
        :param plaintext: roh Text
        :return: lowercase letter only Text

        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        >>> caesar.to_lowercase_letter_only("Test 123 ! HaLLO")
        'testhallo'
        >>> caesar.to_lowercase_letter_only("#+f329jfd0sjdfj9032")
        'fjfdsjdfj'
        """

        plaintext = plaintext.lower()
        return re.compile('[^a-z]').sub('', plaintext)

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        verschlüsselt den plaintext mit der Caesar-Chiffre mit key als Schlüssel

        :param plaintext: roh Text
        :param key: key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird. Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.
        :return: verschlüsselten Text

        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.encrypt("hallo")
        'ibmmp'
        >>> caesar.encrypt("hallo", "c")
        'jcnnq'
        >>> caesar.encrypt("xyz", "c")
        'zab'
        """

        if key is None:
            key = self.key

        plaintext = self.to_lowercase_letter_only(plaintext)

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key_index = alphabet.find(key)
        encrypted = ""

        for char in plaintext:
            char_index = alphabet.find(char)
            char_index = char_index + key_index

            if char_index >= alphabet.__len__():
                char_index = char_index - (alphabet.__len__())

            encrypted += alphabet[char_index]

        return encrypted

    def decrypt(self, crypttext: str, key: str = None) -> str:
        """
        entschlüsselt den crypttext mit der Caesar-Chiffre mit key als Schlüssel

        :param crypttext: verschlüsselter Text
        :param key: key ist ein Buchstabe, der definiert, um wieviele Zeichen zurückverschoben wird. Falls kein key übergeben wird, nimmt übernimmt decrypt den Wert vom Property.
        :return: entschlüsselter Text

        >>> caesar = Caesar("b")
        >>> caesar.decrypt("ibmmp")
        'hallo'
        >>> caesar.decrypt("jcnnq", "c")
        'hallo'
        >>> caesar.decrypt("zab", "c")
        'xyz'
        """

        if key is None:
            key = self.key

        crypttext = self.to_lowercase_letter_only(crypttext)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key_index = alphabet.find(key)
        decrypted = ""

        for char in crypttext:
            char_index = alphabet.find(char)
            char_index = char_index - key_index

            if char_index < 0:
                char_index = char_index + (alphabet.__len__())

            decrypted += alphabet[char_index]

        return decrypted

    def crack(self, crypttext: str, elements: int = 1) -> List[str]:
        """
        berechnet eine Liste mit den wahrscheinlichsten Schlüsseln

        :param crypttext: verschlüsselter Text
        :param elements: gibt die Länge der Liste vor
        :return: wahrscheinlichste Schlüssel

        >>> text='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar = Caesar()
        >>> caesar.crack(text)
        ['a']
        >>> caesar.crack(text, 100) # mehr als 26 können es nicht sein.
        ['a', 'j', 'n', 'o', 'e', 'w', 'd', 'q', 'z', 'p', 'i', 'h', 'y', 's', 'k', 'x', 'c', 'v', 'g', 'b', 'r', 'l']
        >>> crypted = caesar.encrypt(text, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'h', 'l']
        """

        crypttext = self.to_lowercase_letter_only(crypttext)
        haeufigste = dict()
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in alphabet:
            count = crypttext.count(i)
            if count != 0: haeufigste[i] = count

        haeufigste = sorted(haeufigste.items(), key=lambda item: item[1], reverse=False)
        output = []

        for i in range(elements):
            if i > 26 or i >= haeufigste.__len__():
                break

            output.append(self.decrypt(haeufigste[::-1][i][0], "e"))

        return output


if __name__ == '__main__':
    doctest.testmod(verbose=True)
