#1 a
print("""
1
  2
    3
""" )

print()

#b
text = 'Test.\nNext line.'
print(text)

print()

#c
print('One', 'Two' * 2)
print('One' + 'Two' * 2)
print(len('0123456789'))

print()

#d
s = '0123456789'
print (s[3], ", ", s[0:3], "-", s[2:5])
print (s[:3], "-", s[3:], ", ", s[3:100])
print (s[20:], s[2:1], s[1:1])

print()

#e
s = '987654321'
print (s[-1], s[-3])
print (s[-3:], s[:-3])
print (s[-100:-3], s[-100:3])

print()

#2 a
y = str(123)
x = 'hello' * 3
print(x, y)
x = 'hello' + 'world'
y = len(x)
print (y, x)

print()

#b
x = 'hello' + \
'to Python' + \
'world'
for char in x:
    y = char
    print(y, ':', end = ' ')

print()

#c
x = 'hello world'
print(x[:2], x[:-2], x[-2:])
print(x[6], x[2:4])
print(x[2:-3], x[-4:-2])

print()

#3
theStr = "This is a test"
inputStr = input("Enter integer:")
inputlnt = int(inputStr)
testStr = theStr
while inputlnt >= 0:
    testStr = testStr[1:-1]
    inputlnt = inputlnt - 1
testBool = 't' in testStr
print (theStr)
print (testStr)
print (inputlnt)
print (testBool)

print()

#4
testStr = "abcdefghi"
inputStr = input ("Enter integer:")
inputlnt = int(inputStr)
count = 2
newStr = ''
while count <= inputlnt:
    newStr = newStr + testStr[0: count]
    testStr = testStr[2:]
    count = count + 1
print (newStr)
print (testStr)
print (count)
print (inputlnt)

print()

#5
inputStr = input("Give me a string:")
biglnt = 0
littlelnt = 0
otherlnt = 0
for ele in inputStr:
    if ele >= 'a' and ele <= 'm':
        littlelnt = littlelnt + 1
    elif ele > 'm' and ele <= 'z':
        biglnt = biglnt + 1
    else:
        otherlnt = otherlnt + 1
print (biglnt)
print (littlelnt)
print (otherlnt)
print (inputStr.isdigit()) 

print()

#6
in1Str = input(" Enter string of digits: ")
in2Str = input(" Enter string of digits: ")

if len(in1Str)>len(in2Str):
    small = in2Str
    large = in1Str
else:
    small = in1Str
    large = in2Str
newStr = ''
for element in small:
    result = int(element) + int(large[0])
    newStr = newStr + str(result)
    large = large[1:]
print (len(newStr))
print (newStr)
print (large)
print (small)

print()

#7a
S = input("Enter String:")
RS = " "
for ch in S:
    RS = ch + RS
print(S + RS)

print()

#b
S = input("Enter string :")
RS = " "
for ch in S:
    RS = ch + 2 + RS
print(RS + S)

print()

#8
S = "PURA VIDA"
print(S[9] + S[9:15])

S = "PURA VIDA"
S1 = S[: 10] + S[10:]
S2 = S[10] + S[-10]

S = "PURA VIDA"
S1 = S* 2
S2 = S1[-19] + S1[-20]
S3 = S1[-19:]

S = "PURA VIDA"
S1 = S[: 5]
S2 = S[5:]
S3 = S1 * 52
S4 = S2 + '3'
S5 = S1 + 3

print()

#9
print('whenever'.find('never'))
print('whenever'.find('what'))
