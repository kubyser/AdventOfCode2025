from copy import deepcopy

def reduce(equations):
    while True:
        reduced = False
        restart = False
        for i, (elements, val, source) in enumerate(equations):
            for j, (testElements, testVal, testSource) in enumerate(equations):
                if j == i:
                    continue
                if any(x not in testElements for x in elements):
                    continue
                if val > testVal:
                    return None
                if elements == testElements and val != testVal:
                    return None
                reduced = True
                testElements -= elements
                if len(testElements) == 0:
                    equations.pop(j)
                    restart = True
                    break
                else:
                    equations[j] = (testElements, testVal - val, "UPD")
            if restart:
                break
        if not reduced:
            break
    return equations

def solve(equations):
    global minValue
    equations = deepcopy(equations)
    equations = reduce(equations)
    if equations is None:
        return None
    if all(len(x[0]) == 1 for x in equations):
        summ = sum([x[1] for x in equations])
        if minValue is None or minValue > summ:
            minValue = summ
        #print(f"Solved! {equations} Sum={summ} minValue={minValue}")
        return equations
    minEq = min([x for x in equations if len(x[0]) > 1], key = lambda x: x[1])
    for firstVar in minEq[0]:
        break
    #print(minEq, firstVar)
    maxValue = min([x[1] for x in equations if firstVar in x[0]])
    equations.append(({firstVar}, None, "NEW"))
    for newValue in range(maxValue+1):
        equations[-1] = ({firstVar}, newValue, "NEW")
        solve(equations)
    #print("Tried all")
    return equations

data = [s.removesuffix("\n") for s in open("resources/day10_input.txt", "r")]
tasks = []
for s in data:
    s = s.split()
    bs = s[1:-1]
    ts = s[-1][1:-1]
    target = [int(x) for x in ts.split(",")]
    buttons = []
    for b in bs:
        button = set()
        for x in b[1:-1].split(","):
            button.add(int(x))
        buttons.append(button)
    tasks.append((target, buttons))
totalSum = 0
for nt, (target, buttons) in enumerate(tasks): #[7:8]):
    print(f"========= Task {nt} ============")
    minValue = None
    equations = []
    for pos,x in enumerate(target):
        elements = {i for i, b in enumerate(buttons) if pos in b}
        equations.append((elements, x, "ORIG"))
    equations = solve(equations)
    print(f"task {nt} completed, minValue={minValue}")
    totalSum += minValue
print(totalSum)



