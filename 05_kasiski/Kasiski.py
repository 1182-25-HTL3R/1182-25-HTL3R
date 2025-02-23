import doctest
from typing import List


class Kasiski:
    crypttext: str

    def __init__(self, crypttext: str = ""):
        self.crypttext = crypttext

    def allpos(self, text:str, teilstring:str) -> List[int]:
        """Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []"""

        positions = []
        while text.find(teilstring) != -1 :
            positions.append(text.rfind(teilstring))
            text = text[0:text.rfind(teilstring)]

        return sorted(positions)

if __name__ == "__main__":
    doctest.testmod(verbose=True)