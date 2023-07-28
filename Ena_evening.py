# Create a list with 5 items (names of people) and write a python program to output the 2nd item
people = ["ena", "Daisy","Tom", "Linda","Sarah"]
x = people[1]
print(x)
#  Write a python program to change the value of the first item to a new value
people = ["ena", "Daisy","Tom", "Linda","Sarah"]
people[2] = "Ruth"
print(people)

# Write a python program to add a sixth item to the list
people = ["ena", "Daisy","Tom", "Linda","Sarah"]
new_value = "Jane"
people.append(new_value)
print(people)

#Write a python program to add “Bathel” as the 3rd item in your 
people = ["ena", "Daisy","Tom", "Linda","Sarah"]
people[3] = "Bathel"
print(people)

# Write a python program to remove the 4th item from the list
people = ["ena", "Daisy","Tom", "Linda","Sarah"]
people.pop()

#  Use negative indexing to print the last item in your list
people = ["ena", "Daisy","Tom", "Linda","Sarah"]
last_item = people[-1]
print(last_item)

#Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
mylist = [1,2,3,4,5,6,7]
first_item = mylist[3]
second_item = mylist[4]
third_item = mylist[5]
print(first_item, second_item, third_item)

#Write a list of countries and make a copy of it.
countries = ["Uganda","Kenya", "Rwanda","Tanzania"]
new_copy = countries.copy()
print(new_copy)

# Write a python program to loop through the list of countries
countries = ["Uganda","Kenya", "Rwanda","Tanzania"]
for country in countries:
    print(country)

    #Write a list of animal names and sort them in both descending and ascending order.
    animals = ["dog","cat","pig","goat"]
    ascending = sorted(animals)
    descending = sorted(animals,reverse=True)
    print(ascending)
    print(descending)

#Using the list above, write a python program to output only animal names with the letter ‘a’ in them
animals = ["dog","cat","pig","goat"]
for animal in animals :
    if 'a' in animals:
        print(animals)



    # Write two lists, one containing your first names and the other your second names. Join the two lists.
    first_names = ["John", "Ena", "Michael", "Ola"]
second_names = ["Smith", "Josephine", "Kintu", "Brown"]

# Joining the two lists
full_names = []
for first, second in zip(first_names, second_names):
    full_names.append(f"{first} {second}")

print(full_names)

#QUESTION 2 Consider the tuple below;x = (“samsung”, “iphone”, “tecno”, “redmi”) Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = "samsung"

# Outputting the favorite phone brand
if favorite_brand in x:
    print(favorite_brand)
else:
    print("Favorite brand not found in the tuple.")
#Use negative indexing to print the 2nd last item in your tuple. 
x = ("samsung", "iphone", "tecno", "redmi")

second_last_item = x[-2]

print(second_last_item)

#Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")

# Convert the tuple to a list
x_list = list(x)

# Update "iphone" to "itel" in the list
index_to_update = x_list.index("iphone")
x_list[index_to_update] = "itel"

# Convert the list back to a tuple
x_updated = tuple(x_list)

print(x_updated)

#Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")

# Create a new tuple by concatenating with a tuple containing "Huawei"
x_updated = x + ("Huawei",)

print(x_updated)


#Write a python program to loop through the tuple above
x = ("samsung", "iphone", "tecno", "redmi")

# Convert the tuple to a list
x_list = list(x)

# Remove the first item from the list
x_list.pop(0)

# Convert the list back to a tuple
x_updated = tuple(x_list)

print(x_updated)

# Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])

print(cities)

#  Write a python program to unpack your tuple.
x = ("Kampala", "Entebbe", "Jinja", "Gulu")

# Unpacking the tuple
item1, item2, item3, item4 = x

print(item1)
print(item2)
print(item3)
print(item4)

# Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")

# Printing the 2nd, 3rd, and 4th cities using a range of indexes
for index in range(1, 4):
    print(cities[index])

#. Write two tuples, one containing your first names and the other your second names. Join the two tuples
first_names = ("John", "Ena", "Michael", "Ola")
second_names = ("Ssentongo", "Nansera", "Kintu", "Otto")

# Joining the two tuples
full_names = first_names + second_names

print(full_names)

#. Create a tuple of colors and multiply it by 3.
colors = ("white", "black", "pink")

# Multiplying the tuple by 3
result = colors * 3

print(result)



#Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

count_8 = thistuple.count(8)

print(count_8)


# QUESTION 3(SETS)
#  Use the set() constructor to create a set of 3 of your favorite beverages.
favorite_beverages = set(["coffee", "tea", "juice"])

print(favorite_beverages)

#Use the correct method to add 2 more items to the beverages set.
favorite_beverages = {"coffee", "tea", "juice"}

