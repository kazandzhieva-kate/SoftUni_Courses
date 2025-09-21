import random

computer_number = random.randint(1, 100)
print("Hello, dear friend! Want to play a game? Can you guess the number i have generated? It should be between 1 and 100 :)")

while True:
    player_input = input("Gimme a number:")

    if not player_input.isdigit():
        print("Sorry, lad, wrong input. Try again?")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("Way to go! You guessed it!")
        break

    elif player_number > computer_number:
        print("Ooops, too high! Better get your head out of the clouds!")

    else:
        print("Oh no, too low! You gotta lift your spirits up ASAP!")