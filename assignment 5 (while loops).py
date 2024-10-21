total = 0
while total < 50:
    num = int(input('Enter a number: '))
    total = total + num
print('The total is:', total,)

print(' ')

num1 = 0
while num1 < 5:
    num1 = int(input('Enter a number: '))
print('The last number you entered was a', num1)

print(' ')

total1= 0
ans1 = 0
response1 = 'y'
num2 = int(input('Enter a number: '))
while response1 == 'y':
    num3 = int(input('Enter another number: '))
    ans1 = num2 + num3
    total1 = total1 + ans1
    response1 = input('Add another number? [Y for yes]: ')
print(total1)

print(' ')

count1 = 1
name1 = input('Name someone to invite to a party: ')
print(name1, 'has been invited')
response2 = input('Do you want to invite anyone else? (Y/N): ')
while response2 == 'y':
    name2 = input('Name the next person: ')
    print(name2, 'has been invited')
    count1 += 1
    response2 = input('Do you want to invite anyone else? (Y/N): ')
print(count1, 'people have been invited')

print(' ')

copnum = 50
response3 = 0
attempts = 0
while response3 != 50:
    response3 = int(input('Guess the number: '))
    if response3 < copnum:
        print('Too low')
    elif response3 > copnum:
        print('Too high')
    attempts = attempts + 1
print('Good job king, it only took', attempts, 'attempts')

print(' ')

response4 = 0
while response4 == 0:
    num4 = int(input('Enter a number between 10 and 20: '))
    if num4 > 20:
        print('Too high')
    elif num4 < 10:
        print('Too low')
    elif num4 > 10 and num4 < 20:
        response4 += 1
        print('Good job kingaling')

print(' ')

num5 = 10
num6 = 9
print('There are',num5, 'green bottles hanging on the wall,', num5, 'green bottles hanging on the wall, and if 1 green bottle should accidentally fall -')
while num5 > 0:
    response5 = int(input('How many green bottles will be hanging on the wall?: '))
    if response5 != num6:
        print('No king, try again')
    elif response5 == num6:
        num5 -= 1
        num6 -= 1
        print('There are',num5, 'green bottles hanging on the wall,', num5, 'green bottles hanging on the wall, and if 1 green bottle should accidentally fall -')
print('There are no more green bottles hanging on the wall')







    