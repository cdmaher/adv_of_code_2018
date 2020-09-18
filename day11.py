import sys
from sets import Set

grid = [[0] * 300 for i in range(0, 300)]

powerSquares = [[0] * 300 for i in range(0, 300)]

SERIAL = 3999


def printGrid(grid, size):
    for j in range(0, size):
        thing = ''
        for i in range(0, size):
            thing += " " + str(grid[j][i])
        thing += '\n'
        print thing


def printFuelCells(x, y):
    for j in range(y, y + 5):
        thing = ''
        for i in range(x, x + 5):
            thing += " " + str(grid[j][i])
        thing += '\n'
        print thing


def powerLevel(x, y):
    rackID = x + 10
    powerLevel = rackID * y + SERIAL
    powerLevel *= rackID
    powerLevel = (powerLevel / 100) % 10
    return powerLevel - 5


def calcSquare(x, y, size):
    power = 0
    for j in range(y, y + size):
        for i in range(x, x + size):
            if i < 300 and j < 300:
                power += grid[j][i]
            else:
                return 0
    return power


memo = [[[0] * 300 for i in range(0, 300)] for j in range(0, 300)]


def fastCalcSquare(x, y, size, memoX, memoY):
    power = memo[y][x][size - 1] + memoX[size - 1] + memoY[size
                                                           - 1] + grid[y][x]
    if memoX[x][size] == 0:
        memoX[x][size] = memoX[x][size - 1] + grid[y][x]
    if memoY[y][size] == 0:
        memoY[y][size] = memoY[y][size - 1] + grid[y][x]
    return power


for j in range(0, 300):
    for i in range(0, 300):
        grid[j][i] = powerLevel(i, j)

largest = 0
largestCoord = (0, 0, 0)
memo = [[[0] * 300 for i in range(0, 300)] for j in range(0, 300)]
memoX = [[[0] * 300 for i in range(0, 300)] for j in range(0, 300)]
memoY = [[[0] * 300 for i in range(0, 300)] for j in range(0, 300)]

cursize = 299
for size in range(1, cursize + 1):
    for j in range(0, cursize - size + 1):
        for i in range(0, cursize - size + 1):
            powLev = memo[j][i][size - 1]
            powLev += memoX[j][i + size - 1][size - 1]
            powLev += memoY[j + size - 1][i][size - 1]
            powLev += grid[j + size - 1][i + size - 1]
            # print 'x ' + str(memoX[j][i + size - 1][size - 1])
            # print 'y ' + str(memoY[j + size - 1][i][size - 1])
            #
            # print 'pow lev : ' + str(powLev) + " at " + str(i) + ',' + str(
            #     j) + " size " + str(size)
            memo[j][i][size] = powLev
            memoX[j][i + size -
                     1][size] = memoX[j][i + size -
                                         1][size - 1] + grid[j + size -
                                                             1][i + size - 1]
            memoY[j + size -
                  1][i][size] = memoY[j + size -
                                      1][i][size - 1] + grid[j + size -
                                                             1][i + size - 1]
            # print 'grid thing ' + str(grid[j + size][i])
            if powLev > largest:
                largest = powLev
                largestCoord = (i, j, size)
    print 'now ' + str(i) + ',' + str(j)

print 'largest ' + str(largest)
print largestCoord
printFuelCells(largestCoord[0], largestCoord[1])
# print memo[0][0]
# print memoX[0][0]
# print memoY[0][0]
# printGrid(grid, cursize)
