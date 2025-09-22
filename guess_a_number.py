import random



def play_game():
    computer_number = random.randint(1, 100)
    print("Hello, dear friend! Want to play a game?")
    print("Can you guess the number i have generated? It should be between 1 and 100 :)")

    while True:
        try:
            original_number_of_tries = int(input("You have n tries to guess it. Please enter n: "))
            if original_number_of_tries <= 0:
                print("Please enter a positive number of tries, dum dum.")
                continue
            break
        except ValueError:
            print("Sorry, lad, wrong kinda input. Try again?")



    number_of_tries_left = original_number_of_tries

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
            return

        elif player_number > computer_number:
            print("Ooops, too high! Better get your head out of the clouds!")

        else:
            print("Oh no, too low! You gotta lift your spirits up ASAP!")

        number_of_tries_left -= 1

    print(f"Oh no! You are all out of tries! The number was: {computer_number}")

while True:
    play_game()
    answer = input("Wanna play again? (Yes or No pls): ").strip().lower()
    if answer != "yes":
        print("Game over, noob. Shutting down.")
        break
    else:
        print("NEW GAME")
        print("\n")
        print("Welcome back! Muahahahaha")

