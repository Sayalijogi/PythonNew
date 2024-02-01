#compile time error
#program 1

# def addA()
#     print(9 +9)
# addA()

#program 2
#
# def addC():
# print(8+9)  #indentation error
# addC()

# #program 3
# #run time error
# print("hello")
# q1 = int(input('Enter the number one'))
# q2 = int(input('Enter the number two'))
# print(q1/q2)
# print("bye")

# #program 4
# #         0  1  2  3
# listA = [11,22,33,44]   # index error out of range
# print(listA[5])

# #program 5     #logical error -- in this we have to find the error by own
# salary = 15000
# def incrementedSal(salary):
#     return salary * 0.10
# sal = incrementedSal(salary)
# print(sal)

#program 6
#Run time error:
#exceptions

# #program 7
# print("hello")
# try:
#     q1=int(input("Enter the number A"))
#     q2=int(input("Enter the number B"))
#     print(q1/q2)
# except Exception as e:
#     print(e)
# print("bye")

#program 8
print("hello")
try:
    listB = [11,22,33]
    print(listB[3])
except Exception as e:
    print(e)
print("bye")

#program 9
print("hello")
try:
    q1 = int(input("Enter the number A"))
    q2 = int(input("Enter the number B"))
    print(q1/q2)
    listC = [11,22,33]
    print(listC[2])
    print(q3)
except ArithmeticError:
    print("input is not correct")
except IndexError:
    print("No many element present")
except Exception:
    print("not identified")

#try ----except----else----finally
#user defined exception
#assert error

#logical error


