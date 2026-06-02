import random

secret_number= random.randint(1,10)

attempts=1

guess=int(input("Enter your guess:"))

while secret_number != guess:

    if guess < secret_number:
        print("Too low! Try again!")

    elif guess > secret_number:
        print("Too high! Try again!")
        
    attempts+=1

    guess = int(input("Enter your guess: "))
else:
    print("Congratulations! You guessed correctly!")


print("You took", attempts,"guesses!")
        
