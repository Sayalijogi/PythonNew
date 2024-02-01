#Class of Prathamesh Sir
#a=['ramesh',23,25,'pune']
#constructor wise
student={
    'name':'ramesh',
    'age':'12',
    'area':'pune',
    'subjects':['phy','maths','chem']
}

#retrieve
print(student)
name=student['name']
print(name)
print(student['subjects'][1])

#setting the value
student['favcolor']='red'

print(student)

#update
student['favcolor']='white'
print(student)

del student['area']
print(student)

#using list

dict1=dict(a=1,b=2,c=3)
print(dict1)

print(type(dict1))

#through tuple pair
q=dict([('a',1),('b',2),('c',3)])
print(q)

w=dict([('name','rohit'),('roll','23')])
print(w)

w['roll']=49
print(w)

#methods --->
#1. copy() creates a duplicate copy of a dictionary

w=dict([('name','rohit'),('roll',23)])
print('-------------------------------------------------------------------')

r=w.copy()
print(r)

print(id(r),id(w))

r['name']='soham'
print(r,w)

#2 get(key,message).It will give the value of that key,returns a value

q=dict([('a',1),('b',2),('c',3)])
print(q.get('a'))
print(q.get('c'))
print(q.get('e','key does not exist'))

#3.keys() return

q=dict([('a',1),('b',2),('c',3)])
print(q.keys())
print(type(q.keys()))

#