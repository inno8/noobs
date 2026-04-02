# Simple number guessing game
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Guess the number between 1 and 100!")

while True:
    guess = input("Your guess: ")
    guess = int(guess)
    attempts = attempts + 1
    
    if guess == secret:
        print("You got it in " + str(attempts) + " attempts!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    
    if attempts >= max_attempts:
        print("Game over! The number was " + str(secret))
        break

print("Thanks for playing!")
