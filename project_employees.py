
project1 = {"Shreya", "Priya", "Rahul", "Amit"}
project2 = {"Priya", "Rahul", "Sneha", "Rohit"}

print("Project 1 Employees:", project1)
print("Project 2 Employees:", project2)

print("Employees working on both projects:", project1 & project2)

print("Employees only in Project 1:", project1 - project2)

print("Employees only in Project 2:", project2 - project1)

print("All unique employees:", project1 | project2)

print("Total unique employees:", len(project1 | project2))
