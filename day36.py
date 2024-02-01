#program 1
class Dog:
    def talk(self):
        print("bow bow")

class Cat:
    def talk(self):
        print("meow meow")

def call_talk(obj):
    obj.talk()

a = Dog()
b= Cat()
call_talk(a)
call_talk(b)

dog = Dog()
dog.talk()
cat =Cat()
cat.talk()

#program 2
class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hello hii")

class Cat:
    def meow(self):
        print("meow meow")
class Person:
    def greet(self):
        print('hello!!')

def call_talk(obj):
    if(hasattr(obj,"talk")):
        obj.talk()
    elif(hasattr(obj,"meow")):
        obj.meow()
    else:
        print("wrong object pass")

# a1 = Duck()
# call_talk(a1)
# a2 = Human()
# call_talk(a2)
# a3 = Cat()
# call_talk(a3)
a4 = Person()
call_talk(a4)







