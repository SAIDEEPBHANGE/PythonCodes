# ==============================================
# Inheritance in Python - Object-Oriented Programming (OOP)
# ==============================================

# ----------------------------------------------
# What is Inheritance?
# ----------------------------------------------
# Inheritance allows a class (child/subclass) to inherit attributes and methods
# from another class (parent/base class).
# This promotes code reuse and a hierarchical relationship between classes.

# ----------------------------------------------
# Basic Inheritance Example
# ----------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!

# ----------------------------------------------
# Accessing Parent Class Methods
# ----------------------------------------------
class Cat(Animal):
    def speak(self):
        # Call the parent class method (optional)
        base_message = super().speak()
        return f"{base_message} But {self.name} says Meow!"

cat = Cat("Whiskers")
print(cat.speak())
# Output:
# Whiskers makes a sound. But Whiskers says Meow!

# ----------------------------------------------
# Adding New Methods in Child Class
# ----------------------------------------------
class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying."

bird = Bird("Tweety")
print(bird.speak())  # Inherited method
print(bird.fly())    # New method in Bird

# ----------------------------------------------
# Overriding the __init__ Method
# ----------------------------------------------
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Vehicle: {self.brand} {self.model}"

# Car inherits Vehicle but adds new attribute
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors

    def car_info(self):
        return f"{self.brand} {self.model} with {self.doors} doors."

car = Car("Toyota", "Camry", 4)
print(car.info())      # Output: Vehicle: Toyota Camry
print(car.car_info())  # Output: Toyota Camry with 4 doors.

# ----------------------------------------------
# Multiple Inheritance
# ----------------------------------------------
class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming fast!"

# Duck inherits from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())    # From Flyer
print(duck.swim())   # From Swimmer
print(duck.quack())  # Own method

# ----------------------------------------------
# Method Resolution Order (MRO)
# ----------------------------------------------
# When using multiple inheritance, Python follows MRO to decide method lookup.
print(Duck.mro())
# Output shows the order Python will check classes for methods.

# ----------------------------------------------
# Summary:
# ----------------------------------------------
# - Inheritance helps create hierarchical relationships.
# - Child classes inherit attributes and methods from parents.
# - Child classes can override methods or extend functionality.
# - Use super() to access parent methods.
# - Python supports multiple inheritance with MRO to resolve method calls.

