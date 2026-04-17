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
print(word)

word_len = len(word)
placeholder = ''
for letter in word:
    placeholder += '_'
print(f'Your word to guess have {placeholder}({word_len}) letters.')

guessed = []
game_over = False
lives = 5

while not game_over:
    guess = input('Choose a letter to guess: ')

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

    if '_' not in display:
        game_over = True
        print('You win.')

    if lives == 0:
        game_over = True
        print(f'You lose, the word is "{word}".')

