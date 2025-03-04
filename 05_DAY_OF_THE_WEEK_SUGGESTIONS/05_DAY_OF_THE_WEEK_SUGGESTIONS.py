# -----------------------------------------------------------------------------
# Name:        Week Suggestions
# Purpose:     Providing fun activities to complete throughout the week based off the day.
# Author:      Kamal Azeemi
# Created:     3-Feb-2025
# Updated:     4-Mar-2025
# -----------------------------------------------------------------------------
print("This program will help you by providing activities to complete based on the day of the week!")
day = input("Enter the day of the week: ")
print()
print()

if day == "Monday" or day == "monday" or day =="MONDAY":
    print("\033[34mStart your week with a workout!")
elif day == "Tuesday" or day == "tuesday" or day =="TUESDAY":
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
else:
    print("\033[31mPlease enter a valid day of the week! For example 'Sunday'.")