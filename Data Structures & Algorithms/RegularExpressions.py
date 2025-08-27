import re  # Import the regex module

# ---------------------------------------------
# ✅ What is a Regular Expression?
# ---------------------------------------------
# A regular expression (regex) is a special sequence of characters
# that helps match or find patterns in strings.
# Useful for validation, searching, replacing, and splitting strings.

# ---------------------------------------------
# ✅ Basic Functions in re module:
# ---------------------------------------------
# re.match()    – Checks for a match only at the beginning of the string
# re.search()   – Searches for the pattern anywhere in the string
# re.findall()  – Returns a list of all matches in the string
# re.finditer() – Returns an iterator yielding match objects for all matches
# re.sub()      – Replaces occurrences of the pattern with a replacement string
# re.split()    – Splits the string by the occurrences of the pattern

# ---------------------------------------------
# ✅ Simple Match Example
# ---------------------------------------------
text = "Hello, my phone number is 123-456-7890"

pattern = r"\d{3}-\d{3}-\d{4}"  # Pattern for phone number: 3 digits-3 digits-4 digits

# Using re.search to find the phone number in text
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No phone number found")

# ---------------------------------------------
# ✅ Using re.match (matches only at start)
# ---------------------------------------------
start_text = "123-456-7890 is my number"
m = re.match(pattern, start_text)

if m:
    print("Match at start:", m.group())
else:
    print("No match at start")

# ---------------------------------------------
# ✅ Finding All Matches with findall()
# ---------------------------------------------
text2 = "My numbers are 123-456-7890 and 987-654-3210"
all_numbers = re.findall(pattern, text2)
print("All phone numbers:", all_numbers)

# ---------------------------------------------
# ✅ Iterating Matches with finditer()
# ---------------------------------------------
for match in re.finditer(pattern, text2):
    print(f"Found '{match.group()}' at position {match.start()}-{match.end()}")

# ---------------------------------------------
# ✅ Using re.sub to Replace Text
# ---------------------------------------------
text3 = "Call me at 123-456-7890"
new_text = re.sub(pattern, "XXX-XXX-XXXX", text3)
print("After substitution:", new_text)

# ---------------------------------------------
# ✅ Splitting a String Using regex
# ---------------------------------------------
csv = "apple,banana;cherry orange|grape"
# Split by comma, semicolon, space, or pipe
split_pattern = r"[ ,;|]+"
fruits = re.split(split_pattern, csv)
print("Split fruits:", fruits)

# ---------------------------------------------
# ✅ Common Regex Syntax
# ---------------------------------------------
# .      - Any character except newline
# ^      - Start of string
# $      - End of string
# *      - 0 or more repetitions
# +      - 1 or more repetitions
# ?      - 0 or 1 repetition (optional)
# {n}    - Exactly n repetitions
# {n,m}  - Between n and m repetitions
# []     - Set of characters, e.g. [a-z]
# \d     - Digit [0-9]
# \w     - Word character [a-zA-Z0-9_]
# \s     - Whitespace
# \b     - Word boundary
# |      - OR operator
# ()     - Grouping

# ---------------------------------------------
# ✅ Example: Validate Email Address
# ---------------------------------------------
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

emails = ["test@example.com", "invalid-email@", "hello.world@mail.co"]

for email in emails:
    if re.match(email_pattern, email):
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {email}")

# ---------------------------------------------
# ✅ Using Groups and Extracting Data
# ---------------------------------------------
date_text = "Today is 2025-08-27"
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"  # Groups for year, month, day

date_match = re.search(date_pattern, date_text)

if date_match:
    year, month, day = date_match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

# ---------------------------------------------
# ✅ Flags for regex
# ---------------------------------------------
# re.IGNORECASE or re.I  - Case insensitive matching
# re.MULTILINE or re.M   - Multi-line matching (^ and $ match start/end of each line)
# re.DOTALL or re.S      - Dot matches newline too

text_multiline = "First line\nSecond line"

pattern_line = r"^Second"

# Without MULTILINE flag - no match
print("Match without MULTILINE:", re.search(pattern_line, text_multiline))

# With MULTILINE flag - matches "Second" at start of 2nd line
print("Match with MULTILINE:", re.search(pattern_line, text_multiline, re.MULTILINE))

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Use the 're' module to work with regex in Python
# - regex helps match, search, replace, and split text based on patterns
# - Important functions: match, search, findall, finditer, sub, split
# - Learn regex syntax and special characters for powerful pattern matching
