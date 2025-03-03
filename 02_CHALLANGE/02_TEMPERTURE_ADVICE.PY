print("Hey, the weather recently is causing many flues and colds due to random changes in temperature, to avoid this I will be advising you how to dress appropriate to the weather")
print()
print()
temper = int(input("What is the temperature today?: "))

if temper <=10:
    print("\033[34mIt's cold outside. Wear a jacket!")
elif 10 <= temper <= 25:
    print("\033[35mIt's a nice day. Wear short-sleeves!")
elif temper >=25:
    print("\033[31mIt's hot outside. Stay cool!")
else:
    print("\033[0mPlease enter the temperature again, if you entered the degree sign please do not type the symbol.")