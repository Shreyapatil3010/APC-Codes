
import re

text = input("Enter a text: ")

pattern = r'\b\d{10}\b'

phone_numbers = re.findall(pattern, text)

print("Extracted Phone Numbers:")

if phone_numbers:
    for number in phone_numbers:
        print(number)
else:
    print("No phone numbers found.")
