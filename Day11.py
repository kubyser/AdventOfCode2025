from functools import lru_cache

START = "you"
SERVER = "svr"
TARGET = "out"
PART2_PATHS = [[SERVER, "dac", "fft", TARGET], [SERVER, "fft", "dac", TARGET]]

visited = set()

@lru_cache()
def explore(pos, start, target):
    if pos == target:
        return 1
    if pos not in devices:
        return 0
    numPaths = 0
    for d in devices[pos]:
        res = explore(d, start, target)
        numPaths += res
    return numPaths

@lru_cache()
def exploreWithProblematic(pos, toPass = ""):
    if pos == TARGET:
        if toPass == "":
            print(f"At target and ALL GOOD!")
            return 1
        else:
            #print(f"At target but some are not visited, too bad...")
            return 0
    if pos not in devices:
        return 0
    if toPass != "":
        posCheck = pos+','
        if posCheck in toPass:
            toPass = toPass.replace(posCheck, "")
    numPaths = 0
    for d in devices[pos]:
        res = explore(d, toPass)
        numPaths += res
    return numPaths

data = [s.removesuffix("\n") for s in open("resources/day11_input.txt", "r")]
devices = {}
for s in data:
    s = s.split(": ")
    name = s[0]
    connections = {c for c in s[1].split()}
    if name not in devices:
        devices[name] = set()
    devices[name] = devices[name] | connections
numPaths = explore(START, START, TARGET)
print(f"Part 1: {numPaths}")
totalNumPaths = 0
for path in PART2_PATHS:
    numPaths = 1
    for i, start in enumerate(path[:-1]):
        end = path[i+1]
        res = explore(start, start, end)
        numPaths *= res
    totalNumPaths += numPaths
print(f"Part 2: {totalNumPaths}")

