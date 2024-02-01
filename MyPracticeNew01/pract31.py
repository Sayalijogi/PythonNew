# class Mother:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayMName(self):
#         print(self.firstName + self.lastName)
#
# class Father:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#
#     def displayFName(self):
#         print(self.firstName + self.lastName)
#
# class Son(Father,Mother):
#     def __init__(self,fn,ln,sn):
#         super().__init__(fn,ln)
#         self.sname = sn
#
#     def displaySName(self):
#         print(self.sname + self.lastName)
#
# ashu = Son("Dilip","umak","Ashu")
# print(ashu.firstName)
# print(ashu.lastName)
# print(ashu.sname)
# ashu.displaySName()
# ashu.displayFName()

#Method resolution Order

class A(object):
    def method(self):
        print("A is called") # 3
        super().method()

class B(object):
    def method(self):
        print("B is called") # 5
        super().method()

class C(object):
    def method(self):
        print("C is called") # 6 [C]

class X(A,B):
    def method(self):
        print("X is called") # 2
        super().method()

class Y(B,C):
    def method(self):
        print("Y is called") # 4
        super().method()

class P(X,Y,C):
    def method(self):
        print("P is called") # 1
        super().method()

p = P()
p.method()

