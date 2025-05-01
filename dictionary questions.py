#g
sentence = input('Enter a sentence: ')
sentence.lower()
chars = {}
vowel = 'aeiou'
for char in sentence:
    if char in vowel:
        chars[char] = chars.get(char, 0) + 1
print(chars)
print()

#h
sentence = input('Enter a sentence: ')
sentence.lower()
chars = {'vowels' : 0, 'consonants' : 0}
vowel = 'aeiou'
for char in sentence:
    if char in vowel:
        chars['vowels'] += 1
    elif char not in vowel and char.isalpha() == True:
        chars['consonants'] += 1
print(chars)
print()

#i
sentence = input('Enter a sentence: ')
chars = {}
words = sentence.split()
for char in words:
        if char in chars:
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1
print(chars)
print()