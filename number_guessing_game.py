from art import logo
import random

print(logo)

RANDOM_NUMBER = random.randint(1, 100)

print("Welcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

easy_tries_remaining = 10
hard_tries_remaining = 5
guess_correct = False

while guess_correct == False:
    if difficulty == 'easy':
        if easy_tries_remaining > 0:
            print(f"You have {easy_tries_remaining} tries remaining.")
            guess = int(input("Make a guess: "))
            if guess < RANDOM_NUMBER:
                print("Too low.")
                print("Guess again.")
                easy_tries_remaining -= 1
            elif guess > RANDOM_NUMBER:
                print("Too high.")
                print("Guess again.")
                easy_tries_remaining -= 1
            elif guess == RANDOM_NUMBER:
                print(f"You got it! The correct number was {RANDOM_NUMBER}.")
                guess_correct = True
        else:
            print(f"You lose. The correct numer is {RANDOM_NUMBER}.")
            guess_correct = True
        
    elif difficulty == 'hard':
        if hard_tries_remaining > 0:
            print(f"You have {hard_tries_remaining} tries remaining.")
            guess = int(input("Make a guess: "))
            if guess < RANDOM_NUMBER:
                print("Too low.")
                print("Guess again.")
                hard_tries_remaining -= 1
            elif guess > RANDOM_NUMBER:
                print("Too high.")
                print("Guess again.")
                hard_tries_remaining -= 1
            elif guess == RANDOM_NUMBER:
                print(f"You got it! The correct number was {RANDOM_NUMBER}.")
                guess_correct = True
        else:
            print(f"You lose. The correct numer is {RANDOM_NUMBER}.")
            guess_correct = True