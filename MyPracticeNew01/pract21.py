#variables
#arithmetic
#conditional
#types
#comparison
#logical
#loops
#break and continue
#list
#list comprehension
#dictionary
#string

#string
x = "hello"
y = 'chinmay'
print(x)
print(y)
print('The quotes is "Try try but do not cry')
print(" This is chinmay's book  ")

a = """
    I am learning javascript and python
    I find them 90 % similar
    "hello"
    'bye'
"""
print(a)
b = '''
    I am learning python and javascript 
    I find them 90% similar
    "hello"
    'bye'
'''
print(b)
#learning
"""
    This is multiline comment
"""
#program 2
#string stores the value by index??
first_name = "chinmay"
print(first_name)
print(type(first_name))
print(first_name[0])

last_name = "deshpande"
#0  1  2  3  4  5  6  7  8
#d  e  s  h  p  a  n  d  e
#-9 -8 -7 -6 -5 -4 -3 -2 -1
print(last_name[0])
print(first_name[-1])

#for loop
#range
for i in range(len(last_name)):
    #print(i)
    print(last_name[i])

#without range
for char in first_name:
    print(char)

#while
i1 = 0
while(i1 < len(last_name)):
    #print(i1)
    print(last_name[i1])
    i1 = i1 + 1

