import sys, re
from sets import Set


class Marble:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return 'Val: ' + str(self.val) + ' left: ' + str(
            self.left.val) + " right " + str(self.right.val)

    def place(self, left, right):
        self.left = left
        self.right = right
        # print 'self ' + str(self)
        # print 'left ' + str(left)
        # print 'right ' + str(right)
        self.left.right = self
        self.right.left = self
        # print 'new self ' + str(self)
        # print 'new left ' + str(left)
        # print 'new right ' + str(right)
        # print '-----------------------'


    def remove(self):
        temp = self.left
        self.left.right = self.right
        self.right.left = temp

    __repr__ = __str__


def printCirc(node):
    stri = 'Val: ' + str(node.val) + ' '
    curNode = node.right
    while curNode.val != node.val:
        stri += str(curNode.val) + ' '
        curNode = curNode.right
    return stri


curMarb = Marble(0)
curMarb.place(curMarb, curMarb)

PLAYERS = 411
LAST_MARB = 7105800

lastMarb = False
players = [0] * PLAYERS
counter = 1

while not lastMarb and counter < LAST_MARB + 5:
    curPlayer = counter % PLAYERS - 1
    if counter % 23 == 0:
        players[curPlayer] += counter
        toRemove = curMarb.left.left.left.left.left.left.left
        if toRemove.val == LAST_MARB:
            print 'what ' + str(toRemove.val) + " " + str(toRemove.right.val)
            players[curPlayer] += LAST_MARB
            lastMarb = True
        else:
            curMarb = toRemove.right
            toRemove.remove()
            players[curPlayer] += toRemove.val
    else:
        newMarb = Marble(counter)
        newMarb.place(curMarb.right, curMarb.right.right)
        curMarb = newMarb

    counter += 1
    # print 'current ' + printCirc(curMarb)
players.sort()
print 'hi ' + str(players)
