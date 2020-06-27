# - Define a function
# - Call (invocation) that function
# - Can be called multiple times

# Defining a function
# def greet():
#     print("Hello, mate!")
#     print("How are you today?")


# Call to the fn
# greet()

# Write a function asking the name of the visitor and return the value to the caller

def visitor_name(name):
    return "Hey, you are :"+name

print(visitor_name("Josh"))











def visitor_name():
    name = input("What's your name??")
    print(name)
    greet()

# visitor_name()

# parameters to the function

def greet(name, age = 0):
    print(f"Hello, {name}, your age is", age)
    print("Your age is ", age)
    if age == 0:
        print("Well, you are uptight with your privacy!")

# name = input("What's your name??")
# greet("Grace")

# Write a function to calculate area of a circle
# Call the function with radius as 10 and 25 cm

import math

def area_circle(radius):
    area =  math.pi * radius ** 2
    return area


# RETURNING A VALUE
# name = input("What is your name?")
my_area = area_circle(10)
print(my_area)


# Write a function that expects a firstname and lastname.
# Return the the full name

# Call that function with your first and last names

def full_name(firstname, lastname, age):
    fullname = firstname+" "+lastname + ", and you are "+str(age)+" years old!"
    return fullname

fname = full_name("Madhusudhan", "Konda", 36)

fname = full_name(age=36, lastname="Konda", firstname="Madhusudhan")


print(fname)
