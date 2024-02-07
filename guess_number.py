def guess_number(number, max_guesses):
    print("I'm thinking of a number...")
    guesses_left = max_guesses
    while guesses_left > 0:
        guess = input(f"What number am I thinking of? You have {guesses_left} guesses left. (Enter 'q' to quit) ")
        
        if guess.lower() == 'q':
            print(f"The number was {number}.")
            break
        
        try:
            guess = int(guess)
            if guess == number:
                print("Congratulations! You guessed the right number.")
                break
            elif guess < number:
                print("Sorry! Your guess is too low.")
            else:
                print("Sorry! Your guess is too high.")
            guesses_left -= 1
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
    else:
        print(f"Sorry, you've run out of guesses. The number was {number}.")

# Call the function with the number and maximum number of guesses
guess_number(10, 5)
