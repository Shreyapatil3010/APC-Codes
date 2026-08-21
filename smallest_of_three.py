a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if b > a and c > a:
    print("The smallest number is :",a)
elif a > b and c > b :
    print("The smallest number is :",b)
else :
    print("The smallest number is :",c)