from classes import shapes
import math

class TestCirlce:

    def setup_method(self,method):
        print("START OF SETUP METHOD",method)
        self.circle = shapes.Circle(10)

    def teardown_method(self,method):
        print("START OF TEARDOWN METHOD",method)
        del self.circle


    def test_area(self):
        # print("HELLO MY FRIEDN")
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    
    def test_perimeter(self): 
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected