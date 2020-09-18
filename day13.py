import sys
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.prev_state = '|' if direction == 'v' or direction == '^' else '-'
        self.next_move = 'left'
        self.isCrashed = False
        self.hasMoved = False

    def turnLeft(self):
        if self.direction == '>':
            self.direction = '^'
        elif self.direction == '^':
            self.direction = '<'
        elif self.direction == '<':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '>'

    def turnRight(self):
        if self.direction == '>':
            self.direction = 'v'
        elif self.direction == '^':
            self.direction = '>'
        elif self.direction == '<':
            self.direction = '^'
        elif self.direction == 'v':
            self.direction = '<'

    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.hasMoved = True

    def reset(self):
        self.hasMoved = False

    def setPoint(self, next_spot):
        self.prev_state = next_spot
        if next_spot == "\\" and (self.direction == 'v'
                                  or self.direction == '^'):
            self.turnLeft()
        elif next_spot == "\\" and (self.direction == '<'
                                    or self.direction == '>'):
            self.turnRight()
        elif next_spot == "/" and (self.direction == '<'
                                   or self.direction == '>'):
            self.turnLeft()
        elif next_spot == "/" and (self.direction == 'v'
                                   or self.direction == '^'):
            self.turnRight()
        elif next_spot == '+':
            if self.next_move == 'left':
                self.turnLeft()
                self.next_move = 'straight'
            elif self.next_move == 'straight':
                self.next_move = 'right'
            else:
                self.turnRight()
                self.next_move = 'left'
        elif next_spot == '>' or next_spot == '<' or next_spot == 'v' or next_spot == '^':
            self.isCrashed = True
            self.prev_state = 'X'

    def __str__(self):
        return 'Pos: (' + str(self.x) + ',' + str(self.y) + ') dir: ' + str(
            self.direction)

    __repr__ = __str__


def printTrack(track):
    trackStr = ''
    for j in range(0, len(track)):
        for i in range(0, len(track[j])):
            if track[j][i] != '.':
                if isinstance(track[j][i], Cart):
                    trackStr += str(track[j][i].direction)
                else:
                    trackStr += str(track[j][i])
    print trackStr


carts = []
track = [['.' for i in range(500)] for j in range(500)]

i = 0
j = 0
for line in lines:
    i = 0
    for block in line:
        track[j][i] = block
        if block == 'v' or block == '^' or block == '>' or block == '<':
            cart = Cart(i, j, block)
            carts.append(cart)
            track[j][i] = cart
        i += 1
    j += 1

ticks = 0
tries = 30000
while ticks < tries and len(carts) > 1:
    print 'TICK ' + str(ticks)

    carts = sorted(carts, key=lambda cart: cart.x)
    carts = sorted(carts, key=lambda cart: cart.y)
    # print 'carts: ' + str(carts)
    hasCrash = False
    cartnum = 0
    while cartnum < len(carts):
        next_spot = ''
        next_pos = (0, 0)
        cart = carts[cartnum]
        if cart.hasMoved:
            cartnum += 1
            continue
        # print 'cur cart ' + str(cart)
        if cart.direction == '>':
            next_spot = track[cart.y][cart.x + 1]
            next_pos = (cart.x + 1, cart.y)
        elif cart.direction == '<':
            next_spot = track[cart.y][cart.x - 1]
            next_pos = (cart.x - 1, cart.y)
        elif cart.direction == '^':
            next_spot = track[cart.y - 1][cart.x]
            next_pos = (cart.x, cart.y - 1)
        else:
            next_spot = track[cart.y + 1][cart.x]
            next_pos = (cart.x, cart.y + 1)
        track[cart.y][cart.x] = cart.prev_state
        if isinstance(track[next_pos[1]][next_pos[0]], Cart):
            print 'CRASH ' + str(cart)
            hasCrash = True
            carts.remove(cart)
            carts.remove(track[next_pos[1]][next_pos[0]])
            track[next_pos[1]][next_pos[0]] = track[next_pos[1]][next_pos[
                0]].prev_state
            print 'CARTS NOW: ' + str(carts)
            cartnum = 0
            continue
        cart.setPoint(next_spot)
        cart.setPos(next_pos[0], next_pos[1])
        track[next_pos[1]][next_pos[0]] = cart
        cartnum += 1
        if cart.isCrashed:
            print 'NOO wrong crash ' + str(cart)
            hasCrash = True
            track[next_pos[1]][next_pos[0]] = 'X'
            break
    for cart in carts:
        cart.reset()
    # printTrack(track)
    ticks += 1

print carts
printTrack(track)
