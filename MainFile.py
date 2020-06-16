import string
import math
from WorSheetGenerator import WorksheetFunction

def main():
    welcome_message = "\t \t \t Welcome to Math Worksheet Creator "
    choice_message = "Please choose math function by entering:"
    addition_choice = "\t1 for addition problems"
    multiplication_choice = "\t2 for multiplication problems"

    user_name = input("What is your name? ")

    print (welcome_message + user_name)
    print
    print (choice_message)
    print (addition_choice)
    print (multiplication_choice)

    try:
        user_choice = int(input("Enter your choice:"))

        if isinstance(user_choice,int):
            if user_choice == 1:
                WorksheetFunction(1)

            elif user_choice == 2:
                WorksheetFunction(2)

            else:
                print ("Please enter valid value")

    except ValueError:
            print ("Please enter valid integer value")

main()
