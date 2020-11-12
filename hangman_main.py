import random

with open("words.txt", 'r') as f:
    words = f.readlines()
    print(words)

word = words[random.randint(0, len(words))].strip('\n')

allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")

    guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())
    
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True

    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"\nYou found the word! It was {word}")
else:
    print(f"\nGame Over! The word was {word}")