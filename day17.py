dictA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":33,
    "rollNo":45
}

#retrive
print(dictA.get("age"))
print(dictA["age"])

#update
dictA["rollNo"]=50
dictA.update({"rollNo":55})
print(dictA)

#add
dictA["city"]="pune"
print(dictA)

#delete
dictA.pop("city")
dictA.popitem()
print(dictA)

#copy
vehicle={
    "color":"red",
    "type":"sedane"
}

audi = vehicle
audi["color"]="blue"
print(audi)
print(vehicle)

bwm = vehicle.copy()
bwm["color"] ="red"
print(bwm)
print(vehicle)

bwm.clear()
print(bwm)

studentB = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","html"]
}

#print(studentB[0])

for key in studentB:
    print(key,studentB[key])
print("LastName" in studentB)

for key in studentB.keys():
    print(key)

for val in studentB.values():
    print(val)

for k,v in studentB.items():
    print(k,v)

dictA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":33,
    "rollNo":45
}
q1=dictA.setdefault("city","pune")
print(q1)
print(dictA)

keys = ["rule","rule1","rule3"]
q2 = dict.fromkeys(keys,0)
print(q2)
