import math


class Fraction:
    """
    Representiert einen Bruch mit Nenner (numerator) und Zähler (denominator)
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Konstruktor für einen Bruch
        :param numerator: Nenner
        :param denominator: Zähler
        """
        gcd = math.gcd(numerator, denominator)

        if denominator > 0:
            self.numerator = int(numerator / gcd)
            self.denominator = int(denominator / gcd)
        else:
            if denominator == 0:
                raise ZeroDivisionError

            self.numerator = int(-numerator / gcd)
            self.denominator = int(-denominator / gcd)

    def __str__(self):
        """
        erstellt eine sinnvolle Representation eines Bruchs
        :return: String Representation eines Bruchs
        """
        if self.denominator == 1:
            return str(self.numerator)

        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        """
        addiert zwei Brüche
        :param other: anderer Bruch
        :return: addierter Bruch
        """
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        """
        subtrahiert zwei Brüche
        :param other: anderer Bruch
        :return: subtrahierter Bruch
        """
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

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
