#program 1
class Bookx:
    def __init__(self,x):
        self.pages = x
class Booky:
    def __init__(self,y):
        self.pages = y

b1 = Bookx(12)
b2 = Booky(24)
print(b1.pages + b2.pages)
# print(b1 + b2)

# print(1+3)
# print("hello" + "world")
# print([11,22,33] + [111+22+33])

#program 2

class Bookx:
    def __init__(self,x):
        self.pages = x
    def __add__(self, other):
        return self.pages + other.pages
class Booky:
    def __init__(self,y):
        self.pages = y

b1 = Bookx(13)
b2 = Booky(17)
print(b1 + b2)

#program 3

class Booka:
    def __init__(self,a):
        self.pages = a
    def __gt__(self, other):
        return self.pages > other.pages
class Bookb:
    def __init__(self,b):
        self.pages = b

a1 = Booka(122)
a2 = Bookb(24)
print(a1 > a2)

#program 4

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __mul__(self, other):
        return self.salary * other.days
class Attendance:
    def __init__(self,days):
        self.days = days

e1 = Employee("chinmay",100)
e2 = Attendance(30)
# print(e1 * e2)
q1 = e1 * e2
print(q1)

#overloading and overriding

class Cal:
    def addition(self,x,y):
        print(x+y)

    def addition(self,x,y,z):
        print(x+y+z)

    def addition(self,x = None,y = None,z = None,a = None):
        # print(x+y+z+a)
        if(x != None and y != None and z != None and a != None):
            print(x+y+z+a)
        elif(x != None and y != None and z != None):
            print(x+y+z)
        elif(x != None and y != None):
            print(x + y)
a = Cal()
a.addition(12,13)
a.addition(12,13,45)
a.addition(12,13,45,67)
