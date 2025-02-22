from Caesar import Caesar
import doctest


class Vigenere:
    key: str

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        verschlüsselt den plaintext mit der Vigènere-Chiffre mit key als Schlüssel

        :param plaintext: roh Text
        :param key: key ist ein String, der definiert, um wieviele Zeichen verschoben wird. Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.
        :return: verschlüsselten Text

        >>> vigenere = Vigenere("#+!x")
        >>> vigenere.encrypt("abc")
        'xyz'
        >>> vigenere.encrypt("abc", "a")
        'abc'
        >>> vigenere.encrypt("hallo", "ABABA")
        'hblmo'
        """

        if key is None:
            key = self.key
        key = Caesar.to_lowercase_letter_only(key)
        if key == "":
            raise Exception("invalid key")

        plaintext = Caesar.to_lowercase_letter_only(plaintext)

        key_index = 0
        encrypted = ""

        for i in plaintext:
            if key_index >= key.__len__():
                key_index = 0

            caesar = Caesar()
            encrypted += caesar.encrypt(i, key[key_index])

            key_index += 1

        return encrypted

    def decrypt(self, crypttext: str, key: str = None) -> str:
        """
        entschlüsselt den plaintext mit der Vigènere-Chiffre mit key als Schlüssel

        :param crypttext: verschlüsselter Text
        :param key: key ist ein String, der definiert, um wieviele Zeichen verschoben wird. Falls kein key übergeben wird, nimmt übernimmt decrypt den Wert vom Property.
        :return: entschlüsselten Text

        >>> vigenere = Vigenere("#+!x")
        >>> vigenere.decrypt("xyz")
        'abc'
        >>> vigenere.decrypt("abc", "uiop")
        'gto'
        >>> vigenere.decrypt("hblmo", "ABABA")
        'hallo'
        """

        if key is None:
            key = self.key
        key = Caesar.to_lowercase_letter_only(key)
        if key == "":
            raise Exception("invalid key")

        crypttext = Caesar.to_lowercase_letter_only(crypttext)

        key_index = 0
        decrypted = ""

        for i in crypttext:
            if key_index >= key.__len__():
                key_index = 0

            caesar = Caesar()
            decrypted += caesar.decrypt(i, key[key_index])

            key_index += 1

        return decrypted


if __name__ == '__main__':
    doctest.testmod(verbose=True)
