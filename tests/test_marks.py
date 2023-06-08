import pytest
from src.general import (
    add_one,
    add_two,
    add_three,
    add_four,
    is_palindrome,
    username_validator,
)


@pytest.mark.integers
def test_add_one():
    assert add_one(9) == 10


@pytest.mark.integers
def test_add_two():
    assert add_two(9) == 11


@pytest.mark.integers
def test_add_three():
    assert add_three(9) == 12


@pytest.mark.integers
def test_add_four():
    assert add_four(9) == 13


@pytest.mark.strings
def test_is_palindrome():
    assert is_palindrome("alomomola")
    assert not is_palindrome("rayquaza")


@pytest.mark.strings
def test_username_validator():
    assert username_validator("Mewtwo150")


@pytest.mark.strings
def test_username_validator_fails_1():
    with pytest.raises(ValueError):
        username_validator("150Mewtwo")


@pytest.mark.xfail(raises=ValueError)
@pytest.mark.strings
def test_username_validator_fails_2():
    username_validator("150Mewtwo")
