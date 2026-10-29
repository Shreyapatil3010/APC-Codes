
names = []
grades = []

def add_student(name, grade):
    names.append(name)
    grades.append(grade)
    print("Student added successfully")

def update_grade(name, grade):
    if name in names:
        index = names.index(name)
        grades[index] = grade
        print("Grade updated successfully")
    else:
        print("Student not found")

def remove_student(name):
    if name in names:
        index = names.index(name)
        names.pop(index)
        grades.pop(index)
        print("Student removed successfully")
    else:
        print("Student not found")

def display_average():
    if grades:
        print("Average Grade:", sum(grades) / len(grades))
    else:
        print("No grades available")

def display_extremes():
    if grades:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))
    else:
        print("No grades available")

add_student("Shreya", 85)
add_student("Priya", 90)
add_student("Rahul", 75)

update_grade("Rahul", 80)
remove_student("Priya")

print("Students:", names)
print("Grades:", grades)

display_average()
display_extremes()
