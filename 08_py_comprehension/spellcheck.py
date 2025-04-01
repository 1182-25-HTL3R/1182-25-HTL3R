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


if __name__ == '__main__':
    print(read_all_words('C:\\Users\\fabia\\Downloads\\08_py_comprehension\\de-en\\de-en.txt'))
