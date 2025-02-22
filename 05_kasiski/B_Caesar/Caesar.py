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


if __name__ == '__main__':
    doctest.testmod(verbose=True)
