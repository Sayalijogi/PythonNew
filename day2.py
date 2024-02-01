x=10
print(x)
x=1000
print(x)

# +,-,*,/,% arithmetic operations

s=4
t=2

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)

def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
Calculator(12,4)

#function without parameter and without return type
def addA():
    print(9+9)

addA()
addA()
addA()
addA()

#function with parameter and without return type
def addB(x,y):
    print(x+y)
addB(6,3)
addB(16,4)
addB(20,5)

#function with parameter and with return type
#100 Given --- 100+100,100/5,100*0.10,100-50
#100 Shown --- no use

def addC(x,y):
    return x+y
q3 = addC(12,4)
print(q3)
print(q3+q3)
print(q3 * 0.10)
print(q3-5)

#Type
#Extrovert  #Introvert
#loud       #Calm
#outing     #less outing
#social     #less social

#Human ---amol
#property - height,weight,color,gender
#methods - talk(),walk(),sleep()

#Vehicle ---Car
#Property - color,model,regNo
#Methods - Start(),Stop()

#Bank -- ICICI Account
#property-bal,accNo.,accName,branchName,type
#Methods - withdrawl(),deposit()

x=10
print(x)
print(type(x))
#10,-10,0

x=0.19
print(x)
print(type(x))
#19.0,-19.9,0.0

x=True
print(x)
print(type(x))
#True or False

x="chinmay"
print(x)
print(type(x))
#"A","A12","asd@@","","@123414sdrere"

#comparison operator
#entity < entity ====>boolean===>
True or False
#<,>,<=,>=,!=,==
print(3==3) #True
print(3!=3) #False
print(3<4)  #True
print(3>4)  #False
print(3<=4) #True
print(3>=2) #True
print(3>=3) #True
print(3<=3) #True



