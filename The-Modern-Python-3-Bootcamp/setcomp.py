# SET COMPREHENSION


{x**2 for x in range(10)}

# {0,1,64,4,36,9,16,49,81,25}

#DEFINE A DICTIONARY INSTEAD (SHOW DIFFERENCE)
{x:x**2 for x in range(10)}

string = 'hello'

vowel_set = {char for char in string if char in 'aeiou'} # {'e', 'o'}

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

are_all_vowels_in_string('sequoia')
#True
