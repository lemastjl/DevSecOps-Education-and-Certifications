# DICTIONARY METHODS

d = dict(a=1, b=2, c=3)

# .get()
# GETS KEY IN OBJECT, RETURNS None IF NOT FOUND

d.get('a') # 1
d.get('no_key') # None

# .clear()
# CLEARS ALL VALUES

# .copy()
# MAKES A COPY OF A DICTIONARY

clone = d.copy()
clone == d #True

{}.fromkeys(['email'], 'unknown') # {'email': 'unknown'}
# CREATES KEY-VALUE PAIRS FROM COMMA SEPARATED VALUES

new_user = {}.fromkeys(['name', 'score', 'email','profile bio'], 'unknown')
print(new_user)

new_user_keyed = {}.fromkeys(range(1,11), 'unknown')
print(new_user_keyed)

# .pop()
# REMOVE ITEM FROM DICTIONARY
d.pop('a') # 1

d.popitem()
# REMOVE RANDOM ITEM

# .update(dictionary) ONLY ADDDS/UPDATES ITEMS
first = dict(a=1, b=2, c= 3, d=4, e=5)
second = {}

second.update(first)
second # {'a':1, 'b':2 ect...}

#overwrite existing KEY
second['a'] = 'AMAZING'
