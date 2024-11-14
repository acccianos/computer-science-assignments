finalnum = 0
cardnum = int(input('Enter card number: ')) #79927398713
anothernum = cardnum
cardnum = cardnum // 10
while cardnum > 0: 
    digit = cardnum % 10 
    cardnum = cardnum // 100
    digit = digit * 2
    if digit > 9:
        digit = digit - 9
    else:
        digit = digit
    finalnum = finalnum + digit
while anothernum > 0:
    digit2 = anothernum % 10 #test4 = digit2
    anothernum = anothernum // 100 #test5 = anothernum
    finalnum = finalnum + digit2
if finalnum % 10 == 0:
    print('Valid')
else:
    print('Not valid')
print(finalnum)