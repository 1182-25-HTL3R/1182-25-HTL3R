import doctest
from collections import Counter
from typing import List, Set, Tuple
from Caesar import Caesar
from Vigènere import Vigenere


class Kasiski:
    crypttext: str

    def __init__(self, crypttext: str = ""):
        self.crypttext = crypttext

    def allpos(self, text: str, teilstring: str) -> List[int]:
        """Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []"""

        positions = []
        while text.find(teilstring) != -1:
            positions.append(text.rfind(teilstring))
            text = text[0:text.rfind(teilstring)]

        return sorted(positions)

    def alldist(self, text: str, teilstring: str) -> Set[int]:
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

    def dist_n_tuple(self, text: str, laenge: int) -> Set[Tuple[str, int]]:
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
            if text[i + laenge:].find(text[i:i + laenge]):
                teilstring = text[i:i + laenge]
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

    def ggt(self, x: int, y: int) -> int:
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

    def ggt_count(self, zahlen: List[int]) -> Counter:
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

    def get_nth_letter(self, s: str, start: int, n: int) -> str:
        """Extrahiert aus s jeden n. Buchstaben beginnend mit index start.
        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'"""

        return s[start:][::n]

    def crack_key(self, len: int) -> str:
        """
        # Text ist aus Weihnachtserzählungen Band 1 - Doktor Marigold - erste drei Absätze -> mit 'fabian' verschlüsselt
        >>> verschlüsselter_text = "ncijiajionauweoleemneteezneleesanmmrnnfavnyesawnwwjtlhrmbzittlehufjiomnyjbamigjnwmrzztfbeajioqgrqevbefjiovazjsfqwvqljimngesuevsvbbeegeiiucyeumsgjttpaeyndsitsejveemifmwvqlvuwnxmjkhnsgfptftbfontjidpmvhheimvydjmsnhhfdoakomoeaienatnsdqcnxyavazhgeuzapmtfvwrsnfaevsenuaasiomiajmgzevjnminqjnjkhgletbagyeuaevssptlfjiomnrngfveasanmnmzkfvnrswbaknsnjpmqfwpplatciqnrnnfulnsdxwsxqawmrrnhfzrfhhumryfucbsrnnxmnaraolirxadpeitmtbaaipvvkgietzetnsumrffutjegwadptryspsazbimtuzrasqgbqdbcfqnexmlggewwratcizetnsumrfjhsqmfhhxintjwbzeaznembrsspdeeqifmrfnebccubifleefufzdrrwsleaxifqhzxeizwrsihhutjsbotufbfvwrsntqemzfmtitjrxmifjsdpoaaosqhzfugoextmnmnjweoqcubuslensdfzsgfauasgwafoeotrfvuaimfqniftfzhbqtfmiajnewkgtracmrnnfzmhytfzayxdbaeejihviffugmiajrhmmrnnemwvjsfmiayrbbdvjsfzdbptpzwnwejvsrmrgzehsdmqcujrhmngqeninhsdxwlyyebtsutnpzaesidptffnomhzjnbtsrnnumegfbmmtgzneaojzremipmavadnskcirxjiucnqfltjeftnemrrfugueepsbukrntjpmtjgfvbrwdpstbwgfvaasteihngtjprznciilftdpstbwmbzittleqcugiooetjnxztvlejvmnsnjvmvytmmrrsjbprrsvpvuayesaegetfzgrxtbttvsmbvcujsumrutsfvlriesoazfsdpeaznemiajrxmsgjmjbrzjloinqjriqngjntbegxdfzrvjgftfrmluuaapaoviusspwfgfutjefxesvwvjmbvwvqlfzpyftabizreseirieseiriifaavyeomiajrwqoynnfqhexejlsvhhfzspmooqmgmebbeelexmsrsuolhngthmsrmeoeirjiomrqjrwqoynntxirqesvapmdfueefntmiajrwqoynnfoeutrdptuftumayxfmatrwetqevmmeistjhfqmansacsvjfskhgjnjkhgnnpzdaznhhufjioinvmrimrhrdsmhgjuolahkejvmnqhsbegnhseiriifaavyeqtagetfoeafutwgrmtfaahhhnqtzjiomrjjsumsbbejbevsexmsgjuolevsewqoynnfmiafnemrtqejkhfjiosnajn"
        >>> k = Kasiski(verschlüsselter_text)
        >>> k.crack_key(4)
        'fabian'
        >>> k.crack_key(7)
        'fabian'
        """
        distances = self.dist_n_list(self.crypttext, len)
        ceasar = Caesar()
        ggts = self.ggt_count(distances).most_common()
        key_len = ggts[0][0]
        if key_len == 1:
            key_len = ggts[1][0]

        key = ""
        for i in range(key_len):
            key += ceasar.crack(self.get_nth_letter(self.crypttext, i, key_len))[0]

        return key


if __name__ == "__main__":
    doctest.testmod(verbose=True)

    v = Vigenere("fabiansun")
    verschlüsselter_text = v.encrypt(
        "Ich bin ein fahrender Händler, und der Name meines Vaters war Willum Marigold. Zu seinen Lebzeiten vermuteten einige Leute, sein Name sei William, aber mein Vater behauptete stets hartnäckig, nein, er hieße Willum. Was mich angeht, so begnüge ich mich damit, die Sache von folgendem Standpunkt aus zu betrachten: Wenn es einem Mann in einem freien Lande nicht gestattet sein soll, seinen eigenen Namen zu kennen, was kann ihm da wohl noch in einem Land, wo Sklaverei herrscht, erlaubt sein? Wenn man die Sache vom Standpunkt des Registers aus betrachtet, so kam Willum Marigold auf die Welt, bevor noch Register sehr im Schwange waren – und ebenso verließ er sie auch wieder. Außerdem würden sie ihm sehr wenig zugesagt haben, wenn sie zufälligerweise schon vor ihm aufgekommen wären. Ich wurde an der Staatsstraße geboren, und mein Vater holte einen Doktor zu meiner Mutter, als das Ereignis auf einer Gemeindewiese eintrat. Dieser Doktor war ein sehr freundlicher Gentleman und wollte als Honorar nichts annehmen als ein Teetablett, und so wurde ich aus Dankbarkeit und als besondere Aufmerksamkeit ihm gegenüber Doktor genannt. Da habt ihr mich also, Doktor Marigold. Ich bin gegenwärtig ein Mann in mittleren Jahren, von untersetzter Gestalt, in Manchesterhosen, Ledergamaschen und einer Weste mit Ärmeln, an der hinten stets der Riegel fehlt. Man kann ihn so oft ausbessern, wie man will, er platzt immer wieder, wie die Saiten einer Violine. Ihr seid sicher schon im Theater gewesen und habt gesehen, wie einer der Violinspieler, nachdem er an seiner Violine gehorcht hatte, als flüstere sie ihm das Geheimnis zu, sie fürchte, nicht in Ordnung zu sein, an ihr herumdrehte, und auf einmal hörtet ihr, wie die Saite platzte. Genauso geht es auch mit meiner Weste, soweit eine Weste und eine Violine einander gleich sein können.")
    k = Kasiski(verschlüsselter_text)
    print(k.crack_key(3))
    print(k.crack_key(8))
