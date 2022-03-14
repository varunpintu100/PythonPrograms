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

def both(*args,**kwargs):
    print(args)
    print(kwargs)

both(1,2,3,4,5,6,7,8, name="varun",age=25,color="white")
