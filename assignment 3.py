num1 = input('Enter a number: ')
num1 = int(num1)
if num1% 5 ==0:
    print('Hello')
else:
    print('Goodbye')
    
print(' ')

num2 = input('Enter an amount of units for an electricity bill: ')
num2 = float(num2)
if num2 > 100 and num2 <= 200:
    num3 = num2 - 100
    num3 = float(num3)
    num4 = num3 * 5
    num4 = float(num4)
elif num2 > 200:
    num5 = num2 -200
    num5 = float(num5)
    num6 = num5 * 10
    num6 = float(num6)
    bill = num6 + 500
    bill = float(bill)
while num2 > 100 and num2 <= 200:
    print('€',num4 / 100)
    break
while num2 > 200:
    print('€',bill / 100)
    break

print(' ')

cost = input('Enter the cost for a bike: ')
cost = float(cost)
if cost >= 1000:
    vat = cost * 1.15
    vat = float(vat)
    tax = cost * 0.15
    tax = float(tax)
elif cost >=500 and cost < 1000:
    vat2 = cost * 1.1
    vat2 = float(vat2)
    tax2 = cost * 0.1
    tax2 = float(tax2)
elif cost < 500:
    vat3 = cost * 1.05
    vat3 = float(vat3)
    tax3 = cost * 0.05
    tax3 = float(tax3)
while cost >=1000:
    print('The bike is €', cost, 'before tax.')
    print('The tax is €',tax)
    print('The bike is €', vat, 'after tax.')
    break
while cost >=500 and cost < 1000:
    print('The bike is €', cost, 'before tax.')
    print('The tax is €',tax2)
    print('The bike is €', vat2, 'after tax.')
    break
while cost < 500:
    print('The bike is €', cost, 'before tax.')
    print('The tax is €',tax3)
    print('The bike is €', vat3, 'after tax.')
    break


print(' ')

num7 = input('Enter a number: ')
num7 = int(num7)
num8 = input('Enter another number: ')
num8 = int(num8)
num9 = input('Enter another number: ')
num9 = int(num9)
if num9 > num7 and num9 > num8:
    print(num9)
elif num8 > num7 and num8 > num9:
    print(num8)
elif num7 > num8 and num7 > num9:
    print(num7)

print(' ')

letter = input('Enter a letter: ')
letter = letter.lower()
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('vowel')
else:
    print('not a vowel')

print(' ')

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

numero1 = int(input('Enter a number: '))
numero2 = int(input('Enter a number: '))
print(numero1, '+', numero2, '=', (numero1 + numero2))

print(' ')



