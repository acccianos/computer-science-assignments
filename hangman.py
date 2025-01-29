word = 'ca  t'
lives = 7
count = (len(word))
blanks = (count * '-')
answer = '-' * count
guessed = ''
letters = 'abcdefghijklmnopqrstuvwxyz'
alphablanks = '-' * 26
dash = '-'
print('Hangman game')
for c in range(0, count):
    if word[c] == ' ':
        blanks += ' '
    else:
        blanks += blanks[c]
blanks = blanks[count:(count * 2)]
while blanks != word and lives > 0:
    guess = str(input('Guess a letter: '))
    guess = guess.lower()
    if guess in guessed:
        print('Already guessed')
    guessed += guess
    if guess in word:
        for a in range(0, count):
            if word[a] == guess:
                answer += guess
            elif answer[a] != '-':
                answer += answer[a]    
            else:
                 answer += blanks[a]
    else:
        lives -= 1
    if lives == 7:
        print(' +---+')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
    if lives == 6:
        print(' +---+')
        print(' |   |')
        print('     |')
        print('     |')
        print('     |')
    elif lives == 5:
        print(' +---+')
        print(' |   |')
        print(' o   |')
        print('     |')
        print('     |')
    elif lives == 4:
        print(' +---+')
        print(' |   |')
        print(' o   |')
        print('/    |')
        print('     |')
    elif lives == 3:
        print(' +---+')
        print(' |   |')
        print(' o   |')
        print('/|   |')
        print('     |')
    elif lives == 2:
        print(' +---+')
        print(' |   |')
        print(' o   |')
        print('/|\  |')
        print('     |')
    elif lives == 1:
        print(' +---+')
        print(' |   |')
        print(' o   |')
        print('/|\  |')
        print('/    |')
    elif lives == 0:
        print(' +---+')
        print(' |   |')
        print(' o   |')
        print('/|\  |')
        print('/ \  |')
    guessed += guess
    for b in range(0, 26):
        if letters[b] == guess:
            alphablanks += guess
        elif alphablanks[b] != '-':
            alphablanks += alphablanks[b]
        else:
            alphablanks += dash
    alphablanks = alphablanks[26:52]
    print('Lives =', lives)
    print('Letters guessed:', alphablanks)
    if guess in word:
        answer = answer[count:(count * 2)]
    print('Word:', answer)
    print()
    if word == answer:
        print('Good job')
        break
    elif lives == 0:
        print('You fail, the word was', word)
        break