from icecream import ic
from functions.functions_file import add_numbers, divide_numbers, divide_numbers_zerodivisionerror
from classes import shapes
import pytest



def test_add():
    result = add_numbers(1, 5)
    assert result == 6

def test_add_strings():
    result = add_numbers("Shahmeer", " Khan")
    assert result == "Shahmeer Khan"

def test_divide():
    result = divide_numbers(10,2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10,0)

def test_divide_by_zero_2():
    with pytest.raises(ZeroDivisionError):
        divide_numbers_zerodivisionerror(10,0)
    
    assert divide_numbers_zerodivisionerror(10,10) == 1

# def test_divide_by_zero_3():
#     with pytest.raises(ZeroDivisionError):
#         divide_numbers_zerodivisionerror(10,0)

# Testing Rectange class 
# Pytest Fixtures
# In conftest.py file for making the fixtures global

def test_rectangle_area(my_rectangle): 

    assert my_rectangle.area() == 10*20

def test_rectangle_perimeter(my_rectangle): 
    assert my_rectangle.perimeter() == (10 + 20) * 2