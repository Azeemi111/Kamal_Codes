# -----------------------------------------------------------------------------
# Name:        Week Suggestions
# Purpose:     Providing fun activities to complete throughout the week based off the day.
# Author:      Kamal Azeemi
# Created:     3-Feb-2025
# Updated:     4-Mar-2025
# -----------------------------------------------------------------------------
print("This program will help you by providing activities to complete based on the day of the week!")
day = input("Enter the day of the week: ") #Storeing users input by setting a variable
print() #Spacing out the code to make it look visually appealing
print()

if day == "Monday" or day == "monday" or day =="MONDAY": #Executing different possibilities based off the users input
    print("\033[34mStart your week with a workout!")
elif day == "Tuesday" or day == "tuesday" or day =="TUESDAY": #Keeping many "OR'S" incase the users spelling impacts the code
    print("\033[34mIt's a great day to read a book!")
elif day == "Wednesday" or day == "wednesday" or day =="WEDNESDAY":
    print("\033[32mMid-week movie night!")
elif day == "Thursday" or day == "thursday" or day =="THURSDAY":
    print("\033[35mTry a new recipe!")
elif day == "Friday" or day == "friday" or day =="FRIDAY":
    print("\033[34mRelax and enjoy the weekend!")
elif day == "Saturday" or day == "saturday" or day =="SATURDAY":
    print("\033[35mGo for a hike!")
elif day == "Sunday" or day == "sunday" or day =="SUNDAY":
    print("\033[34mPrepare for the week ahead with some self-care.")
else: #Setting a response if the user inputs a number different then the possibilities listed above
    print("\033[31mPlease enter a valid day of the week! For example 'Sunday'.")