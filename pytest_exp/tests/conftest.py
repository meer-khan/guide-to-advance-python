import pytest 
from classes import shapes
@pytest.fixture
def my_rectangle():       
    return shapes.Rectangle(10,20) 