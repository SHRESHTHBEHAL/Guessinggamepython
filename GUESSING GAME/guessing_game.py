import random

def guessing_game():
    print("Welcome to the Python Number Guessing Game!")
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    
    if difficulty == "easy":
        max_attempts = 15
        secret_number = random.randint(1, 50)
    elif difficulty == "medium":
        max_attempts = 10
        secret_number = random.randint(1, 100)
    else:  # hard
        max_attempts = 5
        secret_number = random.randint(1, 200)
    
    attempts = 0
    print(f"Guess a number between 1 and {secret_number * 2 if difficulty == 'hard' else 100}.")
    print(f"You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("⚠️ Please enter a number!")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"🎉 You won in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("⬆️ Higher!")
        else:
            print("⬇️ Lower!")
        
        print(f"Attempts left: {max_attempts - attempts}")
    else:
        print(f"😢 Game over! The number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()