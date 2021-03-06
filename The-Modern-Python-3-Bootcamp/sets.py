#SETS

# NO DUPLICATE VALUES AND NOT ORDERED
# NO INDEX ACCESS (s[0] = ERROR)

s = {1, 4, 5}

4 in s # True

s2 = set({1, 4, 5})

numbers = {1,2,3,4}

for number in numbers:
    print(number)

print(len(set(numbers)))

s3 = ([1,2,3])

s.add(4) # {1,2,3,4}

s.add(4) # STAYS SAME @ {1,2,3,4} NO DUPLICATES

s.remove(4) # {1,2,3}

#  OR USE BELOW TO AVIOD RETURNING ERROR

s.discard(3)

copy_set = s.copy()

clear_set = s.clear()

# UNION A SET
math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

all_students_once = math_students | biology_students

whos_in_both = math_students & biology_students
