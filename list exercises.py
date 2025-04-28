sports = ['Basketball', 'American Football']
favsport = input('Enter your favourite sport: ')
sports.append(favsport)
sports.sort()
print(sports)
print()

subjects = ['maths', 'english', 'irish', 'geography', 'history', 'science']
print(subjects)
badsubject = input('Which of these subjects do you dislike: ')
if badsubject not in subjects:
    print('Subject not in list')
else:
    for b in range(0,5):
        if badsubject == subjects[b]:
            subjects.remove(badsubject)
            print(subjects)
print()

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'black', 'white']
firstcolours = int(input('Enter a number between 0 and 4: '))
secondcolours = int(input('Enter a number between 5 and 9: '))
print(colours[firstcolours:secondcolours])
print()

numlist = [564, 859, 152, 234]
for a in range(0, 4):
    print(numlist[a])
threedig = int(input('Enter a three digit pin: '))
if threedig not in numlist:
    print('Not in list')
else:
    print(numlist.index(threedig))
print()

partypeeps = []
again = 'y'
print('Name three people to invite to a party')
for a in range(0, 3):
    partypeeps.append(input('Person: '))
while again == 'y':
    again = input("Invite another person? ('y' for yes): ")
    again = again.lower()
    if again != 'y':
        break
    else:
        partypeeps.append(input('Person: '))
print(partypeeps)
    
    
