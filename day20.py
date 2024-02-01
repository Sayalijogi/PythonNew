setA = {11,22,33}
setB = set([11,22,33])
setC = set()
for item in setB:
    print(item)

#remove()
setA = {11,22,33,44}
setA.remove(11)
print(setA)

#discard()
setA.discard(22)
print(setA)

#pop()
setA.pop()
print(setA)

setName = {"chinmay","sarika","ashu","satish","mayuri"}
setNameB = setName.copy()
setName.pop()
print(setNameB)
print(setName)

#add()
setCities = {"pune","mumbai","banglore","chennai"}
setCities.add("wardha")
print(setCities)

#clear()
setCities.clear()
print(setCities)

#union()
setA = {"chinmay","sarika","ram"}
setB = {"komal","abhisha","shraddha"}
setD = setA.union(setB)
print(setD)

#intersection  #intersection_update
setD = {"chinmay","sarika","ram"}
setE = {"komal","abhisha","ram"}
setF = setD.intersection(setE)
print(setF)

setD.intersection_update(setE)
print(setD)

#difference  #difference_update
set1 = {"chinmay","sarika","ram"}
set2 = {"komal","abhisha","ram"}

set3 =set1.difference(set2)
print(set3)

set2.difference_update(set1)
print(set2)

#symmetric_difference #symmetric_difference_update
set11 = {"chinmay","sarika","ram"}
set12 = {"komal","abhisha","ram"}

set13 =set11.symmetric_difference(set12)
print(set13)

set11.symmetric_difference_update(set12)
print(set11)

#isdisjoint()
setR = {"chinmay","sarika","ram"}
setS = {"komal","abhisha","ram"}
q = setR.isdisjoint(setS)
print(q)

#issuperset() #issubset()
setM = {11,22,33}
setN = {22,33}
q2 = setM.issuperset(setN)
print(q2)
q3 = setN.issubset(setM)
print(q3)

#update
setNames = {"chinmay","sarika"}
setNames.update(["ashu","sayali"])
print(setNames)

setX = {11,22,33}
# setY = setX
# setY.update({44,55})
# print(setX)
# print(setY)

setY =setX.copy()
setY.update({33,44})
print(setY)
print(setX)

