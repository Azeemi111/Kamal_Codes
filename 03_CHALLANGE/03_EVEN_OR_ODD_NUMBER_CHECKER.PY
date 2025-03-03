print("Hello, this code will help interpret if the number you type is even or odd")
number = int(input("Enter your number: "))
print()
print()

if number % 2 == 0:
    print("\033[33mThe number you have inputted is even.")
else:
    print("\033[31mThe number you have inputted is odd.")