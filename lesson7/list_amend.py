def furniture(items):
    # add additional item "Chairs" here and return the new list

    items.insert(0,"Delivery Charge")
    return items

items = ["Table","Basket","Lamp"]
print(furniture(items))