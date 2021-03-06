# FILE PROCCESSING

# handle = open(filename, mode)
fhand = open('mbox.txt')
print(fhand)

# newline = \n

#FILE HANDLE AS A SEQUENCE
xFile = open('mbox.txt')
for eachLine in xFile:
    print(eachLine)

#COUTNING LINES IN A FILE
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count:', count)

#READING THE "WHOLE" FILE
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

#SEARCHING THROUGH A FILE
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#SKIPPING WITH CONTINUE
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

#USING "in" TO SELECT LINES
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

#PROMPT FOR FILE NAME
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened.', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
