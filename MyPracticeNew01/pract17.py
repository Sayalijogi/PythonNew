listA = ["chinmay","deshpande",45,66]
#retrive
print(listA[0])
#update
listA[1] = "dani"
print(listA)
#add
listA.append("pune")
print(listA)
#delete
#del listA
#total number of element
print(len(listA))

listA = ["chinmay","deshpande",45,66]
for item in listA:
    print(item)

for item in range(len(listA)):
    print(listA[item])

#dict
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":45,
    "rollNo":65
}
#dict does not stores the value by index
q2 = info['firstName']
print(q2)

#update
info['lastName'] = "dani"
print(info)

#add
info['city'] = "pune"
print(info)

#delete
#del info
print(len(info))

#check whether element is present
#looping through list
cities = ["wardha","pune","nagpur"]
for item in cities:
    print(item)
print("wardha" in cities)

info2 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
}
print("age" in info2)
for item in info2:
    #print(item)
    print(item,info2[item])

car = {
    "color":"blue",
    "model":"Q4",
    "company":"Audi"
}

for item in car:
    print(item,car[item])

#get()
q3 = car.get("model")
print(q3)

