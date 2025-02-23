import doctest
from typing import List, Set


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

    def alldist(self, text:str, teilstring:str) -> Set[int]:
        """Berechnet die Abstände zwischen allen Vorkommnissen des Teilstrings im verschlüsselten Text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()"""

        positions = self.allpos(text, teilstring)
        distances = set()

        for i in range(positions.__len__()):
            for j in positions[i:]:
                distance = j - positions[i]
                if distance in distances or distance == 0:
                    continue

                distances.add(distance)

        return distances

if __name__ == "__main__":
    doctest.testmod(verbose=True)