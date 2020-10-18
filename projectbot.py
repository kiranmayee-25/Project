"""
This is a program for a chatbot which allows to play a  game and help you to gain some knowledge...
1.The bot will  greet and ask for name of a person
2.The bot will  welcome the person
3.Bot will ask what a person want to do ,it will offer a choice of things based upon what the bot is designed for
4.It will respond to users input appropriately
"""

from datetime import datetime
from greetings import greet_and_introduce,get_timeofday_greeting,welcome
from guessnumber import guess_number
from first_women import first_woman,show_choice,politics,awards,judge,driving,ips,climb_Mt,games,space


def calculations():
    expr=input("Enter your expression  : ")
    try:
        print('result : ',eval(expr))
    except:
        print("I don't understand that")

def show_menu():
    print("1.play guess number game")
    print("2.General Knowledge")
    print("3.Calculations")
    print("4.End this chat")
    print("*************\n")
    print("--Guide--")
    print("choice-1: Here you are going to guess a number by giving inputs the lower and upper ranges of numbers....Hope you will have a great fun!")
    print("choice-2: This can help you to improve you general knowledge by knowing the details about first indian woman in every field..")
    print("choice-3: In this you can perform mathematical calculations")
    try:
        return int(input("Enter your choice [1-4] : "))
    except:
        print("Only enter choice from 1,2,3 and 4")
        return 0



def bot():
    greet_and_introduce()
    name=input("Your Name: ")
    print("\nThat's cool!")
    welcome(name)
    choice=show_menu()
    while choice!=4:
        if choice==1:
            guess_number()
        elif choice==2:
            first_woman()
        elif choice==3:
            calculations()
        else:
            print("please enter a valid option")
        choice=show_menu()
bot()
