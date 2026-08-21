import re

file_name = input("Enter file name: ")
target = input("Enter word to find: ")
replacement = input("Enter replacement word: ")

choice = input("Case-sensitive? (yes/no): ")

file = open(file_name, "r")
text = file.read()
file.close()

if choice.lower() == "yes":
    text = text.replace(target, replacement)
else:
    text = re.sub(re.escape(target), replacement, text, flags=re.IGNORECASE)

output_file = open("output.txt", "w")
output_file.write(text)
output_file.close()

print("Replacement completed.")
print("Modified text saved in output.txt")