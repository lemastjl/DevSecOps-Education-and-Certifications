fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) +1
        #print(w, 'new', di[w])

largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k
print('The word:', theword, 'apears', largest, 'times')
