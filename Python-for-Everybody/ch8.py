#ADDING ARRAYS

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#ARRAY SLICING

t =[9, 41, 12, 3, 74, 15]
t[1:3] #UP TO BUT NOT INCLUDING 3
#[41,12]

#BUILDING AN ARRAY

stuff = list()
stuff.append('book')
stuff.append('99')
print(stuff)
#['book', 99]
stuff.append('cookie')
print(stuff)
#['book', 99, 'cookie']

#FIND SOMETHING IN AN ARRAY

some = [1, 9, 21, 10, 16]
9 in some
#True
15 in some
#False
20 not in some
#True

#SORT ARRAYS

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
#['Glenn', 'Joseph', 'Sally']
print(friends[1])
#Joseph

#FINDING AVERAGE

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

#