# Using the update() method to add multiple items
favorite_beverages.update(["water", "smoothie"])

print(favorite_beverages)

#  Given the set below; mySet = {“oven”, “kettle”, “microwave”, “refrigerator”} Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")


# Write a python program to remove “kettle” from the set above.
mySet = {"oven", "kettle", "microwave", "refrigerator"}

mySet.remove("kettle")

print(mySet)

# Write a python program to loop through the set above.
mySet = {"oven", "kettle", "microwave", "refrigerator"}

# Looping through the set
for item in mySet:
    print(item)

#  Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set
mySet = {"apple", "banana", "orange", "grape"}
myList = ["mango", "pineapple"]

# Adding elements from the list to the set
mySet.update(myList)

print(mySet)

# Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {25, 30, 35, 40}
first_names = {"Teddy", "Ena", "Dianah", "Cloeh"}

# Joining the two sets
combined_set = ages.union(first_names)

print(combined_set)



# QUESTION 4 (STRINGS)
# Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
x = 20
age = " years old"

concatenated_string = str(x) + age

print(concatenated_string)

#Consider the example below; txt = “ Hello, Uganda! ” Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "

# Removing spaces at the beginning, in the middle, and at the end
txt = txt.strip()

print(txt)

# Write a python program to convert the value of ‘txt’ to uppercase.
txt = "Hello, Uganda!"

# Converting the value of 'txt' to uppercase
txt = txt.upper()

print(txt)

#Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = "Hello, Uganda!"

# Replacing 'U' with 'V' in the string
txt = txt.replace('U', 'V')

print(txt)

# Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position. y = “I am proudly Ugandan”
y = "I am proudly Ugandan"

# Extracting characters in the 2nd, 3rd, and 4th positions
range = y[1:4]

print(range)

# The piece of code below will give an error when output; x = “All “Data Scientists” are cool!”  Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
# or
# x = "All \"Data Scientists\" are cool!"

print(x)




#QUESTION4 (DICTIONARIES)
# With reference to the dictionary below, write a python program to print the value of the shoe size. Add this dictionary to your .py file Shoes = { “brand” : “Nick”, “color” : “black”,“size” : 40}
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Printing the value of the shoe size
shoe_size = Shoes["size"]
print(shoe_size)

#  Write a python program to change the value “Nick” to “Adidas”

# Changing the value from "Nick" to "Adidas"
Shoes["brand"] = "Adidas"

# Printing the updated dictionary
print(Shoes)

#Write a python program to add a key/value pair "type”: "sneakers" to the dictionary.

Shoes["type"] = "sneakers"

# Printing the updated dictionary
print(Shoes)


# Write a python program to return a list of all the keys in the dictionary above.

keys_list = list(Shoes.keys())

# Printing the list of keys
print(keys_list)
#Write a python program to return a list of all the values in the dictionary above.

values_list = list(Shoes.values())

# Printing the list of values
print(values_list)

# Write a python program to loop through the dictionary above.

for key in Shoes:
    value = Shoes[key]
    print(key, ":", value)


# Write a python program to remove “color” from the dictionary.

# Removing the key "color" from the dictionary
del Shoes["color"]

# Printing the updated dictionary
print(Shoes)

# Write a python program to empty the dictionary above.

# Clearing the dictionary
Shoes.clear()

# Printing the updated dictionary
print(Shoes)

# Write a dictionary of your choice and make a copy of it.
# Original dictionary
original_dict = {
    "name": "Ena",
    "age": 20,
    "Course": "BSSE"
}

# Making a copy of the dictionary
copied_dict = dict(original_dict)

# Modifying the copied dictionary
copied_dict["age"] = 25

# Printing both dictionaries
print("Original dictionary:", original_dict)
print("Copied dictionary:", copied_dict)


#  Write a python program to show nested dictionaries.
# Nested dictionaries
student1 = {
    "name": "Ena",
    "age": 20,
    "grades": {
        "math": 95,
        "science": 90,
        "english": 80
    }
}

student2 = {
    "name": "Linda",
    "age": 19,
    "grades": {
        "math": 75,
        "science": 90,
        "english": 80
    }
}

# Accessing nested dictionary values
print("Student 1:")
print("Name:", student1["name"])
print("Age:", student1["age"])
print("Grades:")
print("Math:", student1["grades"]["math"])
print("Science:", student1["grades"]["science"])
print("English:", student1["grades"]["english"])
print()

print("Student 2:")
print("Name:", student2["name"])
print("Age:", student2["age"])
print("Grades:")
print("Math:", student2["grades"]["math"])
print("Science:", student2["grades"]["science"])
print("English:", student2["grades"]["english"])














