"""
Name: game.py
Author: Fashola Oluwaseyifunmi Ademide
class : Computer programming(1026)
Date: 04/08/2022

game.py is a number guessing game.

"""

def main():

    import random

    answer = random.randint(1,100)
    trials = 9
    for count in range(0,9):
        number = int(input("Pick a number between 1-100: "))
        trials -= 1
        print("You have ", trials, "left")
        if number == answer:
           print ("Correct!")
           break
        elif number < answer:
            print("The number inputed is Too Low!")
        elif number > answer:
            print("The number inputed is Too High!")
    else:
        print("game over! You have run out of tries, the answer was: ", answer)
    restart = input("Do you want to start again? (Y/N) ").upper()
    if restart == "Y":
        main()

    else:
        exit()


#The  most effecient(fastest, fewest guesses) method is to guess a random number and if the computer says its too or high you reduce the number and vice versa.

#where the code starts
main()
