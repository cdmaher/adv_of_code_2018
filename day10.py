import sys
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()


class Pos:
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


smallsky = [['.'] * 200 for i in range(0, 200)]

SKY_SIZE = 100


def printSky(sky):
    for j in range(0, SKY_SIZE):
        thing = ''
        for i in range(0, SKY_SIZE):
            thing += " " + sky[j][i]
        thing += '\n'
        print thing


points = []

for curline in lines:
    x = int(curline[10:16])
    y = int(curline[18:24])
    velx = int(curline[36:38])
    vely = int(curline[40:42])
    points.append(Pos(x, y, velx, vely))

print 'what' + str(points)
counter = 0
nope = False
while counter < 20000:
    sky = [['.'] * SKY_SIZE for i in range(0, SKY_SIZE)]
    for point in points:
        newx = point.x + (1 * point.velx)
        newy = point.y + (point.vely * 1)
        point.setPoint(newx, newy)

        tosety = newy / 1 - 100
        tosetx = newx / 1 - 175
        if tosetx < 0 or tosetx > SKY_SIZE - 1 or tosety < 0 or tosety > SKY_SIZE - 1:
            nope = True
        else:
            sky[tosety][tosetx] = '#'
        # smallsky[newy / 1000][newx / 1000] = '$'
    if counter > 10450 and counter < 10470:
        print 'Counter ' + str(counter)
        # print 'what' + str(points)
        printSky(sky)
    counter += 1
