import sys
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()

freq = 0
dups = Set()
found = False
times = 1
while not found:
    times += 1

    for line in lines:
        # num = line.lstrip('+')
        # if line
        freq += int(line)
        if freq in dups:
            print 'FOUND: ' + str(freq)
            print 'tims ' + str(times)
            found = True
            break
        dups.add(freq)
        # print 'cur: ' + str(freq)

print freq
