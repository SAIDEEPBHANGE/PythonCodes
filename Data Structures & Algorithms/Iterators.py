# ---------------------------------------------
# ✅ What is an Iterator?
# ---------------------------------------------
# An iterator is an object that enables traversal over all elements of a collection (like a list or tuple).
# It implements two methods:
#   - __iter__() : Returns the iterator object itself
#   - __next__() : Returns the next item in the sequence
# When no more items are left, __next__() raises StopIteration to signal the end.

# ---------------------------------------------
# ✅ Iterating Over a List with an Iterator
# ---------------------------------------------
my_list = [10, 20, 30]

# Get an iterator object from the list
my_iter = iter(my_list)

print(next(my_iter))  # Output: 10
print(next(my_iter))  # Output: 20
print(next(my_iter))  # Output: 30

# next(my_iter)  # Raises StopIteration if uncommented

# ---------------------------------------------
# ✅ Using a For Loop (which uses iterators internally)
# ---------------------------------------------
for item in my_list:
    print(item)

# ---------------------------------------------
# ✅ Creating a Custom Iterator Class
# ---------------------------------------------
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # The iterator object is self
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Signal iteration end
        else:
            val = self.current
            self.current -= 1
            return val

# Using the custom iterator
countdown = CountDown(5)
for number in countdown:
    print(number)

# ---------------------------------------------
# ✅ Difference Between Iterable and Iterator
# ---------------------------------------------
# Iterable: An object capable of returning its iterator (has __iter__ method)
# Iterator: The object with __next__ method which returns next element

print(hasattr(my_list, "__iter__"))  # True (list is iterable)
print(hasattr(my_list, "__next__"))  # False (list is not iterator)

print(hasattr(my_iter, "__iter__"))  # True (iterator)
print(hasattr(my_iter, "__next__"))  # True (iterator)

# ---------------------------------------------
# ✅ Using Generators (Simpler Way to Create Iterators)
# ---------------------------------------------
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen)  # StopIteration

# Generators automatically implement __iter__() and __next__()

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Iterators allow sequential access to elements in a collection
# - Use iter() to get an iterator from an iterable
# - Use next() to get items one-by-one until StopIteration is raised
# - You can create custom iterators by implementing __iter__ and __next__
# - Generators provide a convenient way to create iterators using yield
