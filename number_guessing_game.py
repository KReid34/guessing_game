from art import logo
import random

print(logo)

RANDOM_NUMBER = random.randint(1, 100)

print("Welcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

easy_tries_remaining = 10
hard_tries_remaining = 5
game_continue = True

while game_continue:
    guess = int(input("Make a guess: "))
    if guess < RANDOM_NUMBER:
        print("Too low.")
        print("Guess again.")
        if difficulty == 'easy':
            easy_tries_remaining -= 1
            print(f"You have {easy_tries_remaining} tries remaining.")
        else:
            hard_tries_remaining -= 1
            print(f"You have {hard_tries_remaining} tries remaining.")
    elif guess > RANDOM_NUMBER:
        print("Too high.")
        print("Guess again.")
        if difficulty == 'easy':
            easy_tries_remaining -= 1
            print(f"You have {easy_tries_remaining} tries remaining.")
        else:
            hard_tries_remaining -= 1
            print(f"You have {hard_tries_remaining} tries remaining.")
    elif guess == RANDOM_NUMBER:
        print(f"You got it! The correct number was {RANDOM_NUMBER}.")
        game_continue = False
    else:
        print(f"You lose. The correct numer is {RANDOM_NUMBER}.")
        game_continue = False
