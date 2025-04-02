__author__ = "Fabian Ha"


def read_all_words(filename: str) -> set[str]:
    """
    gibt den Inhalt von filename als set zurück
    :param filename: Pfad zur Datei
    :return: Inhalt von filename set aus strings
    """
    with open(filename) as f:
        li = f.readlines()
        return {x.strip() for x in li}


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
    """
    li = split_word(wort)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # print({x[0] + x[1][1:] for x in li})  # a)
    # print({x[0] + x[1][1] + x[1][0] + x[1][2:] for x in li if len(x[1]) >= 2})  # b)
    # print({x[0] + y + x[1][1:] for x in li for y in alphabet})    # c)
    # print({x[0] + y + x[1] for x in li for y in alphabet})    # d)
    return ({x[0] + x[1][1:] for x in li}
            .union({x[0] + x[1][1] + x[1][0] + x[1][2:] for x in li if len(x[1]) >= 2})
            .union({x[0] + y + x[1][1:] for x in li for y in alphabet})
            .union({x[0] + y + x[1] for x in li for y in alphabet}))


if __name__ == '__main__':
    print(read_all_words('C:\\Users\\fabia\\Downloads\\08_py_comprehension\\de-en\\de-en.txt'))
    print(split_word("abc"))
    print(edit1("abcd"))
