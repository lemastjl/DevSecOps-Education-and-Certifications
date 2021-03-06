# While loop practice
# n = 1000
# while n > 100:
#     print(f'{n} many loops have progressed')
#
# user_response = None
# while user_response != 'please':
#     user_response = input('Ah ah ah, you didn\'t say the magic word: ')

msg = input('What\'s the secret password?')
while msg != 'bananas':
    print('WRONG!')
    msg = input('What\'s the secret password?')
print('CORRECT!')

for i in range(1,10)
