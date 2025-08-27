# ---------------------------------------------
# ✅ Common Exceptions in Python (With Examples)
# ---------------------------------------------

# 1️⃣ ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ You can't divide by zero!")

# 2️⃣ ValueError
try:
    number = int("abc")  # Invalid string to int
except ValueError:
    print("❌ Invalid value! Cannot convert to int.")

# 3️⃣ TypeError
try:
    result = "5" + 5  # Mixing str and int
except TypeError:
    print("❌ Type mismatch! Cannot add string and integer.")

# 4️⃣ IndexError
my_list = [1, 2, 3]
try:
    print(my_list[5])  # Index out of range
except IndexError:
    print("❌ Index out of range!")

# 5️⃣ KeyError
my_dict = {"name": "Alice"}
try:
    print(my_dict["age"])  # Key doesn't exist
except KeyError:
    print("❌ Key not found in dictionary.")

# 6️⃣ FileNotFoundError
try:
    file = open("not_found.txt", "r")  # File doesn't exist
except FileNotFoundError:
    print("❌ File not found!")

# 7️⃣ NameError
try:
    print(my_var)  # my_var is not defined
except NameError:
    print("❌ Variable not defined.")

# 8️⃣ ImportError
try:
    import non_existing_module
except ImportError:
    print("❌ Module could not be imported.")

# 9️⃣ AttributeError
try:
    x = 10
    x.append(5)  # int doesn't have 'append'
except AttributeError:
    print("❌ Attribute doesn't exist for this type.")

# ✅ General catch-all (not best practice, but useful in some cases)
try:
    something = 5 / 0
except Exception as e:
    print("⚠️ Some error occurred:", e)
