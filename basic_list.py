"""
Program: basic_list.py
Author:  Spencer Cress
Date: 06/20/2020
This program contains two functions that build a list for Basic List Assignment
"""


def get_input():
    """
    :returns: returns a string
    """
    x = input("Please input a number: ")
    return x


def make_list():
    """
    :returns: a list of numbers
    :raises ValueError: returned given non-numeric input
    """
    number_list = []
    for n in range(1, 4):
        x = get_input()
        try:
            x = int(x)
            number_list.append(x)
        except ValueError:
            print("Invalid Entry, please input a number")
    return number_list



if __name__ == '__main__':
    make_list()
