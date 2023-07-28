# Casting
x = int(10)
y = float(3.5)
print(x)
print(y)

# python string
print("Good Evening")
print('Good Evening')

# Muti-line strings
y = """ Am offering BSSE year 3, Recess program in python,at Makerere"""
print (y)

# String concatination and formatting.
age = 20
# name
name = "My name is Nansera and I am {}"
print (name.format(age))
# Example 2 of formatting.
quantity = 10
item = "phones"
price = "$1000"

myitem = "I order for {1}, of quantity {0}, at a price of {2}  "
print (myitem.format(quantity, item, price))

# BOOLEANS EXAMPLE.
print( 20 < 10)
print(10 ==20 )
print(30 > 20 )

v = "Nansera"
w = 20
print(bool(v))
print(bool(w))

#   EXAMPLE OF A DICTIONARY
# Dictinaries are used to store data in values and keys.They are ordered, cahangable and do not allow duplicates 
thisdict = {
  "name": "Nansera",
  "regno": "21/U/076",
  "year": 2023 
}
print(thisdict["name"])

# DUPLICATES IN DICTIONARY
thisdict = {
    "name": "nansera",
    "regno": "21/U/076",
    "year": 2023,
    "year": 2022
}
print(thisdict["year"])

# LENGTH OF THE DICTIONARY
print(len(thisdict))

# Finding the datatype
print(type(thisdict))
x = thisdict.get("regno")
print(x)


# DICTIONARY EXERCISE 1______ Using the values() method to return a list of all values in the dictionary.
# The values() return a view object which contains the values of the dictionary as a list.
thisdict = {
  "name": "Nansera",
  "regno": "21/U/076",
  "year": 2023 
}
y = thisdict.values()
print(y)

# EXERCISE 2----Check if a key exists in a dictionary.
mydict = {
    "fruit": "Orange",
    "colour": "yellow",
    "quantity": 2
}
if "fruit" in mydict:
    print("Exists")
else:
    print("Does not Exist")

    # EXERCISE 3: How to change and update a dictionary
    Fruit = {
        "name": "Mango",
        "colour": "Green",
        "quantity": 5
    }
    # Changing dictionary item
    Fruit["quantity"] = 10 
    print(Fruit)

    # Updating an item
    Myfruit = {
        "name": "Tomato",
        "colour": "Red",
        "quantity": 12
    }
    Myfruit.update({"quantity":30})
    print(Myfruit)

    # EXERCISE 4: How to add and remove an item from a dictonary
    # Removing an item.
    Myfruit = {
        "name": "Tomato",
        "colour": "Red",
        "quantity": 12
    }
    Myfruit.pop("colour")
    print(Myfruit)

# EXERCISE 5: Looping through a dictionary
    print(Myfruit)



