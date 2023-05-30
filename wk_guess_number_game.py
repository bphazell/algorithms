import random

# validates a number is between the start and stop value


def number_validation(num, start, stop):
    if (num) >= start and (num) <= 10:
        return 1
    else:
        print("Number must be between", start, "and", stop)
        return 0

# Stores all guesses into a list
# checks to see that any new guesses aren't in the list


def new_guess_validation(num, list):
    if num in list:
        print("You already guessed that")
        return 0
    else:
        return 1


def guess_random_number(tries, start, stop):
    # random number between start and stop is selected
    ran_num = random.randint(start, stop)
    guesses = []

    # while continues until tries = 0
    while tries != 0:
        print("Number of tries left:", (tries))
        # user is prompted to guess a number
        guess = int(input("Guess a number between 0 and 10: "))
        # validates a number is between the start and stop value
        # validates only new guesses are selected
        if (number_validation(guess, start, stop) == 1) and (new_guess_validation(guess, guesses) == 1):
            if guess == ran_num:
                # Correct number is guessed. Game ends
                print("Success! You guessed the correct number!")
                return 1
            elif guess < ran_num:
                # provides clue to guess higher if guess is lower than
                # random number
                guesses.append(guess)
                print("Guess higher!")
                # incorrect number is guessed. Tries is decremented by 1
                tries -= 1
            else:
                # provides clue to guess lower if guess is lower than
                # random number
                guesses.append(guess)
                print("Guess lower!")
                # incorrect number is guessed. Tries is decremented by 1
                tries -= 1
        if tries == 0:
            # return failure message when user runs out of tries
            print("You have failed to guess the number")
            return 0


def guess_random_num_linear(tries, start, stop):
    # random number between start and stop is selected
    ran_num = random.randint(start, stop)
    print("The number for the program to guess is", ran_num)
    # loops through the range of the start and stop inputs
    for num in range(start, stop):
        print("The program is guessing...", num)
        # correct number is selected. program ends
        if num == ran_num:
            print("The program guessed the correct number")
            return 1
        # incorrect number is selected. Tries is decremented by 1
        else:
            tries -= 1
            print("Number of tries left:", tries)
        # game ends when program runs out of tries
        if tries == 0:
            print("Game Over: The program ran out of tries")
            return 0


def guess_random_num_binary(tries, start, stop):
    # random number between start and stop is selected
    ran_num = random.randint(start, stop)
    print("Random number to find:", ran_num)
    # sets the lower bound to the start parameter
    lower_bound = start
    # sets the upper bound to the start parameter
    upper_bound = stop

    # Loop continues unitl tries not equal to 0
    while tries != 0:
        # sets pivot at the halfway point between start and stop
        pivot = (lower_bound + upper_bound) // 2
        print("the program is guessing", pivot)

        if pivot == ran_num:
            # program selected the correct number
            # the game ends wih success message
            print("The program guessed the correct number!")
            return pivot
        if pivot > ran_num:
            # # if pivot is greater than random guess_random_number
            # all numbers above pivot are removed from possible selection
            # by setting the upper bound to pivot minus 1
            print("Guessing Lower")
            upper_bound = pivot - 1
            tries -= 1
        else:
            # # if pivot is less than random guess_random_number
            # all numbers below pivot are removed from possible selection
            # by setting the lower bound to pivot plus 1
            print("Guessing higher")
            lower_bound = pivot + 1
            tries -= 1
    # failure message is returned when program runs out of tries
    print("Your program failed to find the number")


def random_number_alg_choice():
    # prompts user to input the number of tries, start, and stop values
    tries = int(input("Input the amount of tries: "))
    start = int(input("Input the start number: "))
    stop = int(input("Input the stop number: "))

    while True:
        print("""
            === Guessing  Game   ===         
    
        ------------------------------------------
        | 1.    Random Guess     | 2.    Linear Search      |
        
        ------------------------------------------
        | 3.    Binary Search               
        ------------------------------------------ """)
        # user selects the algorithm to use for the game
        alg_choice = input("What do you choose: ")

        if alg_choice == "1":
            # Runs the random_guess function
            print("You have chosen 1. Random Guess")
            guess_random_number(tries, start, stop)
            break
        elif alg_choice == "2":
            # runs the Linear Search Function
            print("You have chosen 2. Linear Search")
            guess_random_num_linear(tries, start, stop)
            break
        elif alg_choice == "3":
            # runs the binary search function
            print("You have chosen 3. Binary Search")
            guess_random_num_binary(tries, start, stop)
            break
        else:
            # prompts error message if invalid choice
            print("Invalid Choice")


def gambling_game():
    # player starts out with 10 dollars
    player_money = 10
    print("You have", player_money, "dollars")
    # game continues to run until play loses all their player_money
    # or play makes more than 50 dollars
    while player_money > 0 and player_money < 50:
        print("-------------------------")
        # player chooses if program will win or not
        choice = int(
            input("Do you think the computer will guess the number? (1 = yes / 0 = no: "))
        # validatoin that player chooses 1 or 0 (onlly)
        if (choice == 0 or choice == 1) != True:
            print("Invalid choice")
            continue
        print("You have chosen", choice)
        # player inputs how much they want to bet
        bet = int(input("How much do you bet? (Only whole numbers): "))
        print("You have bet", bet, "dollars")
        # error is returned if player bets more money than they have
        if bet > player_money:
            print("You don't have that much money")
            continue
        # random number linear game is called
        # game results in a 1 if program wins
        # game results in a 0 if program loses
        game = guess_random_num_linear(1, 0, 1)
        print("The game result is..... ", game)
        print("You chose", choice)

        # if player choses the same game result their money
        # increases by the amount they bet
        if game == choice:
            print("You won", (bet), "dollars!")
            player_money += (bet)
        # if player did not chose the game outcome, their money decreases
        # by the amount they bet
        else:
            print("You lost", bet, "dollars")
            player_money -= bet
        print("You now have", player_money, "dollars")
    # display message that player lost if money = 0
    if player_money <= 0:
        print("You lost all your money")
    # display message that player wins if money >  50
    elif player_money > 50:
        print("You won all the money!")

# guess_random_num_binary(5, 0, 100)

# guess_random_number(5, 0, 10)

# number_validation(2, 0, 10)

# guess_random_num_linear(5, 0, 10)

# random_number_alg_choice()


gambling_game()

# game = guess_random_num_linear(1, 0, 2)
# print("The game is", game)
