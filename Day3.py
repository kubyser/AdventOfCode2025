banks = [s.removesuffix("\n") for s in open("resources/day3_input.txt", "r")]
sumJolts = 0

def findBiggestNextDigit(s, length):
    maxC = 0
    maxRes = 0
    for c in s[:-length+1] if length > 1 else s:
        if int(c) > maxC:
            maxC = int(c)
    for i in range(len(s)-length+1):
        c = int(s[i])
        if c == maxC:
            if length > 1:
                res = findBiggestNextDigit(s[i+1:], length-1)
                if res > maxRes:
                    maxRes = res
            break
    bestRes = maxC * pow(10, length-1) + maxRes
    return bestRes

for b in banks:
    maxS = findBiggestNextDigit(b, 12)
    print(f"{b}: {maxS}")
    sumJolts += maxS
print(sumJolts)


