def within(a, r):
    return r[0] <= a and r[1] >= a

data = [s.removesuffix("\n") for s in open("resources/day5_input.txt", "r")]
freshRanges = []
available = []
for s in data:
    if s == "":
        break
    ss = [int(x) for x in s.split("-")]
    freshRanges.append(ss)
for s in data[len(freshRanges)+1:]:
    available.append(int(s))
numFresh = 0
for x in available:
    fresh = False
    for r in freshRanges:
        if x >= r[0] and x <= r[1]:
            fresh = True
            break
    if fresh:
        numFresh += 1
print(numFresh)

newRanges = [(freshRanges[0], True)]
for fr in freshRanges[1:]:
    nr = [fr[0], fr[1]]
    for i,rRec  in enumerate(newRanges):
        r = rRec[0]
        isValid = rRec[1]
        if not isValid:
            continue
        if within(r[0], nr) and within(r[1], nr):
            rRec = (r, False)
            newRanges[i] = rRec
            continue
        if within(nr[0], r):
            if within(nr[1], r):
                nr = []
            else:
                nr[0] = r[1]+1
        elif within(nr[1], r):
            nr[1] = r[0]-1
        if len(nr) == 0 or nr[0] > nr[1]:
            break
    if len(nr) > 0 and nr[0] <= nr[1]:
        newRanges.append((nr, True))
sumRanges = sum(r[0][1]-r[0][0]+1 for r in newRanges if r[1])
print(newRanges)
print(sumRanges)