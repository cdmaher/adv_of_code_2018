import sys, re
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()
polymers = lines[0]

x = 0
minlength = 40000
lettr = 'fs'
for c in xrange(ord('A'), ord('Z') + 1):
    char = chr(c)
    lower = char.lower()

    print 'now ' + char + " " + lower
    replacement = polymers
    x = 0
    replacement = re.sub('[' + char + lower + ']', '', polymers)
    # print replacement
    while x < len(replacement) - 1:
        if (replacement[x].lower() == replacement[x + 1].lower()
                and replacement[x] != replacement[x + 1]):
            replacement = replacement[:x] + replacement[x + 2:]
            x -= 2
        x += 1
        if len(replacement) < minlength:
            minlength = len(replacement)
            letter = char
    print letter + ' ' + str(len(replacement))
    print replacement

# print polymers
print len(lines[0])
print minlength
