print(1)
print(2)
print(3)
print(4)
print(5)

#for loop
#range(startIndex, endIndex(not included) ,Steps)

for x in range(10):  #by default startIndex is zero
    print(x)

for x in range(1,10):
    print(x)

for x in range(1,10,1):
    print(x)

#  2  4  6  8  10  12  14  16  18 20
for x in range(2,21,2):
    print(x)

# 5 table in reverse
for x in range(50,0,-5):
    print(x)

# 3 table in reverse
for x in range(30,0,-3):
    print(x)

#break
for x in range(1,9):
    if x == 5:
        break
    print(x) # 1 2 3 4

for x in range(1,9):
    print(x)  # 1 2 3 4 5
    if x == 5:
        break

for x in range(2,21,2):
    print(x)   # 2 4 6 8 10
    if x == 10:
        break

for x in range(50,5,-10):
    print(x)  # 50 40 30 20
    if x == 20:
        break

#continue
for x in range(1,10):
    if x == 3:
        continue
    print(x)  # 1 2 4 5 6 7 8 9

for x in range(1,10,2):
    if x == 3:
        continue
    print(x) # 1 5 7 9

for x in range(50,10,-20):
    if x == 30:
        continue
    print(x) # 50

#while loop