tri1 = float(input('Give 1 side of a triangle: '))
tri2 = float(input('Give another side of a triangle: '))
tri3 = float(input('Give another side of a triangle: '))
if tri1 != tri2 and tri2 != tri3 and tri1 != tri3:
    print('scalene')
elif tri1 != tri2 and tri2 == tri3 and tri1 != tri3:
    print('icoseles')
elif tri1 != tri2 and tri2 != tri3 and tri1 == tri3:
    print('icoseles')
elif tri1 == tri2 and tri2 != tri3 and tri1 != tri3:
    print('icoseles')
elif tri1 == tri2 and tri2 == tri3 and tri1 == tri3:
    print('equilateral')
    
print(' ')

fouror8 = input('Enter a number that ends with 4 or 8: ')
if fouror8[-1] == '4':
    print('Ends with 4')
elif fouror8[-1] == '8':
    print('Ends with 8')
else:
    print('Ends with neither')
    
print(' ')

n = int(input('Enter a number above 20: '))
for n in range(11, n + 1):
    print(n)
    if (n % 3 == 0) and (n % 7 == 0):
        print('Tipsy Topsy')
    elif (n % 7 == 0):
        print('Topsy')
    elif (n % 3 == 0):
        print('Tipsy')

m = int(input('Enter a number above 1: '))
nm = int(input('Enter a number to divide: '))
for m2 in range(1, m + 1):
    if m2 % nm == 0:
        if m2 % 2 == 0:
            print(m2)
            print('Even')
        else:
            print(m2)
            print('Odd')

print(' ')

n2 = int(input('Enter a number: '))
powa = 0
for n2 in range(1, n2 + 1, 2):
   powa = (n2 ** 2) + powa
print(powa)

print(' ')

celsius = 0
fahren = 0
temp = int(input('Enter a temperature: '))
unit = input('What unit is the temperature in? (c for Celsius or f for Fahrenheit): ')
unit.lower()
if unit == 'f':
    celsius = (temp - 32) * (5/9)
    print(celsius,'°C')
elif unit == 'c':
    fahren = ((9 / 5 )* temp) + 32
    print(fahren,'°F')

print(' ')

degcel = float(input('Enter a temperature in celsius: '))
if degcel < -273.15:
    print('Invalid as it is below absolute zero')
elif degcel == -273.15:
    print('The temperature is absolute zero')
elif degcel > -273.15 and degcel < 0:
    print('The temperature is below freezing')
elif degcel == 0:
    print('The temperature is at freezing point')
elif degcel > 0 and degcel < 100:
    print('The temperature is at normal range')
elif degcel == 100:
    print('The temperature is at boiling point')
elif degcel > 100:
    print('The temperature is above boiling point')