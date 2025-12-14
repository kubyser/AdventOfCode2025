data = [s.removesuffix("\n") for s in open("resources/day12_input.txt", "r")]
lineNum = 0
shapes = {}
while True:
    s = data[lineNum]
    if s[-1] != ':':
        break
    shapeNum = int(s[:-1])
    shapeForm = [x for x in data[lineNum+1:lineNum+4]]
    shapeArea = sum([1 if x == '#' else 0 for sl in shapeForm for x in sl])
    shapes[shapeNum] = (shapeForm, shapeArea)
    lineNum += 5
requirements = []
for s in data[lineNum:]:
    s = s.split(": ")
    dim = s[0].split("x")
    width = int(dim[0])
    height = int(dim[1])
    reqs = s[1].split()
    presents = [int(x) for x in reqs]
    requirements.append((width, height, presents))
print(shapes)
print(requirements)
validatedRequirements = []
for r in requirements:
    totalArea = r[0]*r[1]
    reqArea = sum([shapes[i][1] * x for i, x in enumerate(r[2])])
    #print(f"Total area {totalArea}, required area {reqArea}")
    if totalArea >= reqArea:
        validatedRequirements.append(r)
print(f"{len(validatedRequirements)} are at least not too small")
requirements = validatedRequirements
validatedRequirements = []
for r in requirements:
    totalArea = r[0]*r[1]
    reqArea = 9 * sum(r[2])
    #print(f"Total area {totalArea}, safely big area {reqArea}")
    if totalArea >= reqArea:
        validatedRequirements.append(r)
print(f"{len(validatedRequirements)} are definitely big enough")


