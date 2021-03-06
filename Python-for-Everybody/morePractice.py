
# SIMPLE ARRAY

nums = [3,41,12,9]

# VAR FOR FOLLOWONG EXERCISES

fruit = 'banana'

# INDEX OPERATOR FOR STRINGS

letter = fruit[1]
print(letter)

# STRING LENGTH

x = len(fruit)
print(x)

# LOOPING THROUGH STRINGS

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# LOOPING STRINGS WITH FOR LOOP (PRETTIER CODE THAN WHILE LOOP)

for letter in fruit:
    print(letter)

#SLICING STRINGS

s = 'Monty Python'
print(s[0:4])
#prints Mont
print (s[:7])
#BEGINING TO 6

# PARSING AND EXTRACTING

#GET EMAIL ADDRESS DOMAIN (uct.ac.za)
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atPosistion = data.find('@')
print(atPosistion)

stopPosition = data.find(' ', atPosistion)
print(stopPosition)

host = data[atPosistion + 1 : stopPosition]
print(host)
