names = ["chinmay","sarika","poorva","shraddha"]

#retrive
print(names[0])
#add
names.append("rahul")
print(names)
#update
names[0] = "poorva"
print(names)
#delete
names.pop()
print(names)

names.pop(1)
print(names)

#           0       1         2         3
cities = ["pune","mumbai","banglore","kolkata"]
print(cities)

print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])

#for loop using range
for x in range(len(cities)):
    #print(x)
     print(cities[x])

#program 2

countries = ["India","srilanka","bangladesh","UK"]
for x in range(len(countries)):
    #print(x)
    print(countries[x])

#program 3
fruits = ["apple","mango","banana","grapes"]
for a in fruits:
    print(a)

#program 4
a = 10
print(a)

b = a
print(b)

b = 900
print(b)
print(a)

listA = [11,22,33]
print(listA)

listB = listA
print(listB)
print(listA)

listB[0] = 99
print(listB)
print(listA)

