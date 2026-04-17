import random

from hangman_words import words
from hangman_ascii import stages,logo

print(logo)

word = random.choice(words)

word_len = len(word)
placeholder = ''
for letter in word:
    placeholder += '_'
print(f'Your word to guess have {placeholder}({word_len}) letters.')

guessed = []
game_over = False
lives = 6

while not game_over:
    print(f"Lives: {'❤️' * lives}")
    guess = input('Choose a letter to guess: ').lower()

    display = ''

    if guess not in guessed:
        guessed.append(guess)
    else:
        print(f'You already guessed: "{guess}".')

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += '_'

    print(display)

    if guess not in word:
        lives -= 1
        print('You lost a life.')

    if lives == 0:
        game_over = True
        print(f"Game Over. The word was: {word}")

    if '_' not in display:
        game_over = True
        print('You win.')

    print(stages[lives])


