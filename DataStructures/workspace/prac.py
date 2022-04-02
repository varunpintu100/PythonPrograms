"""students_list={"varun":20,"vedhanth":15,"vinnu":40}
for i,j in students_list.items():
    print("name :", i,"--->price :",j)  #[This is the program to get the values and keys in dictonary]"""
    
#LAMBDA FUNCTION
 
"""-- lambda contains four parts 1.lambda key word 2.parameters 3.colon 4.return values --"""

"""add = lambda x,y:x+y 
print(add(2,3))

(lambda x,y:x+y)(2,3) #this is extremely confusing so most people dont use that """

#MAP USAGE

"""def double(x):
    return x*2

li=[1,2,3,4,5,6,7]
doub=map(double,li)    # this is used to map the function with each object in the list 
print(list(doub)) #map function doesnt return a list but it returns a map object """

#LAMBDA and MAP usage

"""sequence = [1,3,5,9]
double = list(map(lambda x:x*2,sequence))  #lambda's are functions without names
print(double)"""


# DICTONARY COMPREHENSION
"""
users=[
    (0,"bob","password"),
    (1,"rolf","rolf123"),
    (2,"Jose","Jose12"),
    (3,"username","1234")]

username_mapping = {user[1]:user for user in users} # here the names get mapped to the each tuple 

print(username_mapping["bob"]) # we can access using the key rather than index in dict

print(username_mapping)

username_input=input("enter username : ")
password_input=input("enter password : ")

_,username,password = username_mapping[username_input]  # this can we used to map the parameters for the related tuple

if username!=username_input: # this checks the username and userinput if both are same 
    print("user name incorrect")
    
if password==password_input: # this checks the password and the password input are both the same 
    print("You have sucessfully logged in ")
    
elif password!=password_input:
    print("the password you have entered is wrong")"""


#collecting multiple parameters 

"""
def multiply(*args):  # args is used to collect arguments
    total=1
    for arg in args:  # this gives us each of the arguments that are passed from function 
        total = total*arg
    return total


print(multiply(1,2,3))
     """

# using args in various ways 
"""
def add(x,y):
    return x+y

nums=[3,5] 
print(add(*nums)) #that assigns the parametes based on the position and in this way need to pass same number of arguments required as parameters

nums1={"x":5,"y":50}
print(add(**nums1)) #this can be used if the parameters we take and the parameters in the dictioary are ex: if we put a in place of x we get an error


"""


#ARGS USAGE IN SOMEOTHER FORMAT
"""
def multiply(*args):
    total =1
    for arg in args:
        total=arg*total
    return total
def apply(*nums,operator):
    if operator=="*":
        return multiply(*nums)
    elif operator=="+":
        return sum(nums)
    else:
        return "No valid operator to apply()"
    
    
print(apply(1,2,3,operator="*"))

"""

#unpacking of keyword(ARGS vs KWARGS)
'''
def named(**kwargs): #dictionary unpacking and returns a dictionary collects keyword arguments and put into a dictionary
    print(kwargs) #dict key-name is name of the keyword and the value is the thing passed into with the name
named(name="bob",age=25)

def named1(name,age):
    print(f"the name of the person is : {name}")
    print(f"the age of the person is : {age}")

temp={"name":"varun","age": 23}

named1(**temp)

def named2(**kwargs):#packing into dictonary
    print(kwargs)#unpacking into dictionary
    
temp1={"name":"varun","age":25}
named2(**temp)'''

#ARGS AND KWARGS
'''
def both(*args,**kwargs):
    print(args)
    print(kwargs)

both(1,2,3,4,5,6,7,8, name="varun",age=25,color="white")
'''

#Object Oriented Programming 

'''
class Student: #--> function inside of a class is called as method
    def __init__(self,name,grades): #--> Magic method 
        self.name= name
        self.grades = grades
        
    def average(self):
        return sum(self.grades)/len(self.grades)
    
student = Student('varun',(100,100,93,78,90))
student1 = Student('Rolf',(90,90,93,78,90))
print(Student.average(student)) #--> base class we can access a function by passing the class instance created
print(Student.average(student1)) 
'''
#__str__ and __repr__ methods
''' 
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Student name : {self.name}\nStudent age : {self.age}"
    
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
person=Person("varun",25)
print(person)
'''

#class method and static method

'''
class ClassTest:
    def isntance_method(self):
        print(f"Called instance_method of {self}")
        
    @classmethod
    def class_method(cls):
         print(f"Called class_method of {cls}")
         
    @staticmethod
    def static_method():
        print("Called the static method.")
        
ClassTest.class_method()
ClassTest.static_method()

'''
#class method and static method
'''
class Book:
    Types = ("handcover","paperbook")
    
    def __init__(self,name,book_type,weight):
        self.name=name
        self.book_type=book_type
        self.weight = weight
        
    def __str__(self):
        return f"<Book : {self.name}, {self.book_type}, weight: {self.weight}grams>"
    
    @classmethod  #-->we use class method just to take the entire class input 
    def hardcover(cls,name,page_weight):
        return cls(name,cls.Types[0],page_weight+100)
    
    @classmethod  #-->we use class method just to take the entire class input 
    def paperbook(cls,name,cls.Types[1],page_weight):
    
        return cls(name,cls.Types[1],page_weight+100)
book =Book.hardcover("harry porter", 100)
book1 = Book.paperbook("Marvel", 120)
print(book)
print(book1)
'''

#inheritance
'''
class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True  
    
    def __str__(self):
        return f"Device {self.name!r} --> ({self.connected_by})"    #--> !r is used for calling the repr method of self.name and comes in quotes
    
    def disconnect(self):
        self.connected=False
        print(f"Device {self.name} Disconnected !!!")

printer = Device("Printer","Usb")
print(printer)
printer.disconnect()

class Printer(Device):
    def __init__(self,name,connected_by,capacity):
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.remaining_Pages = capacity 
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_Pages} pages Remaining)"  #--> we use super to call the methods frpm the parent class
    
    def Print(self,pages):
        if not self.connected:
            print("Device Not connected !!!Please Connect")
        else:
            print(f"Printing {pages} pages.")
            self.remaining_Pages -= pages   
        
printer1 = Printer("Printer","USB",500)
printer1.Print(20)
print(printer1)
printer1.disconnect()
printer1.Print(30)
'''
#type hinting 
"""
from typing import List

def List_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)
"""

#importing
import sys

print(sys.path)
print(sys.modules)



