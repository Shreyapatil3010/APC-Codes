import re

file = open("sample.txt", "r")

text = file.read()
file.close()

text = text.lower()

words = re.findall(r'\b\w+\b', text)

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print("Total words:", len(words))

print("Top 10 frequent words:")

top = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word, frequency in top[:10]:
    print(word, ":", frequency)