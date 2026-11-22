"""Run an interactive higher/lower number guessing game.

Input:
    A lower bound, an upper bound, and repeated guesses.

Process:
    Validate the bounds and guesses, select a random target number,
    provide guess feedback, and repeat until the target is found.

Output:
    Prompts, validation messages, guess feedback, and success messages.
"""

# === Imports ===
from random import randint


# === Main Function ===
def main() -> None:
    """Run the optional higher/lower game practice program."""

    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter an upper bound: "))

    while lower >= upper:
        print("The lower bound must be less than the upper bound.")
        lower = int(input("Enter a lower bound: "))
        upper = int(input("Enter an upper bound: "))

    target = randint(lower, upper)

    guess = int(input("Enter a guess between the selected bounds: "))
    while guess < lower or guess > upper:
        print("That guess is outside the selected bounds.")
        guess = int(input("Enter another guess: "))

    while guess != target:
        if guess < target:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        guess = int(input("Enter a guess between the selected bounds: "))
        while guess < lower or guess > upper:
            print("That guess is outside the selected bounds.")
            guess = int(input("Enter another guess: "))

    print("Congratulations! You guessed the correct number.")


# === Main Guard ===
if __name__ == "__main__":
    main()


