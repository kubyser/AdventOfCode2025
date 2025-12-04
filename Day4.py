from copy import deepcopy

import aoc

data = [s.removesuffix("\n") for s in open("resources/day4_input.txt", "r")]
data, height, width = aoc.stringsArrayToLists(data)
totalAccessibleRolls = 0
running = True
part2 = True
while running:
    newData = deepcopy(data)
    accessibleRolls = 0
    for j in range(height):
        for i in range(width):
            if data[i][j] != '@':
                continue
            neighbours = 0
            for d in aoc.DIRECTION_MOVEMENT:
                c = aoc.addCoords((i, j), aoc.DIRECTION_MOVEMENT[d])
                if c[0] < 0 or c[0] >= width or c[1] < 0 or c[1] >= height:
                    continue
                if data[c[0]][c[1]] == '@':
                    neighbours += 1
                    if neighbours >= 4:
                        break
            if neighbours < 4:
                accessibleRolls += 1
                newData[i][j] = '.'
    totalAccessibleRolls += accessibleRolls
    if accessibleRolls == 0 or not part2:
        running = False
    else:
        data = deepcopy(newData)
print(totalAccessibleRolls)