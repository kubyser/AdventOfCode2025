def within(a, r):
    return r[0] <= a and r[1] >= a

data = [s.removesuffix("\n") for s in open("resources/day5_input.txt", "r")]
freshRanges = []
for s in data:
    if s == "":
        break
    freshRanges.append([int(x) for x in s.split("-")])
available= [int(s) for s in data[len(freshRanges)+1:]]
numFresh = sum([1 if any(within(x, r) for r in freshRanges) else 0 for x in available])
print(numFresh)

newRanges = [(freshRanges[0], True)]
for fr in freshRanges[1:]:
    nr = [fr[0], fr[1]]
    for i,(r, isValid) in enumerate(newRanges):
        if not isValid:
            continue
        if within(r[0], nr) and within(r[1], nr):
            newRanges[i] = (r, False)
            continue
        if within(nr[0], r):
            if within(nr[1], r):
                nr = None
            else:
                nr[0] = r[1]+1
        elif within(nr[1], r):
            nr[1] = r[0]-1
        if nr is None or nr[0] > nr[1]:
            break
    if nr is not None and nr[0] <= nr[1]:
        newRanges.append((nr, True))
sumRanges = sum(r[0][1]-r[0][0]+1 for r in newRanges if r[1])
#print(newRanges)
print(sumRanges)