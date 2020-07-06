# Fruitful function or a Void function

def greet(name):
    print("Howdy, "+name)
    return name


my_greet = greet("Simon")
print(my_greet)

# Write a function that calculates and return the area of a rectangle given len and width
# and call it with 12, 13 as len and width

def area_rectangle(len, width):
    area = len * width
    return area

area = area_rectangle(12, 13)
print(area)


# Write a function for square of a number and call it with some samples


