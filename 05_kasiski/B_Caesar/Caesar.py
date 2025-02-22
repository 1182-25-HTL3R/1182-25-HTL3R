import re, doctest


class Caesar:
    key: str

    def __init__(self, key=None):
        self.key = key

    @staticmethod
    def to_lowercase_letter_only(plaintext: str) -> str:
        """Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
        Kleinbuchstaben aus dem Bereich [a..z] sind.
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
        """key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.
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




if __name__ == '__main__':
    doctest.testmod(verbose=True)
    caesar = Caesar()
    print(caesar.encrypt("hallo", "b"))
