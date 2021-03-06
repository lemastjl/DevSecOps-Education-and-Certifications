#ASSOCIATIVE ARRAYS (DICTIONARIES)

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

ddd['age'] = 23
print(ddd)

#HISOGRAMS USING DICTIONARIES

counts = dict()
names = ['csev', 'csev', 'csev', 'zian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


#BETTER CODE

counts = dict()
names = ['csev', 'csev', 'csev', 'zian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#RETRIEVING LISTS OF KEYS AND VALUES

JJJ = {'chuck':1, 'fred':42, 'jan':100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())
