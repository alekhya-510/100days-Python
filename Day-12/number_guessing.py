import random
from art import logo
print(logo)

print("Welcome to number guessing game!")
print("I am thinking of a number between 1 and 100.")
difficulty_level= input("Choose a difficulty.Type 'easy' or 'hard':")

number_of_guesses = 0
number=random.randint(1,100)
# print(f"guessing number is {number}")

def easy_game():
        number_of_guesses = 10
        print(f"You have {number_of_guesses} attempts to guess the number.")
        check_answer(number_of_guesses)


def hard_game():
    number_of_guesses = 5
    print(f"You have {number_of_guesses} attempts to guess the number.")
    check_answer(number_of_guesses)

def check_answer(number_of_guesses):
    for i in range(1, number_of_guesses + 1):
        guess_input = int(input(f"Make a guess : "))
        number_of_guesses -= 1
        if guess_input == number:
            print(f"Congratulations! You guessed the correct number {number}!.")
            return number
        elif guess_input < number:
            print(f"Too low.\nGuess again. \nYou have {number_of_guesses} attempts remaining to guess the number ")
        elif guess_input > number:
            print(f"Too high.\nGuess again. \nYou have {number_of_guesses} attempts remaining to guess the number ")

if difficulty_level == "easy":
    easy_game()
elif difficulty_level == "hard":
    hard_game()
