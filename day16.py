dictB = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":11,
    "rollNo":45
}
for key in dictB:
    print(key,dictB[key])

for key in dictB:
    if key == 'firstName':
        print(dictB[key])

vehicle = {
    "color":"red",
    "regNo":123
}

#vehicleB = vehicle
#vehicleB['color'] = "blue"
#print(vehicleB)
#print(vehicle)

#copy()
vehicleC = vehicle.copy()
print(vehicleC)
print(vehicle)
vehicleC['color'] = "purple"
print(vehicleC)
print(vehicle)

vehicle = {
    "color":"red",
    "regNo":"123",
    "city":"pune"
}

#keys()
for x in vehicle.keys():
    print(x)

#values()
for x in vehicle.values():
    print(x)

#items()
for x,y in vehicle.items():
    print(x,y)

#clear()
vehicle.clear()
print(vehicle)

student = {
    "marks":[11,22,33,4],
    "school":"DPS",
    "language":"English"
}
#print(student)
# # popitem()
#student.popitem()
#
# #pop()
#student.pop("school")
#print(student)

student.update({"age":25})
print(student)

q1=student.get("age")
print(q1)



