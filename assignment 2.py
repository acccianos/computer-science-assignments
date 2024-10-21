num1 = input('Enter a number: ')
num1 = int(num1)
num2 = input('Enter a second number: ')
num2 = int(num2)
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
    
print(' ')

num3 = input('Enter a number under 20: ')
num3 = int(num3)
if num3 >= 20:
    print('Too high')
else:
    print('Thank you')
    
print(' ')
    
num4 = input('Enter a number between 10 and 20: ')
num4 = int(num4)
if num4 < 10 or num4 > 20:
    print('Incorrect answer')
else:
    print('Thank you')

print(' ')

colour = input('Enter your favourite colour: ')
if colour == 'Red' or colour == 'red' or colour == 'RED':  
    print('I like red too')
else:
    print("I don't like", colour, 'I like red')
    
print(' ')

rain = input('Is it raining?: ')
rain.lower()
if rain == 'yes':
    wind = input('Is it windy?: ')
    wind.lower()
    if wind == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
   print('Enjoy your day')

print(' ')

age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trick-Or-Treating')

print(' ')

num5 = input('Enter 1, 2 or 3: ')
num5 = int(num5)
if num5 == 1:
    print('Thank you')
elif num5 == 2:
    print('Well done')
elif num5 == 3:
    print ('Correct')
else:
    print('Error message')
  