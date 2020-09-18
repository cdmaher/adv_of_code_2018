import sys
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()


class LogEvent:
    def __init__(self, date, time, event, guard):
        self.date = date
        self.time = time
        self.event = event
        self.guard = guard
        self.minutes = [0] * 60

    def printStuff(self):
        print self.date + ", " + self.time + ", " + self.event + ", " + str(
            self.guard)


events = []

for curline in lines:
    expanded = curline.split()
    guard = expanded[3] if expanded[2] == 'Guard' else None
    events.append(
        LogEvent(expanded[0][1:], expanded[1][:-1], expanded[2], guard))


def sorter(log):
    month = int(log.date.split('-')[1])
    day = int(log.date.split('-')[2])
    hour = int(log.time.split(':')[0])
    minute = int(log.time.split(':')[1])
    return month * 1000000 + day * 10000 + hour * 100 + minute


events.sort(key=sorter)

sleepTimes = {}
guardID = None
start = 0
for ev in events:
    if ev.event == 'Guard':
        guardID = ev.guard
    elif ev.event == 'falls':
        start = int(ev.time.split(':')[1])
    elif ev.event == 'wakes':
        end = int(ev.time.split(':')[1])
        sleeptime = end - start
        if guardID not in sleepTimes:
            sleepTimes[guardID] = (0, [0] * 60)
        sleepTimes[
            guardID] = (sleepTimes[guardID][0] + sleeptime, sleepTimes[guardID][1])
        for x in range(start, end):
            sleepTimes[guardID][1][x] = sleepTimes[guardID][1][x] + 1

maxval = (None, 0)
for guard in sleepTimes:
    for minutes in sleepTimes[guard][1]:
        if (minutes > maxval[1]):
            maxval = (guard, minutes)

for ev in events:
    ev.printStuff()

print sleepTimes
print sleepTimes['#1823']
print sleepTimes['#1823'][1].index(14)
print 1823 * 41
print maxval
print " " + str(3011 * sleepTimes['#3011'][1].index(18))
