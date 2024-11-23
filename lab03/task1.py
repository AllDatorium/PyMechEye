#1.1.Создайте класс Геометрическая фигура. Которая имеет функцию расчета
#площади.
#1.2.Создайте классы прямоугольник, круг и ромб, класс геометрическая
#фигура должен быть их родительским классом. Добавьте им необходимые атрибуты
#и перепишите функцию родительского класса.

class Object:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def findS(self):
        pass

class Rectan(Object):
    def __init__(self, a, b):
        super().__init__(a, b)
    def findS(self):
        return (self.a * self.b)

class Romby(Object):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def findS(self):
        return (self.a * self.h)

class Circl(Object):
    def __init__(self, r):
        self.r = r
    def findS(self):
        return round((self.r*self.r) * 3.14, 2)

a = Rectan(6, 9)
b = Romby(4, 6, 3)
c = Circl(3)

print("The area of the Rectangle is " + str(a.findS()))
print("The area of the Rhombus is " + str(b.findS()))
print("The area of the Circle is " + str(c.findS()))
