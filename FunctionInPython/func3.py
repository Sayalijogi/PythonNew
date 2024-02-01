#11 to 15 holidays
#8:30 Git class

#list
#[expression for item in iteration if condition]

#program 1
listA = [1,2,3,4,5,6,7,8,9,10]
square = [item * item for item in listA]
print(square)

#program 2
listB = [1,2,3,4,5]
add = [item + 2 for item in listB]
print(add)

#program 3
listC = [11,2,3,4,5,-55,66,-33,22]
addc = [item + 1 for item in listC if item > 0]
print(addc)

#ternary operator
addD = [item + 1 if item > 0 else item for item in listC]
print(addD)

#program 4
names = ["chinmay","shirish","ram","satish","minal"]
addE = [i.upper() for i in names]
print(addE)

addF = [item.upper() for item in names if item.startswith('s')]
print(addF)

#program 5
str = "I am learning javascript"
#[I a l j]
listWords = str.split(" ")
print(listWords)

addf = [item[0] for item in listWords]
print(addf)

#Table of 2 with list comprehension

addh = [i for i in range(2,21,2)]
print(addh)

addg = [item * 2 for item in range(1,11)]
print(addg)



