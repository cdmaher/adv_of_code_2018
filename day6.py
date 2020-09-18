import sys, re
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()


def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


grid = [[-1 * 500] for i in range(500)]
counters = {}
region_size = 0
region_locs = []
for j in range(0, 500):
    for i in range(0, 500):
        min_dist = 10000
        min_ind = -1
        counter = 0
        total_dist = 0
        for line in lines:
            (x, y) = line.split(',')
            dist = man_dist(int(x), int(y), i, j)
            if dist < min_dist:
                min_dist = dist
                min_ind = counter
            elif dist == min_dist:
                min_ind = -1
            counter += 1
            total_dist += dist

        if total_dist < 10000:
            region_size += 1
            region_locs.append((i, j))

        if i == 0 or i == 499 or j == 0 or j == 499:
            counters[min_ind] = -1
        elif min_ind not in counters:
            counters[min_ind] = 1
        elif counters[min_ind] != -1:
            counters[min_ind] = counters[min_ind] + 1
    print j

for item in sorted(counters.iteritems(), key=lambda val: val[1]):
    print item
print counters
print region_locs
print region_size
