from math import log10

data = [[int(n) for n in s.split("-")] for s in open("resources/day2_input.txt", "r").readline().split(",")]
print(data)
invalidInputs = 0
part2 = True
for d in data:
    print(f"Trying: {d}")
    for n in range(d[0], d[1]+1):
        s = str(n)
        for repetitions in range(2, (len(s)+1) if part2 else 2+1):
            if len(s)%repetitions != 0:
                continue
            patLength = len(s) // repetitions
            pattern = s[:patLength]
            patMatching = True
            for ri in range(1, repetitions):
                if s[patLength*ri:patLength*(ri+1)] != pattern:
                    patMatching = False
                    break
            if patMatching:
                print(f"Invalid: {n}")
                invalidInputs += n
                break
print(invalidInputs)
exit(0)

