# class Student:
#     def __init__(self,fn,ln,adhar):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adhar
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
# ashu = Student("ashu","umak",24)
# print(ashu.firstName)
# print(ashu.lastName)
# print(ashu.adharNo)
# ashu.displayName()
#
# class Teacher:
#     def __init__(self,fn,ln,adhar,salary):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adhar
#         self.salary = salary
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
#     def displaySalary(self):
#         print(self.salary)
#
# chinmay = Teacher("chinmay","deshpande",34,30000)
# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.adharNo)
# print(chinmay.salary)
# chinmay.displayName()
# chinmay.displaySalary()
#

#Program 1
# class Student:
#     def __init__(self,fn,ln,adharNO):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNO
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
# class Teacher(Student):
#
#     salary = 10000
#     def displaySalary(self):
#         print(self.salary)
#
# amol = Teacher("amol","rao",1234)
# print(amol.firstName)
# print(amol.lastName)
# print(amol.adharNo)
# print(amol.salary)
# amol.displayName()
# amol.displaySalary()

#Program 2
# class Student:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
# class Teacher(Student):
#     def __init__(self,fn,ln,adharNo,salary):
#         super().__init__(fn,ln,adharNo)
#         self.salary = salary
#
#     def displaySalary(self):
#         print(self.salary)
#
# chinmay = Teacher("chinmay","deshpande",1234,35000)
# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.adharNo)
# print(chinmay.salary)
# chinmay.displaySalary()
# chinmay.displayName()

#Program 3
class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)

atreya = Son("Madhaorao","Gadge","Sandesh","Atreya")

print(atreya.firstName)
print(atreya.lastName)
print(atreya.fname)
print(atreya.sname)

atreya.displayGName()
atreya.displayFName()
atreya.displaySName()

