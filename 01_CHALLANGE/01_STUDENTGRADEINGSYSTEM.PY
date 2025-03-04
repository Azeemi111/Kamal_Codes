#-----------------------------------------------------------------------------
# Name:        Student Grading System
# Purpose:     To provide ease in determining the grade you achieved based off percentage.
# Author:      Kamal Azeemi
# Created:     2-Mar-2025
# Updated:     3-Mar-2025
#-----------------------------------------------------------------------------
print("Hello! I know it can be difficult to determine the grade you achieved. Let's calculate what grade you got together.")
print()

score = int(input("Write your score out of 100 percent: "))
print()

if score >= 90:
    print("\033[34mCongratulations! You have gotten a 4+. Keep up the good work!")
elif 87 <= score <= 89:
    print("\033[34mCongratulations! You have achieved a level 4.")
elif 80 <= score <= 86:
    print("\033[35mCongratulations! You have achieved a level 4-.")
elif 77 <= score <= 79:
    print("\033[35mCongratulations! You have gotten a level 3+. Try achieving a level 4 next time!")
elif 74 <= score <= 76:
    print("\033[32mGood job! You have gotten a level 3. Try doing better next time :)")
elif 70 <= score <= 73:
    print("\033[32mNice! You got a level 3-.")
elif 67 <= score <= 69:
    print("\033[31mUnfortunately, you got a level 2+.")
elif 64 <= score <= 66:
    print("\033[31mUnfortunately, You got a level 2.")
elif 60 <= score <= 63:
    print("\033[31mUnfortunately, You got a level 2-.")
elif 57 <= score <= 59:
    print("\033[31mYou got a level 1+. Practice more or else no more collage and university dreams for you!")
elif 54 <= score <= 56:
    print("\033[31mYou got a level 1. Practice more or else no more collage and university dreams for you!")
elif 50 <= score <= 53:
    print("\033[31mYou got a level 1-. Practice more or else no more collage and university dreams for you!")
else:
    print("\033[31mYou scored below 50. Keep practicing and don't give up! or else no more collage and university dreams for you!")
