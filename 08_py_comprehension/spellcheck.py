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


if __name__ == '__main__':
    print(read_all_words('C:\\Users\\fabia\\Downloads\\08_py_comprehension\\de-en\\de-en.txt'))
    print(split_word("abc"))
