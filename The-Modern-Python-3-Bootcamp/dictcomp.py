
numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers)

squared_numbers = {num: num**2 for num in [1,2,3,4,5]}

print(squared_numbers)

str1 = 'ABC'
str2 = '123'

combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)

instructor = {'name':'bob', 'city':'cuperin', 'color':'tan'}

all_upper_case = {key.upper():value.upper() for key,value in instructor.items()}

num_list = [1,2,3,4]

print(

{num:('even' if num%2 ==0 else 'odd') for num in num_list},

{num:('even' if num%2 ==0 else 'odd') for num in range(0,100)}

)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {item[0]:item[1] for item in person}
print(answer)
#or

answer = dict(person)
print(answer)
