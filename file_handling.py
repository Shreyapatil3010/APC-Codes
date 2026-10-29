
file = open("student.txt", "w")
file.write("Name: Shreya\n")
file.write("Course: Computer Engineering\n")
file.close()

file = open("student.txt", "r")
data = file.read()
print(data)
file.close()
