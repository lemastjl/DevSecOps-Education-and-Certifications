
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

numbers.append(11)
print(numbers)

numbers.extend([12,13,14,15])
print(numbers)

numbers.insert(2, 'Hi')
print(numbers)

numbers.pop(2)
print(numbers)

list = ['thing1', 'thing2', 'thing3', 'thing4']
print(list)

list.remove('thing4')
print(list)

print(numbers.index(5))
print(numbers.index(5, 1))
print(numbers.index(5, 2))

print(numbers.count(2))
print(numbers.count(3))
print(list.count(2))

print(numbers.reverse())

print(numbers.sort())

words = ['Coding', 'Is', 'Fun!']
print(' '.join(words))

name = ['Mr', 'Steele']
print('. '.join(name))

list.clear()
print(list)
