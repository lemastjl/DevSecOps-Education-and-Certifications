
list1 = ['Bananas', 'Paper', 'Zebra']

r = range(1,10)
list(r)
print(r)

colors = ['purple', 'teal', 'orange', 'emerald', 'hazel']
print(colors[0])
#purple
print(colors[-1])
#orange

print('purple' in colors)
#True

if 'purple' in colors:
    print('Found purple')

numbers = [1, 2, 3, 4, 5]

for numbers in numbers:
    print(numbers)

for color in colors:
    print(color)

i = 0
while i < len(colors):
    print(f'{i}: {colors[i]}')
    i += 1
