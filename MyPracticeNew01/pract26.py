#string as a parameter and string as a return type
def greet(name):
    return "hello"  + name
q1 = greet("sayali")
print(q1)

#list as a parameter and list as a return type
city = ["pune","mumbai","bangalore","Kolkata"]
def addCity(lst):
    lst.append("nagpur")
    return lst
q2 = addCity(city)
print(q2)

#dictionary as a parameter and dictionary as a return type
info = {
    "firstName":"sayali",
    "lastName":"jogi"
}
def addLanguage(information):
    information.update({"language":"marathi"})
    return information
q3 = addLanguage(info)
print(q3)

#tuple as a parameter and tuple as a return type
names = ("sayali","ashu","vrushali","kabir","chinmay")
def addElementToTuple(nmT):
    nmT = list(nmT)
    nmT.append("amol")
    nmT = tuple(nmT)
    return nmT
q4 = addElementToTuple(names)
print(q4)

#set as a parameter and set as a return type
setA = {11,22,33,44,55}

def addSetCValue(setToAdd):
    setToAdd.add(34)
    return setToAdd

q5 = addSetCValue(setA)
print(q5)

#int as a parameter and int as a return type
def add(x,y):
    return x + y
print(add(12,8))

#float as a parameter and float as a return type
def sub(x,y):
    return x - y
print(sub(23.5,22.1))

#boolean as a parameter and boolean as a return type
def canDrive(age,vehicleA):
    if age >= 18 and vehicleA:
        return True
    else:
        return False
print(canDrive(21,True))

#function as a return type
def add(x,y):
    return x + y
q1 = add(12,3)
print(q1)

add = lambda x,y:x+y
print(add)
q2 = add(23,4)
print(q2)

#function as a parameter
sub = lambda x,y:x-y
def subtraction(fn,x,y):
    # fn = lambda x,y:x-y
    q3 = fn(x,y)
    return q3

q4 = subtraction(sub,10,5)
print(q4)
