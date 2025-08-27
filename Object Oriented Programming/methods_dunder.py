# ==============================================
# Methods and Dunder (Magic) Methods in Python Classes
# ==============================================

# ----------------------------------------------
# What are Methods?
# ----------------------------------------------
# Methods are functions defined inside a class and can manipulate instance data.
# They typically take 'self' as the first parameter to access instance attributes.

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name}."

    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}, you are now {self.age} years old."

person = Person("Alice", 30)
print(person.greet())          # Output: Hello, my name is Alice.
print(person.have_birthday())  # Output: Happy Birthday Alice, you are now 31 years old.

# ----------------------------------------------
# What are Dunder (Magic) Methods?
# ----------------------------------------------
# Dunder methods are special methods with double underscores at start and end (__method__).
# They enable classes to implement/override built-in behaviors like printing, arithmetic, etc.

# Common dunder methods include:
# __init__ : Constructor method to initialize objects.
# __str__  : Defines behavior for str() and print().
# __repr__ : Defines unambiguous representation for debugging.
# __len__  : Called by len() function.
# __add__  : Called by + operator.
# __eq__   : Called by == operator.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ controls what print(book) shows
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # __repr__ is for developer/debugging output
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    # __len__ allows len(book) to return number of pages
    def __len__(self):
        return self.pages

    # __add__ allows adding two books' pages together
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

    # __eq__ allows book1 == book2 to compare titles and authors
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title) and (self.author == other.author)
        return False

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)
book3 = Book("1984", "George Orwell", 328)

print(book1)           # Output: '1984' by George Orwell
print(repr(book2))     # Output: Book('Animal Farm', 'George Orwell', 112)
print(len(book1))      # Output: 328
print(book1 + book2)   # Output: 440
print(book1 == book3)  # Output: True
print(book1 == book2)  # Output: False

# ----------------------------------------------
# More useful dunder methods (examples)
# ----------------------------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(v1)            # Output: Vector(2, 3)
print(v1 + v2)       # Output: Vector(6, 4)
print(v1 * 3)        # Output: Vector(6, 9)
print(v1 == Vector(2, 3))  # Output: True

# ----------------------------------------------
# Summary:
# ----------------------------------------------
# - Methods define behaviors of class instances.
# - Dunder (magic) methods customize Python built-in behavior for your objects.
# - Common dunder methods: __init__, __str__, __repr__, __len__, __add__, __eq__, etc.
# - Overriding these improves readability and usability of your classes.

