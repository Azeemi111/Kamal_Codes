#-----------------------------------------------------------------------------
# Name:        Temperature Advice
# Purpose:     Recommending clothing based off the current weather.
# Author:      Kamal Azeemi
# Created:     28-Feb-2025
# Updated:     4-Mar-2025
#-----------------------------------------------------------------------------
print("Hey, the weather recently is causing many flues and colds due to random changes in temperature, to avoid this I will be advising you how to dress appropriate to the weather")
print() #Spacing out the code to make it look visually appealing
print()
temper = int(input("What is the temperature today?: ")) #Storeing users input by setting a variable

if temper <=10: #Executing different possibilities based off the users input
    print("\033[34mIt's cold outside. Wear a jacket!")
elif 10 <= temper <= 25:
    print("\033[35mIt's a nice day. Wear short-sleeves!")
elif temper >=25:
    print("\033[31mIt's hot outside. Stay cool!")
else: #Setting a response if the user inputs something different then the possibilities listed above
    print("\033[0mPlease enter the temperature again, if you entered the degree sign please do not type the symbol.")