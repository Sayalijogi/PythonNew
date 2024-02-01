#Single Inheritance
# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayGName(self):
#         print(self.firstName + self.lastName)
#
# class Father(GrandFather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fname = ffn
#
#     def displayFName(self):
#         print(self.fname + self.lastName)
#
# damodhar = Father("yadaorao","jogi","damodhar")
# print(damodhar.firstName)
# print(damodhar.lastName)
# print(damodhar.fname)
# damodhar.displayGName()
# damodhar.displayFName()

#Multi - level
# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayGName(self):
#         print(self.firstName + self.lastName)
#
# class Father(GrandFather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fname = ffn
#
#     def displayFName(self):
#         print(self.fname + self.lastName)
#
# class Son(Father):
#     def __init__(self,fn,ln,ffn,ssn):
#         super().__init__(fn,ln,ffn)
#         self.sname = ssn
#
#     def displaySName(self):
#         print(self.sname + self.lastName)
#
# aadi = Son("marotrao","wandhare","piyush","aadi")
# print(aadi.firstName)
# print(aadi.lastName)
# print(aadi.fname)
# print(aadi.sname)
#
# aadi.displayFName()
# aadi.displayGName()
# aadi.displaySName()

#Hierarchical Inheritance
# class Mother:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayMName(self):
#         print(self.firstName + self.lastName)
#
# class Son(Mother):
#     def __init__(self,fn,ln,ssn):
#         super().__init__(fn,ln)
#         self.sname = ssn
#
#     def displaySName(self):
#         print(self.sname + self.lastName)
#
# class Daughter(Mother):
#     def __init__(self,fn,ln,dn):
#         super().__init__(fn,ln)
#         self.dname = dn
#
#     def displayDname(self):
#         print(self.dname + self.lastName)
#
# piyush = Son("Meena","Wandhare","piyush")
# Lakshmi = Daughter("Meena","Wandhare","Lakshmi")
#
# print(piyush.firstName)
# print(piyush.lastName)
# print(piyush.sname)
# piyush.displaySName()
# piyush.displayMName()
#
# print(Lakshmi.firstName)
# print(Lakshmi.lastName)
# print(Lakshmi.dname)
# Lakshmi.displayMName()
# Lakshmi.displayDname()

#Multiple inheritance
class Father:
    def __init__(self, fn, ln):
        print("Father constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayFName(self):
        print(self.firstName + self.lastName)


class Mother:
    def __init__(self, fn, ln):
        print("Mother constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)


class Daughter(Mother,Father):
    def __init__(self,fn,ln,ddn):
        super().__init__(fn, ln)
        self.dname = ddn

    def displaySName(self):
        print(self.dname + self.lastName)

sayali = Daughter("Mamta","Jogi","Sayali")
print(sayali.firstName)
print(sayali.lastName)
print(sayali.dname)

sayali.displaySName()
sayali.displayMName()


