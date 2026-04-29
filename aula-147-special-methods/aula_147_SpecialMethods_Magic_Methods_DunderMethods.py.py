# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self): #representa objetos em strings
        return f"({self.x}, {self.y})"
    
    def __repr__(self): #metodos usado para desenvolvedores
        # class_name = type(self).__name__
        class_name = __class__.__name__
        return f"({class_name} x={self.x!r}, y={self.y!r}, z={self.z!r})"
    
p1 = Ponto(3, 5)
p2 = Ponto(865, 555)
print("print do __str__")
print(p1)
print(p2)
print()
print("print do __repr__")
print(repr(p1))
print(repr(p2))
print(f"{p2!r}") #chamando repr com fstrings
