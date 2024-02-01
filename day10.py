#str ---object--properties and methods
firstName ="chinmay"
print(firstName)
print(type(firstName))

#str stores the value by index
last_name="Deshpande"
# 0   1   2   3   4   5   6   7   8
# D   e   s   h   p   a   n   d   e
#-9  -8  -7  -6  -5  -4  -3  -2  -1

print(len(last_name))

#retrive
print(last_name[0])
print(last_name[-2])
#last_name[startIndex:EndIndex(not included):stepSize]
print(last_name[1:7])
print(last_name[3:6])
print(last_name[3:-1])
print(last_name[-8:7])
print(last_name[0:9:2])
print(last_name[:5]) #startIndex by default 0
print(last_name[1:]) #len(str) by default
print(last_name[-1:-6])

#loop through string

last_name="kulkarni"
#  0  1  2  3  4  5  6  7
#  k  u  l  k  a  r  n  i

for char in last_name:
    print(char)

for x in range(8):
    #print(x)
    print(last_name[x])

#are string mutable??
h ="hello"
#h[0]="p"
print(h)
h="bye"
print(h)




