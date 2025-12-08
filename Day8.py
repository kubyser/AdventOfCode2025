import math
from time import time

data = [s.removesuffix("\n") for s in open("resources/day8_input.txt", "r")]
coords = [(int(s.split(',')[0]), int(s.split(',')[1]), int(s.split(',')[2])) for s in data]
connections = {c: set() for c in coords}
circuits = {i:{c} for i,c in enumerate(coords)}
circMap = {c:i for i,c in enumerate(coords)}
numIterations = 1000
startTime = time()
distances = [((math.pow(first[0]-second[0], 2) +
               math.pow(first[1]-second[1], 2) +
               math.pow(first[2]-second[2], 2)), first, second) for a,first in enumerate(coords[:-1]) for second in coords[a+1:]]
distances.sort(key = lambda x: x[0], reverse=True)
i = 0
#for i in range(numIterations):
while True:
#    print(f"iteration {i}")
    minD, first, second = distances.pop()
    connections[first].add(second)
    if (i := i+1) == numIterations:
        sizes = [len(circuits[c]) for c in circuits]
        sizes.sort()
        res = math.prod(sizes[-3:])
        print(f"Part 1 res: {res}")
    if circMap[first] == circMap[second]:
        continue
    newCirc = circMap[first]
    oldCirc = circMap[second]
    for c in circuits[circMap[second]]:
        circuits[newCirc].add(c)
        circMap[c] = newCirc
    circuits.pop(oldCirc)
    if len(circuits) == 1:
        res = first[0] * second[0]
        print(f"Part 2 res: {res}")
        break
endTime = time()
print(f"Elapsed time: {endTime-startTime}")
