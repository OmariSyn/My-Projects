import random

# Ask for the user's name first
user_name = input("Hello! What is your name? ")
print(f"Welcome to the game, {user_name}!")

# Setup the secret number
secret_number = random.randint(1, 10)

# --- PART 1: The Guessing Game (for loop) ---
user_won = False

for tries in range(1, 6):
    guess = int(input(f"Attempt {tries}: Please guess a number between 1 and 10: "))
    
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Correct! It took you {tries} tries to guess correctly.")
        user_won = True
        break

if not user_won:
    print(f"Out of attempts! The secret number was {secret_number}.")

# --- PART 2: The Incrementer (while loop) ---
print("\n--- Incrementing the Correct Guess ---")

count = 1
current_value = secret_number

while count <= 5:
    current_value += 1  # Increment the value by one
    print(f"Iteration {count}: The incremented value is {current_value}")
    count += 1

# Final closing statement
print(f"\nCongratulations, {user_name}! You finished the program.")