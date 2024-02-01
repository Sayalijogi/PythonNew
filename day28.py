class Employee:
    counter = 0
    def __init__(self,fn,ln,ag): #instance with parameters
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        Employee.counter = Employee.counter+1

    def displayInfo(self):
        print(self.firstName+self.lastName)

    @staticmethod
    def countofObj():  # if not self then class
        return Employee.counter

sayali = Employee('sayali','jogi',23)
q1 = Employee('kajal','dule',26)
print(Employee.countofObj())
a = Employee.countofObj()
print(a)

#---------------------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self,fullname,age,salary):
        self.fullname = fullname
        self.age = age
        self.salary = salary

    def displayinfo(self):
        print(self.fullname)
        print(self.age)
        print(self.salary)

class PersonInfo:
    @staticmethod
    def displayInfo(p):
        print(p.salary)
        print(p.fullname)
        print(p.age)

abhisha = Person("abhisha","34",salary=1000)
abhisha.displayinfo()
PersonInfo.displayInfo(abhisha)

#program 3
class PersonR:
    #class variable
    country ="India"
    counter = 0
    #setting instance variable via object
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        PersonR.counter = PersonR.counter + 1

    def displayName(self):
        print(self.firstName +self.lastName)

    @classmethod
    def updateCountry(cls,cntry):
        cls.country = cntry

    @staticmethod
    def countObj():
        return PersonR.counter

sarika = PersonR("sarika","pansare")
print(sarika.firstName)
print(sarika.lastName)
PersonR.countObj()
print(PersonR.countObj())
PersonR.updateCountry("nepal")
print(sarika.country)

