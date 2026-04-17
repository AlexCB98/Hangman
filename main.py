import random

words = [
    "cat",
    "dog",
    "sun",
    "book",
    "tree",
    "car",
    "fish",
    "ball",
    "milk",
    "home"
]

word = random.choice(words)

placeholder = ''
for letter in word:
    placeholder += '_'

guessed = []
game_over = True
lives = 5

while not game_over:
    guess = input('Choose a letter: ')

    display = ''

    if guess in guessed:
        display += guess
    else:
        guessed.append(guess)

    for letter in guessed:
        if letter in guessed:
            display += letter
        else:
            display += '_'

    if '_' not in display:
        game_over = True
        print('You win.')

    if lives == 0:
        game_over = True
        print(f'You lose, the word is "{word}".')

