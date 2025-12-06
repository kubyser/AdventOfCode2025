import math

rawData = [s.removesuffix("\n") for s in open("resources/day6_input.txt", "r")]
data = [s.split() for s in rawData]
totalSum = 0
for i, op in enumerate(data[-1]):
    if op == '+':
        res = sum(int(s[i]) for s in data[:-1])
    else:
        res = math.prod(int(s[i]) for s in data[:-1])
    totalSum += res
print(f"Part1: {totalSum}")
maxLengths = [max(len(s[i]) for s in data[:-1]) for i in range(len(data[0]))]
cepNumbers = [[0] * length for length in maxLengths]
for line in rawData[:-1]:
    pos = 0
    for num, length in enumerate(maxLengths):
        for numInPos in range(length):
            if line[pos] != ' ':
                cepNumbers[num][numInPos] *= 10
                cepNumbers[num][numInPos] += int(line[pos])
            pos += 1
            if pos >= len(line):
                break
        pos += 1
totalSum2 = sum(sum(nums) if op == '+' else math.prod(nums) for op, nums in zip(data[-1], cepNumbers))
print(f"Part2: {totalSum2}")
