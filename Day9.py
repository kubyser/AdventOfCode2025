import time
from gc import DEBUG_LEAK

import aoc
from Day8 import endTime
from aoc import addCoords

def inside(tp, br, pos):
    return True # if pos is inside rectangle without counting the borders

def isGreen(pos):
    return True # if pos is a green tile based on data

def sign(val):
    return 0 if val == 0 else 1 if val > 0 else -1

NONE = 0
RED = 1
GREEN = 2
BLUE = 3

DEBUG = False
ADDHALVES = False

def printMap():
    print("-------------------------")
    for y in ycoords:
        s = ""
        for x in xcoords:
            c = grid[(x,y)]
            s += ' ' if c == NONE else '#' if c == 1 else 'X' if c == 2 else 'x'
        print(s)
    print("-------------------------")

data = [tuple(int(ss) for ss in s.split(",")) for s in open("resources/day9_input.txt", "r")]
areas = [(abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1) for i,a in enumerate(data[:-1]) for b in data[i+1:]]
areas.sort()
print(f"Part1: {areas[-1]}")

startTime = time.time()
xcoords = list({d[0] for d in data})
xcoords.sort()
if DEBUG:
    print(f"XCoords before halves {xcoords}")
if ADDHALVES:
    addX = []
    for i,x in enumerate(xcoords[:-1]):
        nx = xcoords[i+1]
        if nx-x > 1:
            mx = (nx+x)//2
            addX.append(mx)
    xcoords = xcoords + addX
    xcoords.sort()
    if DEBUG:
        print(f"XCoords after  halves {xcoords}")
xcoordsMap = {x:i for i,x in enumerate(xcoords)}

ycoords = list({d[1] for d in data})
ycoords.sort()
if DEBUG:
    print(f"YCoords before halves {ycoords}")
if ADDHALVES:
    addY = []
    for i,y in enumerate(ycoords[:-1]):
        ny = ycoords[i+1]
        if ny-y > 1:
            my = (ny+y)//2
            addY.append(my)
    ycoords = ycoords + addY
    ycoords.sort()
    if DEBUG:
        print(f"YCoords after  halves {ycoords}")
ycoordsMap = {y:j for j,y in enumerate(ycoords)}

grid = {(x,y):NONE for x in xcoords for y in ycoords}

for i,a in enumerate(data):
    j = i+1 if i+1 < len(data) else 0
    b = data[j]
    grid[a] = RED
    delta = (sign(b[0]-a[0]), sign(b[1]-a[1]))
    gridPos = (xcoordsMap[a[0]], ycoordsMap[a[1]])
    gridPos = addCoords(gridPos, delta)
    pos = (xcoords[gridPos[0]], ycoords[gridPos[1]])
    while pos != b:
        grid[pos] = GREEN
        gridPos = addCoords(gridPos, delta)
        pos = (xcoords[gridPos[0]], ycoords[gridPos[1]])

minX = data[0][0]
minY = data[0][1]
for i,a in enumerate(data[:-1]):
    b = data[i+1]
    if a[0] == b[0]:
        if a[0] < minX:
            minX = a[0]
            minY = min([a[1], b[1]])
if DEBUG:
    printMap()

posMinX = xcoordsMap[minX]
posMinY = ycoordsMap[minY]
startX = posMinX + 1
startY = posMinY + 1
print(f"Start pos: {startX, startY}, grid coords {xcoords[startX], ycoords[startY]}")
toExplore = {(startX, startY)}
while len(toExplore) > 0:
    pos = toExplore.pop()
    gridPos = (xcoords[pos[0]], ycoords[pos[1]])
    if grid[gridPos] != NONE:
        continue
    grid[gridPos] = BLUE
    for d in aoc.DIRECTIONS_MAIN:
        newPos = addCoords(pos, aoc.DIRECTION_MOVEMENT[d])
        toExplore.add(newPos)
if DEBUG:
    printMap()
endTime = time.time()
print(f"Time to checkpoint 1: {endTime-startTime}")
maxArea = 0
for i,a in enumerate(data[:-1]):
    for b in data[i+1:]:
        area = (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
        if area <= maxArea:
            continue
        minX = min([a[0], b[0]])
        minY = min([a[1], b[1]])
        maxX = max([a[0], b[0]])
        maxY = max([a[1], b[1]])
        good = True
        for x in range(xcoordsMap[minX], xcoordsMap[maxX]+1):
            for y in range(ycoordsMap[minY], ycoordsMap[maxY]+1):
                gridPos = (xcoords[x],ycoords[y])
                if grid[gridPos] == NONE:
                    good = False
                    break
            if not good:
                break
        if not good:
            continue
        maxArea = area
print(f"Part 2: {maxArea}")
endTime = time.time()
print(f"Total time elapsed: {endTime-startTime}")

exit(0)
for i,a in enumerate(data[:-1]):
    for b in data[i+1:]:
        area = abs(a[0]-b[0]+1)*abs(a[1]-b[1]+1)
        if area <= maxArea:
            continue
        x1 = min([a[0], b[0]])
        y1 = min([a[1], b[1]])
        x2 = max([a[0], b[0]])
        y2 = max([a[1], b[1]])
        good = True
        xr = [x1, x2]
        for y in range(y1, y2+1):
            for di, d in enumerate(data[:-1]):
                d1 = data[i+1]
                if d[1] == y and d1[1] == y:
                    if d[0] < d1[0]:
                        minDX = d[0]
                        maxDX = d1[0]
                    else:
                        minDX = d1[0]
                        maxDX = d[0]
                    if minDX<=xr[0] and maxDX>=xr[1]:
                        break

            if not good:
                break
        if good:
            maxArea = area
print(f"Part2: {maxArea}")
