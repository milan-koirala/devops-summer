from calculator.operations import *

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
