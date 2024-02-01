# String
#------ methods ------
#program 1
first_name = "chinmay"
print(type(first_name))
fn = first_name.upper()
print(fn)

#program 2
lastName = "Deshpande"
ln = lastName.lower()
print(ln)

#Slicing
city = "chandrapur"
#0   1   2  3  4  5  6  7  8  9
#c   h   a  n  d  r  a  p  u  r
#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#city[startIndex:endIndex:steps]
print(city[1:])
print(city[3:9])
print(city[3:-2])
print(city[-7:7])
print(city[:7])
print(city[:-7])
print(city[-10:-7])
print(city[-1:-3])
# 0  1  2  3  4  5  6  7  8  9
# c  h  a  n   d  r  a  p  u  r
#-10 -9 -8 -7 - 6 -5 -4 -3 -2 -1
print(city[0:9:1])
print(city[::-1])

#program 4
city2 = "apple"
q1 = city2.count("p")
print(q1)

city3 = "chandrapur"
q2 = city3.count("a",4)
print(q2)

city4 ="chandrapura"
q3 = city4.count("a",4,8)
print(q3)

#program 5
city5 = "wardha"
q4 = city5.capitalize()
print(q4)

#program 6
info = "chinmay deshpande 7709192441"
email = "chinmaydeshpande@gmail.com"
#["chinmay","deshpande","7709192441"]
q5 = info.split("a")
print(q5)
q6 = email.split("@")
print(q6)
username = q6[0]
print(username)

#program 7
str1 = "chinmay"
str2 = "deshpande"
print(str1 + str2)

#program 8
name = "chinmay deshpande"
age = 34
#My name is chinmay deshpande and age is 34
uinfo = "My name is {} and age is {}".format(name,age)
print(uinfo)
#alternative method
print(f"My name is {name} and age is {age}")

#program 9
info2 = "i am learning javascript"
info3 = info2.replace("javascript","python")
print(info3)

#program 10
fruit = "apple"
info4 = fruit.startswith("a")
info5 = fruit.startswith("App")
print(info4)
print(info5)

#program 11
fruit = "papaya"
info6 = fruit.endswith("ya")
info7 = fruit.endswith("a")
print(info6)
print(info7)

#program 12
city = " goa "
# print(len(city))
# print(len(city.strip()))

info8 = city.lstrip()
x = len(info8)
print(x)

info9 = city2.rstrip()
x = len(info9)
print(x)

#program 13
#                0   1  2  3
city = "pune"   # p  u  n  e
print(city.index("n"))
print(city.index("p"))

#program 14
listA = [11,22,33,44,55,66]
listA[0] = 111
print(listA)

# h = "Hello"
#h[0] = "H"

#program 15
info9 = "chinmay".isalpha()
print(info9)
info10 = "12414344345".isdigit()
print(info10)

print("32423@".isalnum())

