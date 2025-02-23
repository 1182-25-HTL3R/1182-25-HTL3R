import doctest
from collections import Counter
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

    def dist_n_list(self, text: str, laenge: int) -> List[int]:
        """Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []"""

        dist_n = []
        for i in range(text.__len__()):
            if text[i + laenge:].find(text[i:i + laenge]):
                teilstring = text[i:i + laenge]
                if teilstring.__len__() != laenge:
                    continue

                distances = self.alldist(text, teilstring)

                for distance in distances:
                    if distance not in dist_n:
                        dist_n.append(distance)

        return sorted(dist_n)

    def ggt(self, x:int, y:int) -> int:
        """Ermittelt den größten gemeinsamen Teiler von x und y.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(10, 25)
        5"""

        if x == y:
            return y
        else:
            while y != 0:
                if x > y:
                    x = x - y
                else:
                    y = y - x

            return x

    def ggt_count(self, zahlen:List[int]) -> Counter:
        """
        >>> from collections import Counter
        >>> c=Counter([5,8,6,5,3,8,5,3,6,5])
        >>> print(c)
        Counter({5: 4, 8: 2, 6: 2, 3: 2})
        >>> c.most_common()
        [(5, 4), (8, 2), (6, 2), (3, 2)]

        Bestimmt die Häufigkeit der paarweisen ggt aller Zahlen aus list.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt_count([12, 14, 16])
        Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        >>> k.ggt_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        """

        ggts = []

        for pos, zahl1 in enumerate(zahlen):
            for zahl2 in zahlen[pos:]:
                ggts.append(self.ggt(zahl1, zahl2))

        return Counter(ggts)

    def get_nth_letter(self, s:str, start:int, n:int) -> str:
        """Extrahiert aus s jeden n. Buchstaben beginnend mit index start.
        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'"""

        return s[start:][::n]



if __name__ == "__main__":
    doctest.testmod(verbose=True)