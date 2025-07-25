from calculator.operations import add
"""
Unit tests for calculator operations.
This module contains test cases for the following functions from the
calculator.operations module:
- add: Tests addition of two numbers.
- subtract: Tests subtraction of two numbers.
- multiply: Tests multiplication of two numbers.
- divide: Tests division of two numbers and division by zero.
- power: Tests exponentiation of numbers.
- modulus: Tests remainder operation between two numbers.
Each test function asserts the correctness of its respective operation
using various inputs to ensure expected results.
"""
from calculator.operations import subtract
from calculator.operations import multiply
from calculator.operations import divide
from calculator.operations import power
from calculator.operations import modulus


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(5, 0) == "Error: Cannot divide by zero"


def test_power():
    assert power(2, 3) == 8


def test_modulus():
    assert modulus(10, 3) == 1
