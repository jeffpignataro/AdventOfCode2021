from os import linesep


counter = 0

f = open('input.txt', 'r')

lastRow = 0
for i, rowStr in enumerate(f):
    row = int(rowStr)
    if row > lastRow and lastRow > 0:
        counter+=1
        pass
    lastRow = row

print(counter)
