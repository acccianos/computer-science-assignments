#111
bookfile = open('Books.csv', 'w')
bookfile.write(',Book,Author,Year Released,\n')
bookfile.write('0,To Kill A Mockingbird,Harper Lee,1960,\n')
bookfile.write('1,A Brief History of Time,Stephen Hawking,1988,\n')
bookfile.write('2,The Great Gatsby,F. Scott Fitzgerald,1922,\n')
bookfile.write('3,The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985,\n')
bookfile.write('4,Pride and Prejudice,Jane Austen,1813,\n')
bookfile.close()

#112
print('Enter a new record')
book = input('Enter book name: ')
author = input("Enter author's name: ")
year = int(input("Enter the year it was written: "))
bookfile = open('Books.csv', 'a')
number = 5
record = str(str(number) + ',' + book + ',' + author + ',' + str(year) + ',' + '\n')
bookfile.write(record)
bookfile.close()
print()

#113
record_amount = int(input('How many records do you want to add? : '))
for a in range(0, record_amount):
    book = input('Enter book name: ')
    author = input("Enter author's name: ")
    year = int(input("Enter the year it was written: "))
    bookfile = open('Books.csv', 'a')
    number += 1
    record = str(str(number) + ',' + book + ',' + author + ',' + str(year) + ',' + '\n')
    bookfile.write(record)
bookfile.close()
print()

bookfile = open('Books.csv', 'r')
for line in bookfile:
    print(line)
bookfile.close()

booklist = []
authorfind = input('Enter an author in this list: ')
bookfile = open('Books.csv', 'r')
for line in bookfile:
    if authorfind in line:
        booklist.append(line)
for a in range(0, len(booklist)):
    booklist2 = []
    booklist2 = booklist[a].strip()
    booklist2 = booklist2.split(',')
    print(booklist2[1])
bookfile.close()
    
#114
yearlist = []
yearlist3 = []
yearlow = int(input('Enter a starting year: '))
yearhigh = int(input('Enter a finishing year: '))
bookfile = open('Books.csv', 'r')
for line in bookfile:
    yearlist.append(line)
for a in range(1, len(yearlist)):
    yearlist2 = []
    yearlist2 = yearlist[a].strip()
    yearlist2 = yearlist2.split(',')
    yearlist3.append(yearlist2[3])
bookfile.close()
print()
print(yearlist3)

correctyears = []
for a in range(0, len(yearlist3)):
    if int(yearlist3[a]) >= yearlow and int(yearlist3[a]) <= yearhigh:
        correctyears.append(yearlist3[a])
print(correctyears)

bookfile = open('Books.csv', 'r')
booklist = []
for a in range(0, len(correctyears)):
    for line in bookfile:
        if correctyears[a] in line:
                 booklist.append(line)
        for a in range(0, len(booklist)):
            booklist2 = []
            booklist2 = booklist[a].strip()
            booklist2 = booklist2.split(',')
            print(booklist2[1])
bookfile.close()
    