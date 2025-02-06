import random
randomwords = ['microphone', 'conventional', 'attatchment', 'nationalism', 'radiation', 'encyclopedia', 'misunderstanding', 'uncharacteristically', 'philosophical', 'counterproductive', 'incomprehensible', 'unbelievably', 'discombobulated', 'transcendental', 'disproportionately', 'unquestionably', 'revolutionary', 'individualistically', 'unintentionally', 'uncontrollably', 'extraordinarily', 'unrecognizable', 'unpredictable', 'incontrovertible', 'unbelievably']

word = random.choice(randomwords)
lives = 7
count = (len(word))
blanks = '-' * count
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
    print()
    print('Word:', answer)
    print()
    if word == answer or lives == 0:
        if word == answer:
            print('Good job')
        elif lives == 0:
            print('You fail, the word was', word)
        playagain = input("Play again? ('y' for yes): ")
        playagain = playagain.lower()
        if playagain == 'y':
            print('Okay chat')
            word = random.choice(randomwords)
            lives = 7
            count = (len(word))
            blanks = '-' * count
            answer = '-' * count
            guessed = ''
            alphablanks = '-' * 26
            for c in range(0, count):
                if word[c] == ' ':
                    blanks += ' '
                else:
                    blanks += blanks[c]
            blanks = blanks[count:(count * 2)]
        else:
            print('Goodbye')
            break