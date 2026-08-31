import random

words = ["python", "computer", "coding", "program", "developer"]

word = random.choice(words)
guessed = []
wrong = 0

while wrong < 6:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong += 1
        print("Wrong guess. Attempts left:", 6 - wrong)

if wrong == 6:
    print("You lost!")
    print("The word was:", word)