#union()
setA = {1,2,3}
setB = {4,5,6}
setC = setA.union(setB)
print(setC)
print(type(setC))

#intersection()
setE = {11,22,33,44,55}
setF = {44,55,66,77,88,99,100}
setG = setE.intersection(setF)
print(setF)
print(setE)
print(setG)

#intersection_update()
setAA = {1,2,3,4}
setBB = {3,4,5,6}
setAA.intersection_update(setBB)
print(setAA)
setBB.intersection_update(setAA)
print(setBB)

#difference()
setAA = {1,2,3,4}
setBB = {3,4,5,6}
setEE = setAA.difference(setBB)
print(setEE)
setFF = setBB.difference(setAA)
print(setFF)

#difference_update()
setAA={1,2,3,4}
setBB={3,4,5,6}
setAA.difference_update(setBB)
print(setAA)
setBB.difference_update(setAA)
print(setBB)
print(setAA)

#issubset()
setQ = {11,22,33}
setS = {11,22}

q1=setS.issubset(setQ)
print(q1)
q2=setQ.issubset(setS)
print(q2)

#issuperset()
q3= setQ.issuperset(setS)
print(q3)

#symmetric_difference()
setQ = {11,111,33}
setS = {11,222222,44444,55}

setW=setQ.symmetric_difference(setS)
print(setW)

#symmetric_difference_update
setQ.symmetric_difference_update(setS)
print(setQ)
print(setS)

#isdisjoint()
q1=setQ.isdisjoint(setS)
print(q1)

set12 = {1,2,3}
set13 = {1,4,5,6}
q11 = set12.isdisjoint(set13)
print(q11)

set14 = {5,6,7}
set15 = {7,9,10}
q15 = set14.isdisjoint(set15)
print(q15)
