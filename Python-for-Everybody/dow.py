
#FINDING DAY OF WEEK IN TEXT DOCUMENT

han = open('mbox.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
