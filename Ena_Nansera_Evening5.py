import os

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists


# Checking if a File Exists
file_path = "ena.txt"
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")


# Reading the Entire File Content


f = open("ena.txt", "a")
# Write some text to the file
f.write("This is some more text")
f.close()
print("Text appended to the file successfully.")

#  Opening a file in write mode
f = open("ena.txt", "w")
f.write("This is some new text")
f.close()
print("Text written to the file successfully.")


# trying to access the written cotent onto the file


file_path = "ena.txt"
# Open the file in append mode
with open(file_path, "a") as f:
    # Write some text to the file
    f.write("This is some more text")
# Read the appended content
with open(file_path, "r") as f:
    content = f.read()
    print(content)

# By looping through the lines of the file, you can read the whole file, line by line:

# Example
# Loop through the file line by line

f = open("ena.txt", "r")
for x in f:
    print(x)


# Open the file "demofile3.txt" and overwrite the content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())




# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function

import os
os.remove("demofile.txt")

# Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") # THE TRY, EXCEPT AND FINALLY BLOCKS IN PYTHON
"""

try: The try block is used to enclose the code that might raise an exception. 
It allows you to test a block of code for exceptions.

except: The except block is used to handle specific exceptions that
 may occur within the try block. It allows you to define the actions to be 
 taken when a particular exception is raised.

finally: The finally block is used to define a piece of code that will be 
executed regardless of whether an exception occurred or not. It allows you 
to specify cleanup or resource release operations that should always be performed.
"""


def main():
    try:
        x = int(input())
        y = int(input())
        z = int(input())
        print(x + y + z)
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except Exception as e:
        print(e)
    finally:
        print("Finally")

        # EXMAPLES


def validate_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            raise ValueError("You must be at least 18 years old.")
        else:
            print("Age validation successful.")
    except ValueError as e:
        print("Invalid age:", str(e))


# calling the method defined above
validate_age("25")  # Age validation successful.
validate_age("-5")  # Invalid age: Age cannot be negative.
validate_age("15")  # Invalid age: You must be at least 18 years old.


def login(username, password):
    try:
        # Simulating authentication logic
        if username == "admin" and password == "password":
            print("Login successful.")
        else:
            raise ValueError("Invalid username or password.")
    except ValueError as e:
        print("Login failed:", str(e))
        
# calling the method defined above
login("admin", "password")    # Login successful.
login("guest", "123456")      # Login failed: Invalid username or password.
login("admin", "wrongpass")   # Login failed: Invalid username or password.


# User-defined exceptions are created to force certain constraints on the values of the variables.
# To create a User-defined Exception, we have to create a class that implements the Exception class.


# Base class
class PercentageError(Exception):
    pass

# Exception class for percentage > 100


class InvalidPercentageError(PercentageError):
    def init(self):
        super().init("Percentage is invalid")

# Exception class for percentage < 80


class LessPercentageError(PercentageError):
    def init(self):
        super().init("The Percentage is lesser than the Cut-off, Please try again!")

# class to check percentage range


class checkPercentage(PercentageError):
    def init(self, per):
        if per < 80:
            raise LessPercentageError
        if per > 100:
            raise InvalidPercentageError
        print("Congrats you're Enrolled")


# different cases and output for the defined method
try:
    print("For Percenatge: 93")
    checkPercentage(93)
except Exception as e:
    print(e)

try:
    print("\nFor Percenatge: 102")
    checkPercentage(102)
except Exception as e:
    print(e)

try:
    print("\nFor Percenatge: 58")
    checkPercentage(58)
except Exception as e:
    print(e)
