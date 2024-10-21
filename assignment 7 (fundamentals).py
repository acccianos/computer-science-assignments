PI = 3.14
radius = float(input('Give the radius for a circle: '))#
area = PI * (radius * radius)
print(area)

print(' ')

heightcm = int(input('What is your height(in cm)?: '))
heightinch = float(heightcm / 2.54)
heightfoot = int(heightinch // 12)
footremainder = int(heightinch % 12)
print(round(heightinch, 4), 'inches and', round(heightfoot, 1),'"', footremainder, 'in feet')

print(' ')

n1 = int(input('Give a value for n: '))
print(pow(n1, 2),'\n',pow(n1, 3),'\n',pow(n1, 4))

print(' ')

tri1 = float(input('Give 1 side of a triangle: '))
tri2 = float(input('Give another side of a triangle: '))
area = (tri1 * tri2) / 2
print(area)

print(' ')

name = input('Enter your name: ')
class1 = input('Enter your class: ')
age = input('Enter your age: ')
print(name, class1, age,'\n',name,'\n',class1,'\n',age)

print(' ')

n2 = int(input('Enter a single digit number: '))
print((n2),(n2 + 1),(n2 + 2))

print(' ')

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))
num3 = float(input('Enter a number: '))
print(num1, num2, num3)
print((num2 + num1), (num2 + num3), num3)





