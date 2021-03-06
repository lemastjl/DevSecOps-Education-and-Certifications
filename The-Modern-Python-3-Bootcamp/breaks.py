# while True:
#     command = input('Type "exit" to exit: ')
#     if (command == 'exit'):
#         break

from random import randint
print('What is the number to find?')
find_num = int(input());
i = 0
number = 0
while number != find_num:
    i += 1
    number = randint(1, 10)
    print(f'The random number is {number}.')
    if number == find_num:
        break
print(f'Horray, {number} is the right number of "{find_num}"')
print(f'It took {i} tries to find {find_num}.')
