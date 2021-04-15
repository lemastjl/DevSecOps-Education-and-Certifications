
# # using for loop

# for x in range(1):
#     for num in range(1,11):
#         print('\U0001f600' * num)


# # using while loop

# times = 1
# while times < 11:
#     print('\U0001f600' * times)
#     times += 1

# centered

times = 20
i = 1
while i <= times:
    spaces = ' ' * ((times*i) // 2) 
    stars = '\U0001f600' * i
    print(spaces + stars)
    i += 2 