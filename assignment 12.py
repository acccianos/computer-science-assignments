num1 = 1
n1 = int(input('Enter a number: '))
while num1 != n1:
    num1 += 1
    if num1 % 5 != 0:
        print(num1)

print()

num2 = 1
iteration = 0
n2 = int(input('Enter a number: '))
n2 = n2 ** 2
while iteration < 50:
    while num2 != n2 + 1:
        num2 += 1
        print(num2 - 1)
        iteration = iteration + 1
        break

print()

for int3 in range(3, 29):
    if int3 % 2 != 0 and int3 % 5 != 0:
        print(int3)

print()

range1 = int(input('Enter lower range number: '))
range2 = int(input('Enter higher range number: '))
multiple = int(input('Choose multiple to ignore: '))
for int4 in range(range1, range2):
    if int4 % 2 != 0 and int4 % multiple != 0:
        print(int4)

print()

for int5 in range(50, 20, -1):
    if int5 % 3 != 0:
        print(int5)

print()

for int6 in range(12, -14, -1):
    if int6 % 2 == 0:
        print(int6)









