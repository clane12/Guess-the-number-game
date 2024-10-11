import random

from art import logo

game = True
while game:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100")

    # this is to get the random number
    def random_number():
        thinking_num = random.randint(1, 100)
        return thinking_num
    random_num = random_number()
    print(random_num)

    # let the user choose the difficult option
    difficulty = input("Choose the difficulty, type 'easy' or 'hard' : ").lower()

    # if difficulty is easy user will get 10 attempts and if difficulty is hard user gets 5 attempts.
    def diff(difficulty):
        if difficulty == "easy":
            print("you have 10 attempts to guess the number")
        elif difficulty == "hard":
            print("you have 5 attempts to guess the number")

    diff(difficulty)

    # this is to actually create the number of attempts user will get
    def attempt_numb():
        if difficulty == "hard":
            n = 5
        elif difficulty == "easy":
            n = 10

        return n
    # this is to create an attempt variable
    attempts = attempt_numb()

    # created another variable called attempts left
    attempts_left = attempts

    # created a while loop to loop through the rest of the attempts to guess the number
    while attempts_left > 0:
        guess = int(input("Make a guess: "))
        # if the guessed number is right you won, if not you attempts will be decreased by 1.
        def guessed(guessed_no):
            global attempts_left
            if guess == random_num:
                print(f"You guessed correct {guess} was the answer, you won")
                attempts_left = 0
            elif guess <= random_num:
                print("guessed Too low")
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"Try again, you have {attempts_left} attempts left")
            elif guess >= random_num:
                print("guessed to high")
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"Try again, you have {attempts_left} attempts left")


        guessed(guess)
        # This is when user loses all their attempts
        if attempts_left == 0 and guess != random_num:
            print("You've run out of guesses, you lose.")

    # give the user the chance to choose if he wants to play the game again or quit.
    play_again = input("Quit the game press 'n' or play again press 'y': ")
    if play_again == "y":
        print("\n" * 20)
        continue
    elif play_again == "n":
        game = False
        print("Thank you for playing, have a good day.")
    else:
        print("you clicked something wrong, the game will quit.")
        game = False






