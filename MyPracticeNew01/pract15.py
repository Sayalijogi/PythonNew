#Rahul Sir Class
#Program 1
# list comprehension
#printing the elements from the list

list_fruits = ['apple','banana','mango']

for i in list_fruits:
    print(i)

#using list comprehension
ans = [i for i in list_fruits]
print(ans)

#printing the square of each elements from the list
list_num = [1,2,3,4,5,6]

for i in list_num:
    print(i*i)

#using list comprehension
value = [i*i for i in list_num]
print(value)

#printing the square of odd elemnts from the list
for i in list_num:
    if i % 2 != 0:
        print(i * i)

#using list comprehension
sai = [i*i for i in list_num if i%2 != 0]
print(sai)

#print the elements of the list ,but in upper case

list_fruits = ["apple","banana","mango"]
for i in list_fruits:
    print(i.upper())

#using list comprehension
ans = [i.upper() for i in list_fruits if len(i) > 5]
print(ans)

#print the age of each member
birth_year = [1990,1991,1992,1993]

for age in birth_year:
    print(2023 - age)

#using list comprehension
ans = [(2023-age) for age in birth_year]
print(ans)


