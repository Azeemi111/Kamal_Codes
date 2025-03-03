print("Hello, this program will help determine if you a illegible to vote or not")
age = int(input("What is your age? "))
print()
print()
if age >= 18:
    print("\033[34mYou are able to vote!")
else age < 18:
    print("\033[31mYou're too young, go play outside! :))")
