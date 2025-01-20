"""
Class: 4CN
Program UE04_Python_Intro
"""
__author__ = "Fabian Ha"

def is_palindrom (s:str) -> bool:
    """
    check if string is palindrom
    :param s: string to be checked
    :return: True -> palindrom, False -> no palindrom
    """

    return s.lower() == s[::-1].lower()

def is_palindrom_sentence(s:str) -> bool:
    """
    check if string sentence is palindrom
    :param s: string sentence to be checked
    :return: True -> palindrom, False -> no palindrom
    """

    s2 = ""
    for ch in s:
        if ch.isalnum():
            s2 += ch

    return is_palindrom(s2)


def palindrom_product(x: int) -> int:
    """
    creates the biggest palindrom number out of two 3-digit numbers that are smaller than x
    :param x: the highest number for a palindrom
    :return: the biggest palindrom number out of two 3-digit numbers that are smaller than x
    """

    biggest_pal = 0

    for a in range (999, 99, -1):
        for b in range (999, 99, -1):
            product = a * b
            if product >= x:
                continue
            if is_palindrom(str(product)) and product > biggest_pal:
                biggest_pal = product

    return biggest_pal

def to_base (number: int, base: int) -> str:
    """
    converts number to other base
    :param number: Zahl im 10er-System
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    """

    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    s = ""

    while number > 0:
        x = list[number%base]
        number = number//base
        s = x + s

    return s

if __name__ == '__main__':
    print(is_palindrom('abcddcb'))