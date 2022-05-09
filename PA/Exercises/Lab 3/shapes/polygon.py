import math

def def_polygon(n, name):
    class polygon:
        def __init__(self, side):
            self._side = side
        def calculate_area(self):
            return .25*n*self._side**2*(math.tan(math.pi/n)**-1)
        def calculate_perimeter(self):
            return n*self._side
        def __lt__(self, other):
            return self.calculate_area() < other.calculate_area()
        def lessthan(self,other): pass
        def __gt__(self,other):
            return not self < other
        def __str__(self):
            return "I'm a {0} and my area is {1:.2f}".format(name, self.calculate_area())

    return polygon
