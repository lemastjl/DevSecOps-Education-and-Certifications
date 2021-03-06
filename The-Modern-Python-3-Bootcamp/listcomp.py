
#Syntax
#[varName1 for varName1 in list or range]

nums = [1, 2, 3]
print(
[x * 10 for x in nums]
)
#[10, 20 , 30]
print(
[x / 2 for x in nums]
)
#[0.5, 1.0, 1.5]

numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

[num*10 for num in range(1,6)] # [10, 20, 30, 40, 50]

[bool(val) for val in [0, [], '']] # [False, False, False]

string_list = [str(num) for num in nums]

print(string_list)

answer = [char[0][:1] for char in ['Elie', 'Tim', 'Matt']]

print(answer)
