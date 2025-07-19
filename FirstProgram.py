import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum number of guesses
max_guesses = 3
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print(f"You have {max_guesses} attempts to guess it.\n")

# Game loop
while attempts < max_guesses:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If all attempts used
if attempts == max_guesses and guess != secret_number:
    print(f"😢 Sorry, you lost. The number was {secret_number}.")
