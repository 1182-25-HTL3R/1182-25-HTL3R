import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
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
        if self.denominator == 1:
            return str(self.numerator)

        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)
    print(f1)
    print(f2)
    print(f1 + f2)
