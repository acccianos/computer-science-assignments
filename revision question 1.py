list1 = []
number = ''
mean = 0
median = 0
frequency = 0
frequencylist = []
mode = 0
modelist = []


while number != 'q':
    number = input("Enter a whole number ('q' to end input): ")
    if number != 'q':
        if number.isdigit() == True:
            list1.append(int(number))
        else:
            print('Not a whole number')
list1.sort()
print()
print('Sorted list: ', list1)
print()


for a in range(0, len(list1)):
    mean += list1[a]
mean /= len(list1) 
if mean.is_integer() == True:
    print('Mean is', int(mean))
else:
    print('Mean is', mean)

print()

median = (len(list1) / 2)
if median.is_integer() == True:
    median = (list1[int(median - 0.5)] + list1[int(median + 0.5)]) / 2
    print('Median is', median)
else:
    print('Median is', list1[int(median)])
print()

print('Frequency is: ')
for a in range(0, len(list1)):
    frequencylist.append(frequency)
    frequency = list1[a]
    if frequency in frequencylist:
        continue
    else:
        print(frequency, '=', list1.count(frequency))
        if list1.count(frequency) > mode:
            mode = list1.count(frequency)
            modelist = []
            modelist.append(frequency)
        elif list1.count(frequency) == mode:
            modelist.append(frequency)
            
print()


if (len(list1) / mode) == len(modelist):
    print('All are modes - all same frequency')
else:
    if len(modelist) > 1:
        print('Modes are', *modelist)
    else:
        print('Mode is', *modelist)
    


