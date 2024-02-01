#Program 1
#             0     1    2    3
birthYear = [1989,1990,1991,1992]
ages = []
#[34,33,32,31]

for x in range(len(birthYear)):
    #print(x)
    #print(birthYear[x])
    #print(2023 - birthYear[x])
    x = 2023 - birthYear[x]
    ages.append(x)
print(ages)

#list comprehension
#          [expression: for loop :Conditions]
list_comp =[2023-item for item in birthYear]
print(list_comp)

#Program 2
marks = [34,55,66,7,2,44,55,66,99,77]
#[55,66,55,66,99,77]
above50 = []
for item in marks:
    #print(item)
    if item > 50:
        #print(item)
        above50.append(item)
print(above50)

#program 3

totals = [11,22,33]  # // 66
sum = 0
for item in totals:
    sum = sum + item
#    0    +   11  ==== 11
#    11   +    22  ===> 33
#    33    +   33   ===>66
print(sum)

# program 4

cities = ["pune","bangalore","kolkata"]
for item in cities:
    print("Welcome " + item)

