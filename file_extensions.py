import re

files = input("Enter filenames separated by space: ").split()

count = {}

for file in files:
    match = re.search(r'\.[A-Za-z0-9]+$', file)

    if match:
        ext = match.group()
        count[ext] = count.get(ext, 0) + 1

print("Extension count:", count)