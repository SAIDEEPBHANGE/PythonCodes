# ==============================================
# Classes and Object-Oriented Programming (OOP) in Python
# ==============================================

# ----------------------------------------------
# What is a Class?
# ----------------------------------------------
# A class is a blueprint for creating objects.
# An object is an instance of a class.
# Classes encapsulate data (attributes) and behaviors (methods).

# ----------------------------------------------
# Defining a simple class
# ----------------------------------------------
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # The constructor method (__init__) initializes instance attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# ----------------------------------------------
# Creating objects (instances) of the class
# ----------------------------------------------
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.description())  # Output: Buddy is 3 years old.
print(dog2.speak("Woof Woof"))  # Output: Lucy says Woof Woof

# ----------------------------------------------
# Class vs Instance Attributes
# ----------------------------------------------
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

# Change class attribute for all instances
Dog.species = "Canine"
print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine

# Change instance attribute only for dog1
dog1.name = "Max"
print(dog1.description())  # Output: Max is 3 years old.
print(dog2.description())  # Output: Lucy is 5 years old.

# ----------------------------------------------
# Encapsulation: Private attributes and methods
# ----------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute (name mangling with __)

    def get_age(self):
        # Getter method to access private attribute
        return self.__age

    def set_age(self, age):
        # Setter method with validation
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

person = Person("Alice", 30)
print(person.name)       # Output: Alice
# print(person.__age)    # Error! Can't access private attribute directly
print(person.get_age())  # Output: 30
person.set_age(35)
print(person.get_age())  # Output: 35
person.set_age(-5)       # Output: Age must be positive.

# ----------------------------------------------
# Inheritance: Creating subclasses from base classes
# ----------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

cat = Cat("Whiskers")
print(cat.speak())  # Output: Whiskers says Meow!

# ----------------------------------------------
# Polymorphism: Methods with the same name behave differently
# ----------------------------------------------
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"

bird = Bird("Tweety")

# List of different animals
animals = [cat, bird]

for animal in animals:
    print(animal.speak())
# Output:
# Whiskers says Meow!
# Tweety says Chirp!

# ----------------------------------------------
# Class Methods and Static Methods
# ----------------------------------------------
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        # Alternative constructor using diameter
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def circle_info():
        return "Circles are round shapes with all points equidistant from the center."

circle1 = Circle(5)
print(circle1.area())  # Output: 78.53975

circle2 = Circle.from_diameter(10)
print(circle2.radius)  # Output: 5.0

print(Circle.circle_info())  # Output: Circles are round shapes with all points equidistant from the center.

# ----------------------------------------------
# Summary:
# ----------------------------------------------
# - Classes bundle data and methods together.
# - Use __init__ for initialization.
# - Attributes can be instance-level or class-level.
# - Private attributes use __ prefix.
# - Inheritance allows code reuse and polymorphism.
# - Class methods (@classmethod) work with the class.
# - Static methods (@staticmethod) don’t access class or instance.

