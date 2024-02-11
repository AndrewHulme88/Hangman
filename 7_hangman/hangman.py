import random
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

display = []

for _ in range(word_length):
    display += "_"

end_of_game = False

print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is incorrect. You have {lives} tries remaining.")
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game == True
            print("You lose")
            exit()

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

   