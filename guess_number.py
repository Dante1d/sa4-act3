def guess_number(number):
    print("I'm thinking of a number...")
    while True:
        guess = input("What number am I thinking of? (Enter 'q' to quit) ")
        
        if guess.lower() == 'q':
            print(f"The number was {number}.")
            break
        
        try:
            guess = int(guess)
            if guess == number:
                print("Congratulations! You guessed the right number.")
                break
            else:
                print("Sorry! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

# Call the function with the number
guess_number(10)
