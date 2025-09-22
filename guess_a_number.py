import random

game_on = True

while game_on is True:
    computer_number = random.randint(1, 100)
    print("Hello, dear friend! Want to play a game? Can you guess the number i have generated? It should be between 1 and 100 :)")
    print("You have n tries to guess it. Please enter n:", end="")
    original_number_of_tries = input()
    if not original_number_of_tries.isdigit():
        print("Sorry, lad, wrong kinda input. Try again?")
        continue
    number_of_tries_left = int(original_number_of_tries)

    while number_of_tries_left > 0:
        player_input = input("Gimme a number:")

        if player_input == "End":
            game_on = False
            print("Game severed manually. Try again?")
            break

        if not player_input.isdigit():
            print("Sorry, lad, wrong kinda input. Try again?")
            continue

        player_number = int(player_input)

        if player_number == computer_number:
            print(f"Way to go! You guessed it!. And it only took {original_number_of_tries - number_of_tries_left + 1} tries!")
            game_on = False
            print("Play again? (Yes/No)")
            break

        elif player_number > computer_number:
            print("Ooops, too high! Better get your head out of the clouds!")

        else:
            print("Oh no, too low! You gotta lift your spirits up ASAP!")

        number_of_tries_left -= 1

    if number_of_tries_left == 0:
        game_on = False
        print("Oh no! You are all out of tries! Play again? (Yes/No)")

    if game_on is False:
        answer = input()
        if answer == "Yes":
            game_on = True
        elif answer == "No":
            print("Game over, noob. Shutting down.")
            break

