
students = {"Shreya", "Priya", "Sneha", "Riya", "Amit"}

present = {"Shreya", "Priya", "Amit"}

absent = students - present

attendance = {
    "Present": present,
    "Absent": absent
}

print("Attendance Report")

print("\nPresent Students:")
for name in attendance["Present"]:
    print(name)

print("\nAbsent Students:")
for name in attendance["Absent"]:
    print(name)

print("\nTotal Students:", len(students))
print("Present Count:", len(present))
print("Absent Count:", len(absent))
