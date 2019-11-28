import random


randomNumber = random.randint(0, 20)

counter = 0



while counter < 6:
    print("Guess a number: ")
    guess = input()
    guess = int(guess)

    counter = counter + 1

    if guess == randomNumber:
        print("You guessed it right!")
        break
    elif guess > randomNumber:
        print("The number you guessed is too high!")
    elif guess < randomNumber:
        print("THe number you have gussed it too low!")
    else:
        print("Please enter a valid number from 0 to 20")

    