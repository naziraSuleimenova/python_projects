import random

print("* Welcome to the Number Guessing Game! *")
print("I am thinking of a number between 1 and 10.")

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = input("Enter you guess: ")

    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)

    attempts += 1

    if guess == secret_number:
       print(f"Correct. You guessed the number in {attempts} attempts! You win.")
       break

    elif guess < secret_number:
       print("Too low. Try again!")

    else:
       print("Too high. Try again!")