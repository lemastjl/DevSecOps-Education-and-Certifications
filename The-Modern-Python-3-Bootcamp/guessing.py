from random import randint
rand_num = randint(1,10)
while True:
    print('Guess a number between 1 and 10: ')
    try:
        user_guess = input()
        user_guess = int(user_guess)
    except ValueError:
        print('Error: Not integer! The input was not a valid integer.')
    else:
        user_guess = int(user_guess)
        if user_guess > 11 or user_guess < 0:
            print('Error: Out of bounds! Please enter a valid number between 1 and 10.')
        elif user_guess < rand_num:
            print('Too low, try again!')
        elif user_guess > rand_num:
            print('Too high, try again!')
        else:
            print('You guessed it! You won!')
            print('Would you like to play again?')
            play_again = input('(y/n): ')
            play_again = play_again.capitalize()
            if play_again == 'Y':
                rand_num = randint(1,10)
            elif play_again == 'N':
                print('Thank you for playing.')
                exit()
            else:
                print('Error: Invalid choice!')
                print('Exiting game')
                exit()
