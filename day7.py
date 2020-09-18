import sys
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()

steps = {}

for curline in lines:
    deps = curline.split()
    if deps[7] in steps:
        steps[deps[7]][0].append(deps[1])
    else:
        steps[deps[7]] = ([deps[1]], False, -1)

path = []
counter = 0
workers = ['0', '0', '0', '0', '0']

for i in range(ord('A'), ord('Z') + 1):
    cur_step = chr(i)
    if cur_step not in steps:
        steps[cur_step] = ([], False, -1)
time = 0
while len(path) < 7 and counter < 5000000:

    i = ord('A')
    while i < ord('Z') + 1:
        cur_step = chr(i)
        # print cur_step
        if not steps[cur_step][1]:
            available = True
            if steps[cur_step][2] < i - ord('A') + 60:
                available = False
            if available:
                path.append(cur_step)
                steps[cur_step] = ([], True, 0)
                workers[workers.index(cur_step)] = '0'
                i = ord('A') - 1
        i += 1

    for i in range(ord('A'), ord('Z') + 1):
        cur_step = chr(i)
        if not steps[cur_step][1] and cur_step in workers:
            steps[cur_step] = (steps[cur_step][0], steps[cur_step][1],
                               steps[cur_step][2] + 1)
        elif not steps[cur_step][1] and steps[cur_step][2] == -1:
            available = True
            for deps in steps[cur_step][0]:
                if deps not in steps or not steps[deps][1]:
                    available = False
                    break
            if available:
                for w in range(0, len(workers)):
                    if workers[w] == '0':
                        workers[w] = cur_step
                        steps[cur_step] = (steps[cur_step][0],
                                           steps[cur_step][1], 0)
                        break

    print '----------------------'
    print "cur workers " + str(workers)
    print 'cur path ' + str(path)
    print counter
    counter += 1

for step in steps:
    print step + " " + str(steps[step])
print counter
print path
str = ''
for i in path:
    str += i
print str
print len(str)
