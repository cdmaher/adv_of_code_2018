import sys
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()
# lines = lines[:-1000]
# print lines

fabric = [[None] * 1000 for _ in range(1000)];

dups = 0
noOverlaps = Set()
for curline in lines:
    expanded = curline.split()
    pos = expanded[2].split(',')
    x = int(pos[0])
    y = int(pos[1][:-1])
    (width, height) = expanded[3].split('x')
    (width, height) = (int(width), int(height))
    # print str(expanded) + width + ', ' + height
    overlap = False
    for i in range(x, x + width):
        for j in range(y, y + height):
            # print "I " + str(i) + " J " + str(j)
            # print "fab " + str(fabric[j][i])
            if (fabric[j][i] == None):
                fabric[j][i] = expanded[0][1:]
                # noOverlaps.add(expanded[0][1:])
            else:
                overlap = True
                if fabric[j][i] in noOverlaps:
                    noOverlaps.remove(fabric[j][i])
    if not overlap:
        noOverlaps.add(expanded[0][1:])

print noOverlaps
print "dups " + str(dups)
