import art 
logo = art.logo
from random import randint
easy_level_turns = 10
hard_level_turns = 5

def set_difficulty():
    level = input("Choose a difficulty type easy or hard:")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns
    
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns-1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns-1
    else:
        print("You got it. You won the game")
    
def game():
    print(logo)
    print("Welcome to the user guessing game")
    # choosing number from 1 to 100
    answer = randint(1,100)
    turns = set_difficulty()
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of turns, You lose")
            return
        elif guess != answer:
            print("Guess again")

game()

    