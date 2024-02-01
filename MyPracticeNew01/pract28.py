#OOPS
#Program 1
class Person:
    firstName = None
    lastName = None
    age = None
    rollNo = None
    def displayName(self):
        print(self.firstName + self.lastName)

sayali = Person()
print(sayali.firstName)
print(sayali.lastName)
print(sayali.age)
print(sayali.rollNo)
#sayali.displayName()

sayali.firstName = "sayali"
sayali.lastName = "jogi"
sayali.age = 22
sayali.rollNo = 45

print(sayali.firstName)
print(sayali.lastName)
print(sayali.age)
print(sayali.rollNo)
sayali.displayName()

#Program 2
class PersonB:
    def __init__(self,fn,ln,ag,roll):
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        self.rollNo = roll

    def displayName(self):
        print(self.firstName + self.lastName)

ashu = PersonB("ashu","umak",24,66)
chinmay = PersonB("chinmay","deshpande",32,63)
ashu.displayName()
chinmay.displayName()



