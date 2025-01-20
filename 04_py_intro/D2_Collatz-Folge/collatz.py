"""
Class: 4CN
Program UE04_Python_Intro - Collatz
"""
__author__ = "Fabian Ha"


def collatz(n: int) -> int:
    """
    Gibt den nächsten Wert in der Collatz Reihenfolge zurück
    :param n: Int-Startwert
    :return: Nächster Wert in der Collatz Reihenfolge
    """

    if n % 2 == 0:
        return int(n / 2)
    return 3 * n + 1


if __name__ == "__main__":
    assert(collatz(11) == 34)
    assert(collatz(52) == 26)

