#program 1
class Person:
    firstname = "chinmay"
    lastName = "deshpande"
    adharNo = 123

    def displayName(self):
        print(self.firstname + self.lastName)

#obj 1
amol = Person()
print(type(amol))
print(amol.firstname)
print(amol.lastName)
print(amol.adharNo)
amol.displayName()

# amol.firstname = "amolr"
# amol.lastName = "raor"
# amol.lastName = 567
# amol.displayName()

#obj 2
chinmay = Person()
print(chinmay.firstname)
print(chinmay.lastName)
print(chinmay.adharNo)
chinmay.displayName()

#program 2
#using constructor

class Person:
    #class level
    country = "India"

    #constructor
    def __init__(self,fn,ln,adharNo):
        self.firstname = fn
        self.lastName = ln
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstname + self.lastName)

amol12 = Person("amol12","rao2",4562)
amol13 = Person("amol13","rao3",4563)
amol14 = Person("amol14","rao4",4564)

amol12.displayName()
amol13.displayName()
amol14.displayName()

print(amol12.country)
print(amol13.country)
print(amol14.country)

#program 3

class Person:
    #class level variable
    country = "india"

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    #instance method
    def updateFirstName(self,fn):
        self.firstName = fn

    def updateLastName(self,ln):
        self.lastName = ln

    @classmethod
    def changeCount(cls,cntName):
        cls.country = cntName

amol13 = Person("amko","rock")
print(amol13.firstName)
print(amol13.lastName)
print(amol13.country)
amol13.country = "nepal"
print(amol13.country)
amol13.updateFirstName("amolR")
print(amol13.firstName)

chinmay3 = Person("chinmay3","deshpande")
print(chinmay3.country)

Person.changeCount("china")
print(chinmay3.country)
chinmay3.country= "bharat"
print(chinmay3.country)


