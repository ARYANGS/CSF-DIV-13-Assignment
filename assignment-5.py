import re

text = input("Enter a string: ")

if re.search(r'^[a-zA-Z0-9]+$', text):
    print("Contains only a-z, A-Z, and 0-9.")
else:
    print("Contains other characters.")