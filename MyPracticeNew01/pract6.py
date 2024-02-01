# loops
#
# for x in range(startValue,EndValue(not included),stepSize):
#       #statements
#
# program 1
# print 0 to 5
for x in range(6):
    print(x)

# print "hello" 3 times
for x in range(3):
    print("hello")
    # print(x)

# print 1 to 5
for x in range(1,6):
    print(x)

# print 5 to 1
for x in range(5,0,-1):
    print(x)

#print table of 5 in reverse
for x in range(50,0,-5):
    print(x)

#print table of 2
# 2 ,4 , 6 , 8 , 10, 12, 14 ,16 , 20
for x in range(2,22,2):
    print(x)

#break statement with for loop
for item in range(1,5):
    if item == 3:
        break
    print(item) #1 #2

for item in range(1,5):
    print(item)
    if item == 3:
        break  # 1 # 2 # 3

for item in range(5,55,5):
    if item == 45:
        break
    print(item)

for item in range(50,0,-5):
    if item == 45:
        break
    print(item)

#continue with for
for x in range(1,6):
    if(x == 3):
     continue
    print(x)   #1 #2 #4 #5

for x in range(20,0,-2):
    if x == 10:
        continue
    print(x)

