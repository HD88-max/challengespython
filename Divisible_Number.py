number = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
x = number%number2
if x == 0:
    print("The two numbers can be divided. ")
else:
    print("The two numbers cannot be divided.")