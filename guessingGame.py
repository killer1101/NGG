
import random
print("number guessing game")
number = random.randint(1, 10)
chances = 0
print("guess a number between 1 and 10: ")

while chances < 5:

    guess = int(input("Enter Your Guess:- "))


    if guess == number:
        print("Congrats you WON!")
        break
    
    elif guess < number:
        print("Think of a higher number than", guess)
        
    else:
        print("think of a lower number than", guess)

    chances += 1

if not chances < 5:
    print("YOU LOOSE! The number was: ", number)