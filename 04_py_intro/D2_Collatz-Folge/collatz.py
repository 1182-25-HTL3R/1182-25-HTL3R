"""
Class: 4CN
Program UE04_Python_Intro - Collatz
"""
__author__ = "Fabian Ha"

from selenium.webdriver.common.devtools.v85.debugger import step_out


def collatz(n: int) -> int:
    """
    Gibt den nächsten Wert in der Collatz Reihenfolge zurück
    :param n: Int-Startwert
    :return: Nächster Wert in der Collatz Reihenfolge
    """

    if n % 2 == 0:
        return int(n / 2)
    return 3 * n + 1

def collatz_sequence(number: int, output: list = None) -> list[int]:
    """
    Gibt die Collatz Reihenfolge als Liste zurück
    :param number: Int-Startwert
    :param output: Liste der Collatz-Werte
    :return: Collatz Reihenfolge als Liste
    """

    if output is None:
        output = []
    if number == 1:
        return output

    next_value = collatz(number)
    output.append(next_value)
    return collatz_sequence(next_value, output)


if __name__ == "__main__":
    assert(collatz(11) == 34)
    assert(collatz(52) == 26)

    assert (collatz_sequence(5) == [16, 8, 4, 2, 1])
    assert (collatz_sequence(19) == [58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
