#program 1
setA = {11,22,33,44}
setA.pop()
print(setA)

#program 2
setA = {11,22,33,44}
setA.update([55,66,77])
setA.update((88,99,100))
setA.update({101,102,103})
print(setA)

#program 3
setC = {11,22,33}
setD = {22,33,44}
# In intersection it shows common values store in set
setE = setC.intersection(setD)
print(setE)

#program 4
setC = {11,22,33}
setD = {22,33,44}
setF = setC.union(setD)
#In union it keeps only one common value and give a combine set
print(setF)

#Program 5
setC = {11,22,33}
setD = {22,33,44}
setC.intersection_update(setD)
#In intersection update the intersection value such as common value given in set
print(setC)

#Program 6
setC = {11,22,33}
setD = {22,33,44}
#It shows difference in set which is different
print(setC.difference(setD))
print(setD.difference(setC))

#Program 7
setS = {11,22,33}
setR = {22,33,44}
setS.difference_update(setR)
#It gies difference update in set which set is different
print(setS)

#Program 8
setA = {11,22,33}
setB = {22,33,44}
#In symmetric difference it keeps duplicate value and shows Common value
setJ = setA.symmetric_difference(setB)
print(setJ)

setA.symmetric_difference_update(setB)
#In symmetric difference update it shows difference in given set
print(setA)

#Program 9
setX = {11,22}
setY = {11,22,33,44}
print(setX.issubset(setY)) #In subset it checks whesther values are store in both particular set or not
print(setY.issuperset(setX)) #In superset it checks wheather value in one set is present or not in another set

#Program 10
setI = {112,222}
setK = {11,22,33,44}
print(setI.isdisjoint(setK)) # In disjoint  returns True if none of the items are present in both sets, otherwise it returns False.

#Program 11
setG = {112,222}
setH = {11,22,33,44}

setG.remove(112)
print(setG)

print(setG.discard(112))

setCities = {"Pune","Mumbai","Banglore","Kolkata","Nagpur"}
print(setCities)
for item in setCities:
    print(item)

