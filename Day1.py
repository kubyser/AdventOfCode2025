from math import trunc

data = [int(n[1:]) * (-1 if n[0]=="L" else 1) for n in [l.removesuffix("\n") for l in open("resources/day1_input.txt", "r")]]
pos = 50
zeroCount_part1 = 0
zeroCount_part2 = 0
for n in data:
    newPos = (pos + n) % 100
    realPos = pos + n
    if newPos == 0:
        zeroCount_part1 += 1
    zeroCount_part2 += trunc((abs(realPos)-1) / 100) + (1 if pos*realPos < 0 else 0) + (1 if newPos == 0 else 0)
    pos = newPos
print(f"Part 1: {zeroCount_part1}")
print(f"Part 2: {zeroCount_part2}")