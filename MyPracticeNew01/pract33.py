#Duck typing

class Human:
    def talk(self):
        print("Hello Hii")

class Dog:
    def talk(self):
        print("Bow Bow")

def obj_talk(obj):
    obj.talk()

c = Human()
d = Dog()

obj_talk(c)
obj_talk(d)

#Operator Overloading

class BookX:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages

class BookY:
    def __init__(self,pages):
        self.pages = pages

Geeta = BookX(200)
Mahabharat = BookY(150)
print(Geeta.pages + Mahabharat.pages)
print(Geeta + Mahabharat)

#Method Overloading

class Calculator:
    # def addition(self,x,y):
    #     print(x + y)
    # def addition(self,x,y,z):
    #     print(x+y+z)
    # def addition(self,x,y,z,a):
    #     print(x+y+z+a)

    def addition(self, x=None, y=None, z=None, b=None):
        if x != None and y != None and z != None and b != None:
            print(x + y + z + b)
        if x != None and y != None and z != None:
            print(x + y + z)
        if x != None and y != None:
            print(x + y)

a = Calculator()
a.addition(13,4)
a.addition(13,4,4)
a.addition(13,4,4,4)

#Method Overriding

class WorldBank:
    def loan(self):
        print("I am loan from worldBank")
    def save(self):
        print("I am save from WorldBank")

class SBI(WorldBank):
    def loan(self):
        print("I am loan from SBI")
    def save(self):
        print("I am save from SBI")

Nagpur = SBI()
Nagpur.save()
Nagpur.loan()

