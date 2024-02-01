#Program 1
def add(x,y):
    return x + y
q1 = add(12,4)
print(q1)

#Program 2
#lambda function
add = lambda x,y:x+y
q2 = add(13,4)
print(q2)

#Program 3
sqr = lambda x:x*x
e = sqr(3)
print(e)

#Program 4

def additionAll(*args):
    print(args)
    total = 0
    for i in args:
        total = total + i
    return total
#args return the
f = additionAll(11,22,33,44,55,66,77,88,99,100)
print(f)

#Program 5
def updateCity(**kwargs):
    print(kwargs)
    kwargs['city']="Nagpur"
    return kwargs
#kwargs return dictionary
f2 = updateCity(fullName = "sayali",city="pune",age = 22)
print(f2)

#Program 6
def addition(x = 4,y = 6):
    print(x+y)
addition()
addition(1,2)

#Program 7
def add(x3,x2,x1):
    print(x3+x2+x1)
    print(x3)
add(x1 = 2,x2 = 2,x3 = 2)
