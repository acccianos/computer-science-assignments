name1 = input('Enter your first name: ')
name2 = input('Enter your surname: ')
print('Hello', name1, name2)

print(' ')

print('What do you call a bear with no teeth? A gummy bear💀💀💀💀')

print(' ')

num1 = input('Enter a number:')
num1 = int(num1)
num2 = input('Enter another number:')
num2 = int(num2)
num3 = num1 + num2
num3 = int(num3)
print('Your first number and second number add up to:', num3)

print(' ')

slices = input('Imagine you have a cheeky pizza in front of you. Tell me how many slices should be on the pizza:')
slices = int(slices)
munched = input('Now imagine you decided to munch on the pizza. Tell me how many slices you scarfed:') 
munched = int(munched)
left = slices - munched
left = int(left)
print('Now you have', left, 'slices left')

print(' ')

num4 = input('Enter a number:')
num4 = int(num4)
num5 = input('Enter another number:')
num5 = int(num5)
num6 = input('Enter another number:')
num6 = int(num6)
num7 = num4 + num5
num7 = int(num7)
num8 = num7 * num6
num8 = int(num8)
print(num4, 'plus', num5, 'then multplied by', num6, 'is:', num8)

print(' ')

name3 = input('Enter your first name again: ')
num9 = input('How old are you?:')
num9 = int(num9)
num10= num9 + 1
print('Next year, you,', name3, 'will be', num10, 'years old')

print(' ')

bill = input('Imagine you went to a diner for a munch. Tell me what would the total bill would be:')
bill = float(bill)
diners = input('Now tell me how many diners were with you:') 
diners = float(diners)
each = bill / diners
each = float(each)
print('Split evenly, each diner would pay', each, 'euro each')

print(' ')

days = input('Tell me a number of days:')
days = int(days)
hours = days * 24
hours = int(hours)
mins = days * 1440
mins = int(mins)
secs = mins * 60
print('There are', hours, 'hours,', mins, 'minutes and', secs, 'seconds in', days, 'days')

print(' ')

kg = input('Tell me a weight in kilograms (without kg symbol):')
kg = float(kg)
lbs = kg * 2.204
lbs = float(lbs)
print('There are', lbs, 'pounds in', kg, 'kilograms')

print(' ')

num11 = input('Pick a number over 100:')
num11 = int(num11)
num12 = input('Now pick a number under 10:')
num12 = int(num12)
num13 = num11 / num12
num13 = float(num13)
print(num12, 'goes into', num11, num13, 'times')
