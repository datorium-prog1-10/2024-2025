number_of_guesses = 0

while True:
    number_guess = int(input("Guess a number between 1 and 100: "))
    number_of_guesses += 1

    if number_guess == number_target:
        print(f"You won after {number_of_guesses}")
        break
    elif number_guess < number_target:
        print("Guess higher")
    elif number_guess > number_target:
        print("Guess lower")
