__author__ = "Fabian Ha"

import doctest


def read_all_words(filename: str) -> set[str]:
    """
    gibt den Inhalt von filename als set zurück
    :param filename: Pfad zur Datei
    :return: Inhalt von filename set aus strings
    """
    with open(filename) as f:
        li = f.readlines()
        return {x.strip().lower() for x in li}


def split_word(wort: str) -> list[tuple[str, str]]:
    """
    bestimmt eine Liste aller Aufteilungen des Wortes
    :param wort: string Wort, das aufgeteilt wird
    :return: Liste aus Tuplen mit Aufteilungen
    """
    return [(wort[:x], wort[x:]) for x in range(len(wort) + 1)]


def edit1(wort: str) -> set[str]:
    """
    bestimmt mit dem Ergebnis von split_word() alle möglichen Wörter mit einem Fehler
    a) ein Buchstabe fehlt
    b) zwei Buchstaben verdreht sind
    c) ein Buchstabe durch einen anderen Buchstaben ersetzt wurde
    d) ein Buchstabe eingefügt wurde
    :param wort: Wort welches auf Fehler angesehen wird
    :return: Set aus möglichen Wörtern

    >>> my_set = edit1("ab")
    >>> my_set == {'aob', 'oab', 'ib', 'pab', 'akb', 'al', 'zb', 'yb', 'apb', 'ob', 'aqb', 'lb', 'ah', 'ahb', 'pb', 'am', 'fb', 'ac', 'axb', 'abu', 'tab', 'fab', 'sab', 'rb', 'abw', 'abo', 'vb', 'nab', 'vab', 'abc', 'abq', 'ay', 'abn', 'mab', 'nb', 'abi', 'ak', 'abk', 'iab', 'aeb', 'anb', 'bb', 'af', 'azb', 'ab', 'abe', 'abs', 'cb', 'acb', 'hb', 'jb', 'au', 'abj', 'rab', 'avb', 'ae', 'abb', 'abp', 'gb', 'eab', 'eb', 'av', 'aj', 'atb', 'az', 'asb', 'wb', 'ar', 'sb', 'mb', 'abg', 'aub', 'abm', 'abv', 'ayb', 'ad', 'xab', 'qb', 'bab', 'yab', 'ap', 'aq', 'aab', 'b', 'uab', 'a', 'ba', 'wab', 'at', 'as', 'arb', 'ao', 'ag', 'ai', 'alb', 'kb', 'aw', 'jab', 'lab', 'qab', 'abh', 'aby', 'ub', 'aba', 'afb', 'aa', 'ajb', 'hab', 'gab', 'aib', 'xb', 'adb', 'awb', 'agb', 'abr', 'dab', 'amb', 'abt', 'abl', 'ax', 'tb', 'kab', 'db', 'abd', 'zab', 'cab', 'abz', 'abf', 'abx', 'an'}
    True
    """
    li = split_word(wort)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ({x[0] + x[1][1:] for x in li}
            .union({x[0] + x[1][1] + x[1][0] + x[1][2:] for x in li if len(x[1]) >= 2})
            .union({x[0] + y + x[1][1:] for x in li for y in alphabet})
            .union({x[0] + y + x[1] for x in li for y in alphabet}))


def edit1_good(wort: str, alle_woerter: list[str]) -> set[str]:
    """
    liefert nur die richtigen Wörter aus dem Wörterbuch
    :param wort: Wort welches überprüft wird
    :param alle_woerter: Liste aller Wörter
    :return: die richtigen Wörter
    """
    return edit1(wort.lower()) & set(alle_woerter)


def edit2_good(wort: str, alle_woerter: list[str]) -> set[str]:
    """
    bestimmt wörter mit edit-Distanz zwei
    :param wort: Wort welches überprüft wird
    :param alle_woerter: Liste aller Wörter
    :return: die richtigen Wörter
    """
    edit2 = set.union(*[edit1(w.lower()) for w in edit1(wort.lower())])
    return edit2 & set(alle_woerter)


def correct(word: str, alle_woerter: list[str]) -> set[str]:
    """
    Findet die Korrektur(en) für word als "Liste":
    • entweder ist das Wort im Wörterbuch (Ergebnis: eine Liste mit einem Eintrag word)
    • oder (mindestens) ein Wort mit Edit-Distanz eins ist im Wörterbuch (Ergebnis: Liste dieser Wörter)
    • oder (mindestens) ein Wort mit Edit-Distanz zwei ist im Wörterbuch (Ergebnis: Liste dieser Wörter)
    • oder wir haben keine Idee (zu viele Fehler oder unbekanntes Wort): liefere eine leere Liste
    :param word: Wort welches überprüft wird
    :param alle_woerter: Liste aller Wörter
    :return: die Korrekturen für word als "Liste"
    >>> woerter = list(read_all_words("de-en.txt"))
    >>> sorted(correct("Aalsuppe", woerter))
    ['aalsuppe']
    >>> sorted(correct("Alsuppe", woerter))
    ['aalsuppe']
    >>> sorted(correct("Alsupe", woerter))
    ['aalsuppe', 'absude', 'alse', 'lupe']

    die Test-Beispiele in der Angabe geben in meinen Augen keinen Sinn:
        Z.B.: "Aalsuppe" soll ['aalquappe', 'aalsuppe', 'aalsuppen'], was die Ergebnisse für edit Distanz 1 sind,
        jedoch haben wir in der Funktion edit1 explizit festgelegt, dass alle Wörter .lower() gemacht werden.

        Oder: "Alsuppe" soll ['aalsuppe', 'aalsuppen', 'suppe', 'ursuppe'] zurückgeben, was die Ergebnisse für edit Distanz 2 sind,
        aber wenn man Alsuppe sofort zu alsuppe macht (.lower()), dann ist leicht erkennbar, dass es edit Distanz 1 ist.
    """
    return {word.lower()} if word.lower() in alle_woerter else edit1_good(word, alle_woerter) or edit2_good(word, alle_woerter) or set()


if __name__ == '__main__':
    all_words = read_all_words('de-en.txt')
    print(split_word("abc"))
    print(edit1("ab"))
    doctest.testmod()
    print(edit1_good("Pyton", list(all_words)))
    print(edit2_good("Pyton", list(all_words)))
    print(correct("Platon", list(all_words)))
    print(correct("Plaaton", list(all_words)))
    print(correct("Plaaaton", list(all_words)))
    # a or b gibt a zurück wenn a true ist, sonst b
    # a | b gibt eine Vereinigung der sets zurück, also alle Elemente
