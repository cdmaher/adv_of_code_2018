import sys
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()


for curline in lines:
    for line in lines:
        matches = 0
        for x in range(0, len(line)):
            if curline[x] != line[x] and matches == 1:
                matches += 1
                break
            if curline[x] != line[x]:
                matches += 1
        if matches == 1:
            print curline + ' . ' + line


threeCount = 0
twoCount = 0
for line in lines:
    totals = {}
    twos = Set()
    threes = Set()
    for char in line:
        totals[char] = totals[char] + 1 if char in totals else 1
        if (totals[char] == 2):
            twos.add(char)
        if (totals[char] == 3):
            twos.remove(char)
            threes.add(char)
        if (totals[char] == 4):
            print "NO"
            threes.remove(char)
    # print totals
    twoCount = twoCount + 1 if twos else twoCount
    threeCount = threeCount + 1 if threes else threeCount
    # print 'threes: ' + ','.join(threes)
    # print 'twos: ' + ','.join(twos)


print 'twos: ' + str(twoCount)
print 'threes: ' + str(threeCount)
print 'sdfn ' + str(twoCount * threeCount)
