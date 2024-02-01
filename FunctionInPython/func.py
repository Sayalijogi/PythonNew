#function

#int as a parameter and int as return type
def add(x,y):
    return x + y
print(add(12,4))

#float as a parameter and float as return type
def sub(x,y):
    return x - y
print(sub(23.5,22.1))

#boolean as a parameter and boolean as a return type
def canDrive(age,vehicleA):
    if age >= 18 and vehicleA:
        return True
    else:
        return False
print(canDrive(18,True))

#string as a parameter and string as a return type
def greet(word):
    return "good" + word
print(greet("morning"))
print(greet("afternoon"))

#list as a parameter and list as a return type
#           0        1          2         3
cities = ["pune","banglore","kolkata","chennai"]
print(cities)
def addCity(lst):
    lst.append("nagpur")
    return lst
print(addCity(cities))

#dictionary as a parameter and dictionary as a return type
info = {
    "firstName":"sayali",
    "lastname":"jogi"
}
def addcity(info,cityvalue):
    info['city'] = cityvalue
    return info
print(addcity(info,"wardha"))

#set as a parameter and set as a return type
setA = {11,22,33,44,55}
def removeElem(setB):
    setB.remove(44)
    return setB
print(removeElem(setA))

#tuple as a parameter and tuple as a return type
country=("cuba","india","pakistan")
def addCountry(tupleB):
    tupleB = list(tupleB)       #["cuba","india","pakistan"]
    tupleB.append("srilanka")   #["cuba","india","pakistan","srilanka"]
    tupleB = tuple(tupleB)      #("cuba","india","pakistan","srilanka")
    return tupleB
print(addCountry(country))

#function as a parameter
square = lambda x: x * x
print(square(5))

#function as a return type

