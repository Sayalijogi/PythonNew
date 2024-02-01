#program 1
x = 10
print(x)
print(type(x))  #int

#program 2
y = 12.3
print(y)
print(type(y))  #float

#program 3
z = True
print(z)
print(type(z))  #boolean

#program 4
v = "chinmay"
print(v)
print(type(v))   #string

#program 5
names = ["chinmay","poorva","sarika","ram"]
print(names)
print(type(names))   #list

#program 6
cities = ("pune","nagpur")
cities2 = "wardha","nagpur"
print(cities)
print(cities2)
print(type(cities))   #tuple
print(type(cities2))

#program 7
info = {11,22,33,44,33,44,55}
print(info)  #set does not allow duplicate values
print(type(info))  # set

# program 8
info2 = {
    "firstName":"sayali",
    "lastName":"jogi"
}
print(info2)
print(type(info2))  #dict

# program 9
# operators

#Arithmetic Operators
# +, - , * ,  / , %
a = 10
b = 5
print(a+b)

firstname = "chinmay"
lastname = "deshpande"
print(firstname + lastname)

q1 = 10
q2 = 5

print(q1 + q2)
print(q1 - q2)
print(q1 * q2)
print(q1 / q2)
print(q1 % q2)

#comparison operator
# entity < entity --- boolean  True or False
# < , > , <= , >= , == , !=
#progarm 10
print(12 < 4)  #False
print(12 > 4)  #True
print(12 !=  4)  #True
print(12 ==  4)   #False
print(12 ==  12)  #True
print(12 >=  12)  #True
print(12 <=  12)  #True
print(12 <=  13)  #True
print(12 >=  13)  #False

#logical operators
#AND
# True  and  True  ----> True
# False and  True  ----> False
# True  and  False  ----> False
# False  and False  ----> False

print(3 == 3 and 4 == 4)  #true
print(3 != 3 and 4 == 4)  #false
print(3 == 3 and 4 != 4)  #false
print(3 != 3 and 4 != 4)  #false

# OR
# True  and  True  ----> True
# False and  True  ----> True
# True  and  False  ----> True
# False  and False  ----> False

print(3 == 3 and 4 == 4)  #true
print(3 == 3 and 4 == 4)  #true
print(3 == 3 and 4 == 4)  #true
print(3 != 3 and 4 != 4)  #false

#not
#not True --- False
#not False --- True

print(not(6 == 3))  #not(False)=True
print(not(6 == 6))  #not(True)=False

#conditional statements