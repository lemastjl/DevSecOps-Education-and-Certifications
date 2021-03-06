# ask for age

# 18-21 wristband

# 21+ drink, normal entry

# too young, sorry

print('18+ Only! Enter your age to continue:')
age = input()
if age:
    age = int(age)
    if age >= 21:
        print('You may enter...')
        print('No restrictions (.)(.)')
    elif age >= 18:
        print('18-20. You may enter, but with restrictions...')
        print('Wristband required!')
        print('No drinking!')
    else:
        print('You are not old enough to enter!')
        print('** ACCESS DENIED! **')
else:
    print('Did not disclose age...')
    print('** ACCESS DENIED! **')
