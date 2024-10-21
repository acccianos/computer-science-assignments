name1 = input('Enter your name: ')
num1 = int(input('Enter a number: '))
for name in range(num1):
    print(name1)

print(' ')

name2 = input('Enter your name: ')
num2 = int(input('Enter a number: '))
for name in range(num2):
    for character in name2:
        print(character)

print(' ')

num3 = int(input('Enter a number between 1 and 12: '))
for num4 in range(13):
    print(num3, 'x', num4, '=', num4 * num3)
    
print(' ')

num5 = int(input('Enter a number below 50: '))
for num6 in range(50, num5, -1):
    print(num6)
print(num5)

print(' ')

name3 = input('Enter your name: ')
num7 = int(input('Enter a number below 10: '))
if num7 < 10:
    for name in range(num7):
        print(name3)
else:
    for name in range(3):
        print('Too high')

print(' ')

total = 0
for totalnum in range(5):
    num8 = int(input('Enter a number: '))
    inc1 = input('Do you want this number included? (Y/N): ')
    inc1.lower()
    if inc1 == 'yes' or inc1 == 'y':
        total += num8
print(total)

print(' ')

dir1 = input('What direction do you want to count? (Up/Down):')
dir1.lower()
if dir1 == 'up':
    num9 = int(input('Enter the top number: '))
    for num10 in range(1, num9 +1):
        print(num10)
elif dir1 == 'down':
        num11 = int(input('Enter a number below 20: '))
        for num12 in range(num11, 0, -1):
            print(num12)

print(' ')

num13 = int(input('How many people do you want to invite to a party?: '))
if num13 < 10:
    for inv in range(num13):
        name4 = input('Enter each of their names: ')
        print(name4, 'has been invited')
else:
    print('Too many people')