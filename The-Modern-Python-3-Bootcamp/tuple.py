# TUPLES

#IMMUTABLE
#CAN SLICE BUT NOT NEST

number = (1, 2, 3, 4, 5)

alphabet = ('a', 'b', 'c', 'd')
print(alphabet)
type(alphabet) # <class 'tuple'>

first_tuple = (1, 2, 3, 3, 5)

first_tuple[1] # 2
first_tuple[2] # 3
first_tuple[-1] # 5

# TUPLES AS A KEY
locations = {
    (35.6895, 39.6917): 'Tokyo Office',
    (40.7128, 74.0060): 'New York Office',
    (37.7749, 122.4194): 'San Francisco Office'
}

# .items() RETURNS A TUPLE

for location in locations:
    print(location)

# BACKWARDS

i = len(locations) - 1
while i >= 0:
    print(locations[i])
    i -= 1

# .count() METHOD
x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

# .index90 METHOD
t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) #ERROR
t.index(3) # 2 ONLY THE FIRST '3' IS RETURNED
