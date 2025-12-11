from copy import deepcopy
from functools import lru_cache


def findCandidateButtons(lights, target, pushedButtons, buttonsToTry, depth):
    toTry = []
    lightToChange = [i for i,c in enumerate(lights) if c!=target[i]]
    candButtons = [b for b in buttonsToTry if any(bc in lightToChange for bc in b)]
    for b in candButtons:
        newButtons = deepcopy(buttonsToTry)
        newButtons.pop(b)
        newPushedButtons = pushedButtons + [buttonsToTry[b]]
        test = (lights, b, newPushedButtons, newButtons, depth+1)
        toTry.append(test)
    return toTry

def findCandidateButtonsPart2(jolts, target, pushedButtons, buttons, depth):
    toTry = []
    #joltsToChange = [i for i,c in enumerate(jolts) if c<target[i]]
    joltsToChange = [0] if jolts[0]<target[0] else []
    joltsNotToChange = [i for i,c in enumerate(jolts) if c>=target[i]]
    candButtons = [b for b in buttons if any(bc in joltsToChange for bc in b)
                   and not any(bc in joltsNotToChange for bc in b)]
    for b in candButtons:
        newPushedButtons = pushedButtons + [buttons[b]]
        test = (jolts, b, newPushedButtons, depth+1)
        toTry.append(test)
    return toTry

def pushButton(before, button):
    after = ""
    for i in range(len(before)):
        if i in button:
            after += '.' if before[i] == '#' else '#'
        else:
            after += before[i]
    return after

def pushButtonJolts(before, button):
    after = [0] * len(before)
    for i in range(len(before)):
        if i in button:
            after[i] = before[i] + 1
        else:
            after[i] = before[i]
    return after

def generateCombinations(target, sum, buttons, usedButtons = {}):
    b2 = set(buttons)
    b = b2.pop()
    if len(b2) == 0:
        ub2 = usedButtons.copy()
        ub2[b] = sum
        newTarget = calculateNewTarget(target, ub2)
        if any(x<0 for x in newTarget):
            return []
        return [ub2]
    allNewCombinations = []
    for i in range(sum+1):
        ub2 = usedButtons.copy()
        ub2[b] = i
        newTarget = calculateNewTarget(target, ub2)
        if any(x<0 for x in newTarget):
            break
        newCombinations = generateCombinations(target, sum-i, b2, ub2)
        allNewCombinations += newCombinations
    return allNewCombinations

def calculateNewTarget(target, combination):
    newTarget = list(target)
    for b in combination:
        rep = combination[b]
        if rep != 0:
            for pos in b:
                newTarget[pos] -= rep
    return tuple(newTarget)


@lru_cache
def solveTask(target, buttons, first=True): #, curCost=0, curMinCost=None):
    if all(x == 0 for x in target):
        return 0
    validButtons = [b for b in buttons if not any(target[i] == 0 for i in b)]
    targetValid = all(any(i in b for b in validButtons) for i,x in enumerate(target) if x != 0)
    if not targetValid:
        return None
    maxItem = max([x for x in target])
    #if curMinCost is not None and curCost + maxItem >= curMinCost:
    #    return None
    #minItem = min([x for x in target if x != 0])
    nPos = list(target).index(maxItem)
    eligibleButtons = [b for b in buttons if nPos in b and not any(target[i] == 0 for i in b)]
    #print(f"target {target} MinItem = {minItem} eligible buttons {eligibleButtons}")
    if len(eligibleButtons) == 0:
        return None
    combinations = generateCombinations(target, maxItem, eligibleButtons)
    numCombinations = len(combinations)
    print(f"Combinations {numCombinations}")
    cycleSize = numCombinations // 500
    counter = 0
    minCost = None
    for nc, comb in enumerate(combinations):
        newTarget = calculateNewTarget(target, comb)
        if any(x<0 for x in newTarget):
            continue
        #if first:
        #    maxItem = max([x for x in target])
        #    if minCost is not None and minItem+maxItem >= minCost:
        #        continue
        cost = solveTask(tuple(newTarget), buttons, False) #, curCost+minItem, minCost)
        if first:
            if (counter := counter+1) == cycleSize:
                print(f"Progress {round(nc/numCombinations*100, 2)}% Trying combination {nc}/{numCombinations} target {newTarget}, cur min cost = {minCost}")
                counter = 0
        if cost is not None and (minCost is None or cost+maxItem < minCost):
            minCost = cost+maxItem
    if minCost is None:
        return None
    return minCost

data = [s.removesuffix("\n") for s in open("resources/day10_input.txt", "r")]
tasks = []
for s in data:
    s = s.split()
    buttons = tuple(tuple(int(c) for c in bs[1:-1].split(",")) for bs in s[1:-1])
    jolts = tuple((int(c) for c in s[-1][1:-1].split(",")))
    task = (s[0][1:-1], buttons, jolts)
    tasks.append(task)
totalPushes = 0

for taskNum, task in enumerate(tasks):
    target = task[2]
    buttons = task[1]
    minPushes = solveTask(target, buttons)
    totalPushes += minPushes
    print(f"Task {taskNum} Min pushes: {minPushes}")

    #exit(0)
print(f"Total pushes: {totalPushes}")
exit(0)

while True:
    depth = 0
    toTry = findCandidateButtonsPart2(jolts, target, [], buttons, 0)
    while len(toTry) > 0:
        jolts, button, pushedButtons, depth = toTry.pop(0)
        #print(f"trying depth {depth} buttons {pushedButtons}")
        if depth > maxDepth:
            print(f"Reached depth {depth}")
            maxDepth = depth
        newJolts = pushButtonJolts(jolts, button)
        strNewJolts = str(newJolts[0])
        if strNewJolts in joltsCache:
            continue
        joltsCache.add(strNewJolts)
        print(f"Test: depth {depth} target {target}, jolts {newJolts} pushes {pushedButtons}")
        #if tuple(newJolts) == target:
        if newJolts[0] == target[0]:
            print(f"Hooray! Machine {taskNum} min pushes: {depth}, pushed buttons: {pushedButtons}")
            totalPushes += depth
            break
        newToTry = findCandidateButtonsPart2(newJolts, target, pushedButtons, buttons, depth)
        toTry = toTry + newToTry
    break
print(f"Total pushes: {totalPushes}")
exit(0)

for taskNum, task in enumerate(tasks):
    cache = set()
    lights = '.' * len(task[0])
    target = task[0]
    buttons = task[1]
    buttonsToTry = buttons
    depth = 0
    toTry = findCandidateButtons(lights, target, [], buttonsToTry, 0)
    while len(toTry) > 0:
        lights, button, pushedButtons, buttonsToTry, depth = toTry.pop(0)
        cacheButtons = pushedButtons
        cacheButtons.sort()
        cacheButtons = str(cacheButtons)
        if cacheButtons in cache:
            continue
        cache.add(cacheButtons)
        newLights = pushButton(lights, button)
        if newLights == target:
            print(f"Hooray! Machine {taskNum} min pushes: {depth}, pushed buttons: {pushedButtons}")
            totalPushes += depth
            break
        newToTry = findCandidateButtons(newLights, target, pushedButtons, buttonsToTry, depth)
        toTry = toTry + newToTry
print(f"Total pushes: {totalPushes}")