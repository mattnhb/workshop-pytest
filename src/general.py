from typing import Union, NoReturn


def add_one(number_to_add: int) -> int:
    """
    The add_one function takes a number and adds one to it.

    :param number_to_add: int: Indicate that the function expects an integer to be passed in
    :return: The result of the addition

    >>> add_one(9)
    10

    """

    return number_to_add + 1


...


def add_two(number_to_add: int) -> int:
    return number_to_add + 2


def add_three(number_to_add: int) -> int:
    return number_to_add + 3


def add_four(number_to_add: int) -> int:
    return number_to_add + 4


...


def is_palindrome(word_to_check: str) -> bool:
    """
    The is_palindrome function takes a string as input and returns True if the string is a palindrome, False otherwise.
    A palindrome is defined as a word that reads the same forwards and backwards.

    :param word_to_check: str: Specify the type of the parameter
    :return: True if the word_to_check is a palindrome, and false otherwise
    >>> is_palindrome("Girafarig")
    True
    >>> is_palindrome("Giratina")
    False
    """
    return word_to_check.lower() == word_to_check.lower()[::-1]


def username_validator(username_to_check: str) -> Union[NoReturn, str]:
    """
    The username_validator function checks to see if the username provided by the user is valid.
    It does this by checking that the first character of their username is not a number and that all characters in their
    username are alphanumeric. If either of these conditions are not met, it raises a ValueError.

    :param username_to_check: str: Specify the type of data that will be passed into the function
    :return: Either the valid username or an error
    """
    if not username_to_check[0].isdigit() and all(
        c.isalnum() for c in username_to_check
    ):
        return True
    raise ValueError(
        "Your username cannot start with a number and cannot contain special characters"
    )
