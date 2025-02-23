import doctest
from typing import List, Set, Tuple


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

    def dist_n_tuple(self, text:str, laenge:int) -> Set[Tuple[str, int]]:
        """Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """

        dist_n = set()
        for i in range(text.__len__()):
            if text[i+laenge:].find(text[i:i+laenge]):
                teilstring = text[i:i+laenge]
                if teilstring.__len__() != laenge:
                    continue

                distances = self.alldist(text, teilstring)

                for distance in distances:
                    dist_n.add((teilstring, distance))

        return dist_n

if __name__ == "__main__":
    doctest.testmod(verbose=True)