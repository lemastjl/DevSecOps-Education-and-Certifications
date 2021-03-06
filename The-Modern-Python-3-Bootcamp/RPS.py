# Game Rock, Paper, Scissors...
player_wins = 0
computer_wins = 0
winning_score = 1
print('\nWelcome to Rock, Paper, Scissors!\n')
print('Let\'s play!\n')
print('Please enter a winning rounds score:\n')
winning_score = int(input())
while player_wins < winning_score and computer_wins < winning_score:
    print(f'\nPlayer Score: {player_wins} Computer Score: {computer_wins}\n')
    print('Please enter a choice below: Rock, Paper, or Scissors\n')
    user_choice = input()
    user_choice = str(user_choice.capitalize())
    print(f'\nPlayer chooses "{user_choice}".\n')
    if user_choice == 'Rock' or user_choice == 'Paper' or user_choice == 'Scissors':
        import random

        comp_choice = random.randint(0, 2)
        if comp_choice == 0:
            comp_choice = 'Rock'
        elif comp_choice == 1:
            comp_choice = 'Paper'
        else:
            comp_choice = 'Scissors'
        comp_choice = str(comp_choice.capitalize())
        print(f'Computer chooses "{comp_choice}".\n')
        if comp_choice == 'Rock' or comp_choice == 'Paper' or comp_choice == 'Scissors':
            lose_statement = f'{comp_choice} beats {user_choice}.\n \nYou have lost the round!'
            win_statement = f'{user_choice} beats {comp_choice}.\n \nYou have won the round!'
            tie_statement = f'{user_choice} is equal to {comp_choice}.\nIt\'s a tie!'
            if user_choice == comp_choice:
                print(tie_statement)
            elif user_choice == 'Rock':
                if comp_choice == 'Scissors':
                    player_wins += 1
                    print(win_statement)
                elif comp_choice == 'Paper':
                    computer_wins += 1
                    print(lose_statement)
            elif user_choice == 'Paper':
                if comp_choice == 'Rock':
                    player_wins += 1
                    print(win_statement)
                elif comp_choice == 'Scissors':
                    computer_wins += 1
                    print(lose_statement)
            elif user_choice == 'Scissors':
                if comp_choice == 'Paper':
                    player_wins += 1
                    print(win_statement)
                elif comp_choice == 'Rock':
                    computer_wins += 1
                    print(lose_statement)
        else:
            print('Opps, something went wrong!')
            print('\nGoodbye!\n') 
            exit()
    else:
        print('Player did not enter a valid choice, exiting game...')
        print('\nGoodbye!\n')
        exit()
if player_wins >= winning_score:
    print('\n  Congratulations! You have won the game!')
else:
    print('\n  Sorry, you have lost the game!\n')
print(f'\nFinal score => Player: {player_wins} Computer: {computer_wins}\n')
# tie_statement = f'So you think yo can dance {user_choice} {comp_choice}

