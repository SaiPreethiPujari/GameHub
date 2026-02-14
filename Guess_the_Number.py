import random
import guessthenum
EASY_ATTEMPTS=10
HARD_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_ATTEMPTS
    else:
        print("Inavild Input..!!!")
def check_answer(guess_answer,answer,attempts):
    if guess_answer>answer:
        print("Guess is too high")
        return attempts-1
    elif guess_answer<answer:
        print("Guess is too low")
        return attempts-1
    elif guess_answer==answer:
        print(f"{guess_answer} is correct .Guess is correct.YOU WIN")

def game():
    print(guessthenum.logo)
    print("Let me think of a number between 1 to 50")
    answer = random.randint(1, 50)
    level = input("Choose the level 'hard' or 'easy': ").lower()
    attempts = set_difficulty(level)
    guess_answer = 0
    while guess_answer != answer:
        print(f"You have {attempts} attempts remaining.")
        guess_answer = int(input("Enter a number: "))
        attempts = check_answer(guess_answer, answer, attempts)

        if attempts == 0:
            print(f"YOU LOSE. You are out of attempts. The correct answer is {answer}")
            return
        elif guess_answer != answer:
            print("Guess again.")

game()
