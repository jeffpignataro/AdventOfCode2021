from os import linesep


counter = 0

f = open('input.txt', 'r')

set1, set2, set3 = 0
lastSet = 0
for i, rowStr in enumerate(f):
    row = int(rowStr)
    set1+=row
    if i%3 == 0:
        if row > lastSet and lastSet > 0:
            counter+=1
            pass
        lastSet = row

print(counter)
