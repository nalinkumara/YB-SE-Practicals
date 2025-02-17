import pytest
from mypackage.calculator import add, subtract, multiply, divide, factorial, power, user_input, is_prime

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_factorial():
    assert factorial(5) == 120

def test_prime():
    assert is_prime(3) == True

def test_power():
    assert power(2, 3) == 8
    
def test_invalid_input(monkeypatch):
    """Test when the user inputs invalid data."""
    monkeypatch.setattr('builtins.input', lambda _: "3 7 9")  # Too many numbers
    with pytest.raises(ValueError, match="Invalid input"):
        user_input()