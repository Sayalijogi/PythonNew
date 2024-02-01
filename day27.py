#program 1
#constructor
class Person:
    country = "India"
    def __init__(self):
        self.firstName = "sayali"
        self.lastName = "jogi"
        self.age = 24

    def displayName(self):
        print(self.firstName + self.lastName)

sayali = Person()
print(sayali.firstName)
print(sayali.lastName)
print(sayali.age)
sayali.displayName()

chinmay = Person()
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.age)
chinmay.displayName()


class PersonB:
    country = "India"   #class parameter
    def __init__(self,fn,ln,ag):
        self.firstName = fn
        self.lastName = ln
        self.age = ag

    def displayName(self):
        print(self.firstName + self.lastName)

    @classmethod
    def updateCountry(cls,country):
        PersonB.country = country

PersonB.updateCountry("bharat")
amolB = PersonB("amolB","raoB","34")
amolC = PersonB("amolC","raoC","34")
amolB.displayName()
amolC.displayName()
print(PersonB.country)
print(PersonB.country)
amolB.country="nepal"
print(amolB.country)

#program 2
class Bank:
    def __init__(self,accName,accNo,bal):
        self.accName = accName
        self.accNo = accNo
        self.bal = bal
        self.transactions = []

    def withDrawl(self,amount):
        if self.bal > amount:
            self.bal = self.bal - amount
            self.transactions.append(-amount)
        else:
            print("insufficient balance")
        return self.bal

    def deposit(self,amount):
        self.bal = self.bal + amount
        self.transactions.append(amount)
        return self.bal

    def lastFiveTransactions(self):
        return self.transactions[-5:]

chinmay = Bank("chinmay","123",10000000)
print(chinmay.withDrawl(10000))

chinmay.deposit(10000)
chinmay.deposit(10000)
chinmay.deposit(100)
chinmay.deposit(10000)
chinmay.deposit(10)
chinmay.deposit(10000)
chinmay.withDrawl(99)
chinmay.withDrawl(100)
print(chinmay.lastFiveTransactions())
