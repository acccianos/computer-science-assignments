numcount = 0
total = 0
int1 = input('Enter an integer: ')
while int1 != "":
    numcount = numcount + 1
    int1 = int(int1)
    total = int(total)
    total = int1 + total
    average = total / numcount
    int1 = input('Enter an integer: ')
print('The average of those integers are', average)

print()

numcount2 = 0
total2 = 0
average2 = 0
int2 = int(input('Enter an integer: '))
while int2 >= 0:
    numcount2 = numcount2 + 1
    total2 = int(total2)
    total2 = int2 + total2
    average2 = total2 / numcount2
    int2 = int(input('Enter an integer: '))
print('The average of those integers are', average2)

print()

numcount3 = 0
total3 = 0
finalgrade = 0
grades = int(input('Enter your test grade: '))
while grades >= 0:
    numcount3 = numcount3 + 1
    total3 = int(total3)
    total3 = grades + total3
    finalgrade = total3 / numcount3
    grades = int(input('Enter your next grade: '))
if finalgrade >= 90 :
    print('You got an A')
elif finalgrade <= 89 and finalgrade >= 80:
    print('You got a B')
elif finalgrade <= 79 and finalgrade >= 70:
    print('You got a C')
elif finalgrade <= 69 and finalgrade >= 60:
    print('You got a D')
elif finalgrade <= 59:
    print('You got an F')
    
print()

int3 = int(input('Enter a number: '))
while int3 > -1:
    print(int3)
    int3 = int3 - 1
    
print()

int4 = int(input('Enter a number: '))
for int4 in range(2, int4 + 1):
    if int4 % 2 == 0:
        print(int4)