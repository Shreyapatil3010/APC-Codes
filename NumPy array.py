import numpy as np

a = np.array([10, 20, 30, 40])

labels = np.array(['A', 'B', 'C', 'D'])

print("Original Array:")
print(a)

print("Character Labels:")
print(labels)

print("Array with Labels:")

for i in range(len(a)):
    print(labels[i], ":", a[i])