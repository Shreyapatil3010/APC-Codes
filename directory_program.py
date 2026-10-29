
import os

directory = "MyFolder"

if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created successfully")
else:
    print("Directory already exists")

print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir("."))
