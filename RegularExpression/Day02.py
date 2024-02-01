import re
# program
q1 = "an apple a day keeps doctor away"
r = re.findall(r'\ba[\w]*',q1)
print(r)

# program 2
q2 = "an apple a ay keeps doctor away"
r = re.findall(r'\ba[\w]*',q1)
print(r)


# program 3
str = "The meeting will be conducted on 21st and 1st  31st of every month"
q3 = re.findall(r'\d[\w]*',str)
print(q3)

str = "The meeting will be conducted on 21st and 1st  31st of every month"
q4 = re.findall(r'\d\d[\w]*',str)
print(q4)


# program 4
str2 = "one two three 4 5 6 7 8 nine ten 7777 88888 99999"
q5 = re.findall(r'\d[\d]*',str2)
print(q5)


# program 5
str2 = "one two three 4 5 6 7 8 nine ten 7777 88888 99999 five four seven"
q6 = re.findall(r'\b\w\w\w\b',str2)
q7 = re.findall(r'\b\w{3}\b',str2)
q8 = re.findall(r'\b\w{4,}\b',str2)
q9 = re.findall(r'\b\w{4,5}\b',str2)
print(q6)
print(q7)
print(q8)
print(q9)

