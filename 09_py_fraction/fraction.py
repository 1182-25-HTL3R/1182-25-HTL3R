import doctest
import functools
import math


@functools.total_ordering
class Fraction:
    """
    Representiert einen Bruch mit Nenner (numerator) und Zähler (denominator)

    Attributes:
        _numerator: Zähler des Bruchs
        _denominator: Nenner des Bruchs

    >>> Fraction(3, 6)
    Fraction(1, 2)
    >>> Fraction(-3, -6)
    Fraction(1, 2)
    >>> Fraction(-3, 6)
    Fraction(-1, 2)
    >>> Fraction(3, -6)
    Fraction(-1, 2)
    """

    def __init__(self, numerator: int = 0, denominator: int = 1):
        """
        Konstruktor für einen Bruch
        :param numerator: Zähler
        :param denominator: Nenner

        >>> Fraction(2, 4)
        Fraction(1, 2)
        >>> Fraction(-2, 4)
        Fraction(-1, 2)
        >>> Fraction(0, 5)
        Fraction(0, 1)
        >>> try:
        ...     Fraction(1, 0)
        ... except ArithmeticError:
        ...     print("ArithmeticError")
        ArithmeticError
        """
        gcd = math.gcd(numerator, denominator)

        if denominator > 0:
            self._numerator = int(numerator / gcd)
            self._denominator = int(denominator / gcd)
        else:
            if denominator == 0:
                raise ArithmeticError("Nenner darf nicht 0 sein.")

            self._numerator = int(-numerator / gcd)
            self._denominator = int(-denominator / gcd)

    @property
    def numerator(self) -> int:
        """
        Gibt den Zähler des Bruchs zurück
        :return: Zähler
        >>> Fraction(5, 2).numerator
        5
        >>> Fraction(-3, 4).numerator
        -3
        """
        return self._numerator

    @property
    def denominator(self) -> int:
        """
        Gibt den Nenner des Bruchs zurück
        :return: Nenner
        >>> Fraction(5, 2).denominator
        2
        >>> Fraction(3, -4).denominator
        4
        """
        return self._denominator

    def __str__(self) -> str:
        """
        erstellt eine sinnvolle Representation eines Bruchs
        :return: String Representation eines Bruchs
        >>> str(Fraction(3, 1))
        '3'
        >>> str(Fraction(5, 3))
        '1 2/3'
        >>> str(Fraction(2, 3))
        '2/3'
        >>> str(Fraction(-7, 3))
        '-2 1/3'
        """

        num, den = self._numerator, self._denominator
        if den == 1:
            return str(num)

        if abs(num) > den:
            return f"{int(num / den)} {abs(num) % den}/{den}"

        return f"{num}/{den}"

    def __repr__(self) -> str:
        """
        Offizielle String-Repraesentation
        :return: String Repraesentation - "Fraction(numerator, denominator)"
        >>> repr(Fraction(3, 4))
        'Fraction(3, 4)'
        >>> repr(Fraction(-2, 5))
        'Fraction(-2, 5)'
        """
        return f"{self.__class__.__name__}({self._numerator}, {self._denominator})"

    def __add__(self, other):
        """
        addiert zwei Brüche
        :param other: anderer Bruch
        :return: addierter Bruch
        >>> Fraction(1, 2) + Fraction(1, 3)
        Fraction(5, 6)
        >>> Fraction(1, 2) + 1
        Fraction(3, 2)
        >>> 1 + Fraction(1, 2)
        Fraction(3, 2)
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            return Fraction(self._numerator * other.denominator + self._denominator * other.numerator,
                            self._denominator * other.denominator)
        return NotImplemented

    def __radd__(self, other):
        """
        addiert eine Zahl mit einem Bruch
        :param other: Zahl
        :return: addierter Bruch
        >>> 1 + Fraction(3, 4)
        Fraction(7, 4)
        >>> 1 + Fraction(1, 2)
        Fraction(3, 2)
        """
        if isinstance(other, int):
            return Fraction(other) + self
        return NotImplemented

    def __sub__(self, other):
        """
        subtrahiert zwei Brüche
        :param other: anderer Bruch
        :return: subtrahierter Bruch
        >>> Fraction(3, 4) - Fraction(1, 4)
        Fraction(1, 2)
        >>> Fraction(1, 4) - 1
        Fraction(-3, 4)
        >>> 1 - Fraction(1, 4)
        Fraction(3, 4)
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            return Fraction(self._numerator * other.denominator - self._denominator * other.numerator,
                            self._denominator * other.denominator)
        return NotImplemented

    def __rsub__(self, other):
        """
        subtrahiert eine Zahl mit einem Bruch
        :param other: Zahl
        :return: subtrahierter Bruch
        >>> 1 - Fraction(1, 2)
        Fraction(1, 2)
        >>> 1 - Fraction(1, 4)
        Fraction(3, 4)
        """
        if isinstance(other, int):
            return Fraction(other) - self
        return NotImplemented

    def __mul__(self, other):
        """
        multipliziert zwei Brüche
        :param other: anderer Bruch
        :return: multiplizierter Bruch
        >>> Fraction(2, 3) * Fraction(3, 4)
        Fraction(1, 2)
        >>> Fraction(2, 3) * 3
        Fraction(2, 1)
        >>> 3 * Fraction(2, 3)
        Fraction(2, 1)
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            return Fraction(self._numerator * other.numerator, self._denominator * other.denominator)
        return NotImplemented

    def __rmul__(self, other):
        """
        multipliziert eine Zahl mit einem Bruch
        :param other: Zahl
        :return: multiplizierter Bruch
        >>> 2 * Fraction(3, 4)
        Fraction(3, 2)
        >>> 3 * Fraction(2, 3)
        Fraction(2, 1)
        """
        if isinstance(other, int):
            return Fraction(other) * self
        return NotImplemented

    def __truediv__(self, other):
        """
        dividiert zwei Brüche
        :param other: anderer Bruch
        :return: dividierter Bruch
        >>> Fraction(3, 4) / Fraction(3, 2)
        Fraction(1, 2)
        >>> Fraction(3, 4) / 2
        Fraction(3, 8)
        >>> try:
        ...     Fraction(1, 2) / Fraction(0, 1)
        ... except ArithmeticError:
        ...     print("ArithmeticError")
        ArithmeticError
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ArithmeticError("Nenner darf nicht 0 sein.")
            return Fraction(self._numerator * other.denominator, self._denominator * other.numerator)
        return NotImplemented

    def __rtruediv__(self, other):
        """
        dividiert eine Zahl mit einem Bruch
        :param other: Zahl
        :return: dividierter Bruch
        >>> 3 / Fraction(2, 3)
        Fraction(9, 2)
        >>> 1 / Fraction(1, 2)
        Fraction(2, 1)
        """
        if isinstance(other, int):
            return Fraction(other) / self
        return NotImplemented

    def __eq__(self, other):
        """
        vergleicht auf Gleichheit
        :param other: Zahl oder Bruch
        :return: Ergebnis des Vergleichs - true or false
        >>> Fraction(1, 2) == Fraction(2, 4)
        True
        >>> Fraction(3, 7) == Fraction(10, 7).__sub__(1)
        True
        >>> Fraction(1, 2) != Fraction(1)
        True
        """
        if isinstance(other, int):
            return self == Fraction(other)
        if isinstance(other, Fraction):
            return self._numerator == other.numerator and self._denominator == other.denominator
        return NotImplemented

    def __lt__(self, other):
        """
        kleiner-als-Vergleich mit Zahl oder Bruch
        :param other: Zahl oder Bruch
        :return: Ergebnis des Vergleichs - true or false
        >>> Fraction(1, 3) < Fraction(1, 2)
        True
        >>> Fraction(1, 2) < 1
        True
        >>> Fraction(3, 2) < 1
        False
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            return (self - other).numerator < 0
        return NotImplemented

    def __float__(self) -> float:
        """
        wandelt Bruch in float um
        :return: Bruch als float
        >>> float(Fraction(1, 2))
        0.5
        >>> float(Fraction(-3, 4))
        -0.75
        """
        return self._numerator / self._denominator


if __name__ == "__main__":
    doctest.testmod(verbose=True)