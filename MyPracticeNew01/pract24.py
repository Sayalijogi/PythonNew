g = {11,22,33,44,55,66,77,88,77}
print(type(g))

g = {11,22,33,44,55,66,77,88,77}
print(type(g))

#set stores the value by index ??
# print(g[0])
# print(g)

#string,list,tuple,dictionary,set
#len()
#del()
#looping over set
for item in g:
    print(item)

#len of set
print(len(g))

#adding element to set
setB = {'amol','satish','ram','sham'}
setB.add('sarika')
print(setB)

#update the vslue of set
setB.update({"ramesh","suresh"})
print(setB)

#deleting set value
setB.remove('ramesh')
print(setB)

setC = {11,22,33,44}
setC.add(55)
setC.update({66,77,88})
setC.remove(66)
print(setC)

setD = {"pune","mumbai","banglore","kolkata"}
setD.pop()
print(setD)

setD.clear()
print(setD)

setE = {11,22,33}
setF = setE
setF.add(44)
print(setE)
print(setF)

setE = {11,22,33}
setF = setE.copy()
setF.add(44)
print(setE)
print(setF)


