#inner class
class Person:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        self.db = self.DOB()

    class DOB:
        def __init__(self):
            self.dt = 11
            self.mn = 11
            self.yy = 1989

        def displayDate(self):
            print(self.dt,self.mn,self.yy)

sayali = Person("sayali","jogi")
print(sayali.firstName)
print(sayali.lastName)
e = sayali.db

print(e.dt)
print(e.mn)
print(e.yy)
e.displayDate()

#program 2
class Person:
    def __init__(self,fn,ln,dd,mm,yy):
        self.firstName = fn
        self.lastName = ln
        self.db = self.DOB(dd,mm,yy)

    class DOB:
        def __init__(self,dd,mm,yy):
            self.dt = dd
            self.mm = mm
            self.yy = yy

        def displayDate(self):
            print(self.dt,self.mm,self.yy)

ashu = Person("ashu","umak",4,5,2000)
print(ashu.firstName)
print(ashu.lastName)
e = ashu.db

print(e.dt)
print(e.mm)
print(e.yy)
e.displayDate()

#program 3
class Person:
    def __init__(self,name):
        self.fullname = name

    def displayName(self):
        print(self.fullname)

    class DOB:
        def __init__(self):
            self.dd = 12
            self.mm = 7
            self.yy = 1990

        def displayDate(self):
            print(self.dd,self.mm,self.yy)

        class Display:
            greet = "hello"

chinmay = Person("chinmay deshpande")
chinmay.displayName()

q1 = Person("amol rao").DOB()
print(q1.yy)
print(q1.mm)
print(q1.dd)
q1.displayDate()

q2 = Person("ram dani").DOB().Display()
print(q2.greet)

#24 polymorphis , inheritance
#abstraction , interface


