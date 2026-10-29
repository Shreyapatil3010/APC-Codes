
from collections import Counter
import re

text = input("Enter a paragraph: ")

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

print("Total number of words:", len(words))

frequency = Counter(words)

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

print("\nTop 3 most frequent words:")
for word, count in frequency.most_common(3):
    print(word, ":", count)

vowels = "aeiou"
vowel_count = sum(1 for ch in text.lower() if ch in vowels)

print("\nTotal number of vowels:", vowel_count)
