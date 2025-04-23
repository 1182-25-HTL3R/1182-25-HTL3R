import math


class Fraction:
    """
    Representiert einen Bruch mit Nenner (numerator) und Zähler (denominator)

    Attributes:
        _numerator: Zähler des Bruchs
        _denominator: Nenner des Bruchs
    """

    def __init__(self, numerator: int = 0, denominator: int = 1):
        """
        Konstruktor für einen Bruch
        :param numerator: Zähler
        :param denominator: Nenner
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
        """
        return self._numerator

    @property
    def denominator(self) -> int:
        """
        Gibt den Nenner des Bruchs zurück

        :return: Nenner
        """
        return self._denominator

    def __str__(self) -> str:
        """
        erstellt eine sinnvolle Representation eines Bruchs
        :return: String Representation eines Bruchs
        """

        num, den = self._numerator, self._denominator
        if den == 1:
            return str(num)

        if abs(num) > den:
            return f"{num // den} {abs(num) % den}/{den}"

        return f"{num}/{den}"

    def __repr__(self) -> str:
        """
        Offizielle String-Repraesentation

        :return: String Repraesentation - "Fraction(numerator, denominator)"
        """
        return f"{self.__class__.__name__}({self._numerator}, {self._denominator})"

    def __add__(self, other):
        """
        addiert zwei Brüche
        :param other: anderer Bruch
        :return: addierter Bruch
        """
        return Fraction(self._numerator * other.denominator + self._denominator * other.numerator,
            self._denominator * other.denominator)

    def __radd__(self, other):
        """
        addiert eine Zahl mit einem Bruch
        :param other: Zahl
        :return: addierter Bruch
        """
        if isinstance(other, int):
            return Fraction(other) + self
        return Exception

    def __sub__(self, other):
        """
        subtrahiert zwei Brüche
        :param other: anderer Bruch
        :return: subtrahierter Bruch
        """
        return Fraction(self._numerator * other.denominator - self._denominator * other.numerator,
                        self._denominator * other.denominator)

    def __rsub__(self, other):
        """
        subtrahiert eine Zahl von einem Bruch
        :param other: Zahl
        :return: subtrahierter Bruch
        """
        if isinstance(other, int):
            return Fraction(other) - self
        return Exception

    def __mul__(self, other):
        """
        multipliziert zwei Brüche
        :param other: anderer Bruch
        :return: multiplizierter Bruch
        """
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        """
        dividiert zwei Brüche
        :param other: anderer Bruch
        :return: dividierter Bruch
        """
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(-2, 3)
    print(f1)
    print(f2)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)