# Program 1
# class Calculator:
#     #class level variable
#     c = 10
#     def __init__(self,x,y,z):
#         #instance variable
#         self.x = x
#         self.y = y
#         self.z = z
#
# amol = Calculator(122,133,144)
# chinmay = Calculator(121,131,141)
# print(amol.x)
# print(amol.y)
# print(amol.z)
# print(amol.c)
#
# print(chinmay.x)
# print(chinmay.y)
# print(chinmay.z)
# print(chinmay.c)
# chinmay.c = 99
#
# print(amol.c)
# print(chinmay.c)

#Program 2 Changing value of instance level variable

class CalculatorB:
    a = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #instance level method
    def changeX(self,change):
        self.x = change

ashu = CalculatorB(12,3)
print(ashu.x)
print(ashu.y)
ashu.changeX(45)
print(ashu.x)

class CalculatorC:
    c = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def changeC(cls,ch):
        cls.c = ch

sayali = CalculatorC(3,4)
print(sayali.x)
print(sayali.y)
print(sayali.c)
sayu = CalculatorC(13,14)
print(sayu.x)
print(sayu.y)
print(sayu.c)
CalculatorC.changeC(45)
print(sayali.c)
print(sayu.c)

sayu.c = 99
print(sayu.c)
print(sayali.c)

