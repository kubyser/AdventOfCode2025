from copy import deepcopy
from functools import lru_cache

@lru_cache()
def calculateTimelines(pos, dataPos):
    i = dataPos
    if i >= len(data):
        return 1
    while data[i][pos] != '^':
        i += 1
        if i >= len(data):
            return 1
    leftTimelines = calculateTimelines(pos-1, i+1)
    rightTimelines = calculateTimelines(pos+1, i+1)
    return leftTimelines + rightTimelines

data = [s.removesuffix("\n") for s in open("resources/day7_input.txt", "r")]
startPos = data[0].find("S")
beams = {startPos}
numSplits = 0
for s in data[1:]:
    newbeams = set()
    for b in beams:
        if s[b] == '^':
            newbeams.add(b-1)
            newbeams.add(b+1)
            numSplits += 1
        else:
            newbeams.add(b)
    beams = deepcopy(newbeams)
print(numSplits)
numTimelines = calculateTimelines(startPos, 1)
print(numTimelines)