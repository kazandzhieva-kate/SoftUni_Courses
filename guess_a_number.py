import random

def play_game(max_number, original_number_of_tries):
    computer_number = random.randint(1, max_number)
    number_of_tries_left = original_number_of_tries

    while number_of_tries_left > 0:
        player_input = input("Gimme a number:")

        if player_input.strip().lower() == "end":
            print("Game severed manually.")
            return None

        if not player_input.isdigit():
            print("Sorry, lad, wrong kinda input. Try again?")
            continue

        player_number = int(player_input)

        if player_number == computer_number:
            print(f"Way to go! You guessed it!. And it only took {original_number_of_tries - number_of_tries_left + 1} tries!")
            return True

        elif player_number > computer_number:
            print("Ooops, too high! Better get your head out of the clouds!")

        else:
            print("Oh no, too low! You gotta lift your spirits up ASAP!")

        number_of_tries_left -= 1

    print(f"Oh no! You are all out of tries! The number was: {computer_number}")

max_number = 100
level = 1

while True:
    print("Hello, dear friend! Want to play a game?")
    print(f"Can you guess the number i have generated? It should be between 1 and {max_number} :)")
    print(f"---Level {level}---")
    while True:
        try:
            original_number_of_tries = int(input("You have n tries to guess it. Please enter n: "))
            if original_number_of_tries <= 0:
                print("Please enter a positive number of tries, dum dum.")
                continue
            break
        except ValueError:
            print("Sorry, lad, wrong kinda input. Try again?")

    win = play_game(max_number, original_number_of_tries)

    if win:
        level += 1
        max_number += 100

        answer = input("Wanna play again? (Yes or No pls): ").strip().lower()
        if answer != "yes":
            print(f"Thanks for playing! You made it to level {level}.")
            break
        else:
            print("Welcome back! Muahahahaha")

