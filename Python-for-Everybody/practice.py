print('Hello World')
print('Bob Tanner')


# IF STATEMENT

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finit')

# IF ELSE STATEMENT

if x > 2 :
    print('Bigger')
else :
    print('Smaller')

#MULTIWAY ELIF STATEMENT

if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All Done')


# WHILE LOOP

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

# FOR LOOP

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

friends = ['Joe', 'Moe', 'Ed', 'Larry']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# LOOP BREAK / CONTINUE

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        contunue
    if line == 'done':
        break
    print(line)
print('Done!')

# CONVERT STRING TO INTEGER

sVal =  '123'
iVal = int(sVal)
print(iVal + 1)

# USER INPUT

nam = input('Who are you? ')
print('Welcome', nam)

# CONVERTING USER INPUT

inputFloor = input('Europe floor?')
usFloor  = int(inputFloor) + 1
print('US floor', usFloor)

# TRY / EXCEPT

aString = 'Hello Bob'
try:
    iString = int(aString)
except:
    iString = -1
print('First', iString)

aString = '123'
try:
    iString = int(aString)
except:
    iString = -1
print('Second', iString)

# FUNCTIONS

def thing():
    print('Hello')
    print('Fun')

thing()

def greet(lang):
    if lang  == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

greet('en')
greet('es')
greet('fr')

print(greet('en'), 'Glen')
print(greet('es'), 'Juan')
print(greet('fr'), 'Micheal')

# COUNTING IN A LOOP

iterationCount = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    iterationCount += 1
    print(iterationCount, thing)
print('After', iterationCount)

# FINDING THE AVERAGE IN A LOOP

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum += value
    print(count, sum, value)
print('After', count, sum, sum / count)

# USING "None" and "is" TO FIND THE SMALLEST VALUE

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
