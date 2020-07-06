def friends(*names):
    print(names)
    for name in names:
        print(name)


# Variable arguments
# friends("Bob","Elisa","John", "Tim","Grace","Ram","Charan","Grace","Ram","Charan","Grace","Ram","Charan")

friends(32, "Bob",12, True, 1.1,39)
friends(34, "Freeda",14, False, 1.2, 29)

# Write a function which has the following requirements:
# - takes in name of the person;
# - expects a four or more characteristics about him/her

# Call it with your best friend's name and his/her characteristics

def charecteristics(name, *chars):
    print(name, chars)

charecteristics("John", "Sleeping", "Reading")

def furniture(items):
    for item in items:
        print(item)

items = ["Table","Basket","Lamp"]
furniture(items)

# Write a function that iterates through list of animals

def animals(animals):
    for animal in animals:
        print(animal)

animals = ["Monkeys","Elephants","Zebras"]
furniture(animals)






