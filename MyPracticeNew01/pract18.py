listA = ["chinmay","deshpande",45,66]
#retrive
print(listA[0])
# update
listA[1] = "dani"
# add
listA.append("pune")
#delete
#del listA
# total number of element
print(len(listA))

listA =["chinmay","deshpande",45,66]
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
#dict does not store value by index
q2 = info['firstName']
print(q2)
#update
info['lastName']= "dani"
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
car.get("model")

#Dictionary

info = ["chinmay","deshpande",34,56]
info2 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "skills":["python","django","javascript"]
}
print(info2)

#Dictionary stores the value by index
#print(info2[0])

#retrive
q1 = info2['firstName']
print(q1)

#update
info2['firstName'] = "tanmay"
print(info2)

#add
info2['city'] = "pune"
print(info2)

#delete
#del info2
print(len(info2))

#dictionary

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}

#get()
print(vehicle.get('regNo'))
#vehicle['regNogg']
q1 = vehicle.get("regNo")
print(q1)

#program 2 #pop()
vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}
vehicle.pop('color')
print(vehicle)

#program 3
vehicle.clear()
print(vehicle)

#program 4
student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "skills":["python","javascript"]
}
print(student)
print(type(student))
print("age" in student)
print(student.keys())

for key in student.keys():
    print(key)

for val in student.values():
    print(val)

for k,v in student.items():
    print(k,v)

country = {
    "cities":356,
    "states":29,
    "pincode":1000
}
print(country['cities'])
for key in country:
    print(key,country[key])

for key in country.keys():
    print(key)

for val in country.values():
    print(val)

for k,v in country.items():
    print(k,v)

