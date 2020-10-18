import random
import math
def guess_number():
    print("Let's start our game!")
    print("please enter the lower and upper ranges of numbers")
    lower=int(input("please give the lower range : "))
    upper=int(input("please give the upper range : "))
    if lower>=0 and upper>=0:
        number=random.randint(lower,upper)
        chances=round(math.log(upper-lower+1,2))
        print("You have only",chances,"chances to guess the number\n")
        print("Best of Luck!")
        count=0
        while count<chances:
            count+=1
            playerguess=int(input("Guess a number: "))
            if playerguess > number:
                print("That's too high!")
            elif playerguess< number:
                print("That's too low")
            elif playerguess==number:
                print("**Congratulations you did it**\n")
                break
            if count >=chances:
                print("\n--Oops! you lost, Better luck next time--\n")
                print("The number is: ",number,"\n")
                break
    else:
        print("Please give valid inputs")

   