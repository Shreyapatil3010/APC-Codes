
from array import array

numbers = array('i', [10, 20, 30, 40, 50])

print("Array elements:", numbers)

numbers.append(60)
print("After adding element:", numbers)

numbers.remove(30)
print("After removing 30:", numbers)

print("First element:", numbers[0])
print("Array length:", len(numbers))
