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

if __name__ == '__main__':
    print(is_palindrom('abcddcb'))