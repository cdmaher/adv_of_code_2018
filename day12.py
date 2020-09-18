import sys
from sets import Set

file = open(sys.argv[1], 'r')

init_state = open(sys.argv[2], 'r')

lines = file.readlines()


class Plant:
    def __init__(self, x, y, velx, vely):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely

    def setPoint(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Pos: ' + str(self.x) + ',' + str(self.y) + ' vel: ' + str(
            self.velx) + "," + str(self.vely)

    __repr__ = __str__


GENERATIONS = 20000

state = init_state.readlines()[0]
state = state.replace('\n', '')

state = ('.' * 20000) + state + ('.' * 20000)

# pots = [hash('.....')] * len(state)
# first = hash('0000' + state[0])
# second = hash('000' + state[0] + state[1])
# pots[0] = hash('00' + state[0] + state[1] + state[2])
# pots[1] = hash('0' + state[0] + state[1] + state[2] + state[3])
# first = hash(state[len(state) - 1] + '....')
# second = hash(state[len(state) - 2] + state[len(state) - 1] + '...')
# pots[len(state)
#      - 2] = hash(state[len(state) - 3] + state[len(state) - 2] + state[len(state)
#                                                                   - 1] + '..')
# pots[len(state) - 1] = hash(state[len(state) - 4] + state[len(
#     state) - 3] + state[len(state) - 2] + state[len(state) - 1] + '.')
#
# pots = [0] * len(state)
# for i in range(2, len(state) - 2):
#     pots[i] = hash(state[i - 2:i + 2])


def addPots(pots):
    count = 0
    for i in range(0, len(pots)):
        if pots[i] == '#':
            count += i - 20000
    return count


rules = {}

for line in lines:
    split = line.split()
    rules[hash(split[0])] = split[2]

next_state = state
last_amount = -2342234
for gen in range(0, 140):
    state = next_state
    for i in range(2, len(state) - 2):
        cur_rule = hash(state[i - 2] + state[i - 1] + state[i] + state[i + 1] +
                        state[i + 2])
        # print 'curr ' + str(cur_rule)
        if cur_rule in rules:
            # print 'RULE ' + str(rules[cur_rule]) + ' ' + str(cur_rule)
            # print 'OLD ' + state
            next_state = next_state[:i] + rules[cur_rule] + next_state[i + 1:]
            # print 'NEW ' + next_state
        else:
            next_state = next_state[:i] + '.' + next_state[i + 1:]
        # print 'index ' + str(i)
    print str(addPots(next_state))
    if last_amount == addPots(next_state):
        break
    print 'DIFF ' + str(addPots(next_state) - last_amount)
    last_amount = addPots(next_state)
    print 'GEN ' + str(gen)

print 12196 + ((50000000000 - 128) * 78)
