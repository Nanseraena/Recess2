# EXAMPLE 1: Calculate area and circumference of a circle.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = math.pi * self.radius**2
        return area
    
    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

# Create an instance of the Circle class
circle = Circle(8)

# Calculate and display the area and circumference
area = circle.calculate_area()
circumference = circle.calculate_circumference()

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)

#EXAMPLE 2: Calculate thye area and perimeter of  a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        area = self.length * self.width
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

# Create an instance of the Rectangle class
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)

# Calculate and display the area and perimeter
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)


# EXAMPLE 2:Convert a temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit:", fahrenheit)

#EXERCISE: Encapsulation with Employee information to give increamentation.
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary incremented successfully.")
        else:
            print("New salary should be greater than the current salary.")

            # Create an instance of the Employee class
employee = Employee("Nansera Ena", 1500000)

# Get the employee's name and salary
print("Name:", employee.get_name())
print("Salary:", employee.get_salary())

# Set a new salary
employee.set_salary(2000000)
print("New Salary:", employee.get_salary())

# Try to set a lower salary
employee.set_salary(1000000)
print("Updated Salary:", employee.get_salary())

