#Rahul sir class
#Exceptional Handling
a = 100
b = 200
c = a/b
print(c)

# a = 100
# b = 0
# c = a/b  #ZeroDivisonError
# print(c)

# a = 100
# b = 200
# c = a/b
# print(c  #here we have to coorect the error manually

#Error : Syntax Error
#Exception : ZeroDivisonError

# https://docs.python.org/3.12/library/exceptions.html?highlight=exception#exception
#---------------------------------------------------
#using try.. except block
#try:
#   code prone to error
#except:
# msg if the exception occurs
#------------------------------------------------
try:
    a = 100
    b = 200
    c = a/b
    print(c)
except:
    print("Some error occured")
#-------------------------------------------------
a = 100
try:
    b = int(input("Enter a number other than zero"))
    c = a/b
    print(c)
except:
    print("Some error occured")
#-----------------------------------------------
name = "PRATIK"
print(name[3])
# print(name[9]) #index error
#------------------------------------------------
name = "PRATIK"
try:
    print(name[9])
except:
    print("Some error occured")
#-----------------------------------------------
#using exception class
name = "PRATIK"
try:
    print(name[9])
except Exception as e :
    print("Some error occured" ,e)
#------------------------------------------------
#how to work on multiple exceptions???
name = "PRATIK"
a = 100
try:
    print(name[3])
    b = int(input("Enter a number other than zero"))
    c = a/b
    print(c)
except Exception as e :
    print("Some error occured",e)
#--------------------------------------------------
name = "PRATIK"
a = 100
try:
    b = int(input("Enter a number other than zero:"))
    print(name[9])
    c = a/b
    print(c)
except Exception as e:
    print("Some error occured",e)
#------------------------------------------------
#handling each type of exception using their specific class
#so as to make the code better
name = "PRATIK"
a = 100
try:
    b = int(input("Enter a number other than zero:"))
    c = a/b
    print(c)
    print(name[9])
except ZeroDivisionError as e:
    print("Some error occured",e)
except IndexError as i:
    print("Some error occured",i)
