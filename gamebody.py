import random

def start_game(name):
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("__GAME INSTRUCTIONS__")
    print("1. Guess a number with 2, 3, or 4 digits based on difficulty.")
    print("2. You'll have a limited number of attempts.\n")
    print("LEVELS:")
    print("1. Easy     [2 digits, 20 attempts]")
    print("2. Moderate [3 digits, 15 attempts]")
    print("3. Hard     [4 digits, 10 attempts]")

    while True:
        try:
            level = int(input("Enter your preferred level (1-3): "))
            if level not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Invalid input. Please enter 1, 2, or 3.")

    if level == 1:
        secret = random.randint(10, 99)
        chances = 20
    elif level == 2:
        secret = random.randint(100, 999)
        chances = 15
    else:
        secret = random.randint(1000, 9999)
        chances = 10

    print(f"\nGuess the number between {10**(level)} and {10**(level+1) - 1}")
    attempts = 0
    guessed = False

    while attempts < chances:
        try:
            guess = int(input(f"\n{name}'s guess: "))
            attempts += 1
            remaining = chances - attempts

            if guess < secret:
                print("🔻 Too low!")
            elif guess > secret:
                print("🔺 Too high!")
            else:
                print("🎉 Hurrah! You've guessed the correct number!")
                guessed = True
                break

            print(f"⏳ Attempts left: {remaining}")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    if not guessed:
        print(f"\n😢 Sorry {name}, you've used all {chances} attempts.")
        print(f"The correct number was {secret}.")

def main():
    name = input("Your name: ").strip().capitalize()
    while True:
        start_game(name)
        choice = input("\n🔁 Do you want to play again? (Yes/No): ").lower()
        if choice not in ['yes', 'y']:
            print(f"\n👋 Thanks for playing, {name}!")
            print("Visit Again!!")
            break

if __name__ == "__main__":
    main()
