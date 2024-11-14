booknum = int(input('Enter 9 digit book number: ')) #020131452
booknum = int(booknum)
booknum2 = booknum
multiply = 2
multiply2 = 0
total = 0
checksum = 0
while booknum > 0: 
    booknum2 = booknum % 10
    booknum = booknum // 10
    multiply2 = multiply * booknum2
    multiply = multiply + 1
    total = total + multiply2
while total % 11 != 0:
    total = total + 1
    checksum = checksum + 1
print(checksum)