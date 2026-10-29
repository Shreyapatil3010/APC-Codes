
book1 = input("Enter text of Book 1: ")
book2 = input("Enter text of Book 2: ")

words1 = set(book1.lower().split())
words2 = set(book2.lower().split())

print("\nUnique words in Book 1:", words1)
print("Unique words in Book 2:", words2)

print("\nCommon words:", words1 & words2)

print("Words only in Book 1:", words1 - words2)
print("Words only in Book 2:", words2 - words1)

all_words = words1 | words2

print("All unique words:", all_words)
print("Total unique words:", len(all_words))
