temp1 = float(input('Give the temperature for Monday: '))
temp2 = float(input('Give the temperature for Tuesday: '))
temp3 = float(input('Give the temperature for Wednesday: '))
temp4 = float(input('Give the temperature for Thursday: '))
temp5 = float(input('Give the temperature for Friday: '))
temp6 = float(input('Give the temperature for Saturday: '))
temp7 = float(input('Give the temperature for Sunday: '))
print((temp1+temp2+temp3+temp4+temp5+temp6+temp7)/7)

print(' ')

x = float(input('Give x: '))
y = float(input('Give y: '))
z = float(input('Give z: '))
print((4 * pow(x, 4)) + (3 * pow(y, 3)) + (9 * z) + (6 * 3.14))

print(' ')

secs = int(input('Give an amount of seconds: '))
mins = int(secs // 60)
print(mins, 'minutes and', (secs % 60), 'seconds')

print(' ')

hour = int(input('Give an hour between 1 and 12: '))
ahead = int(input('Give how many hours ahead: '))
time = int(hour + ahead)
while time > 12:
    time = time - 12
print('In', ahead, 'hours, it will be', (time), "o'clock")

print(' ')

digit = str(input('Give a 3 digit number: '))
print(digit[::-1])

print(' ')

day = int(input('Enter a day(number): '))
month = int(input('Enter a month(number): '))
month = month * 30
print('This is day', (day + month), 'of  the current year')