from types import LambdaType

opening_parantethes = {
    "(":")",
    "{":"}",
    "[":"]",
    "<":">"
}

closing_parantethes = {
    ")":"(",
    "}":"{",
    "]":"[",
    ">":"<"
}

parantethes_values = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

auto_complete_values = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    scores = list()
    for l_index,l in enumerate(lines):
        para_stack = list()
        error = None
        for c_index,c in enumerate(l):
            if c in opening_parantethes:
                para_stack.append(c)
            elif c in closing_parantethes:
                if para_stack.pop() != closing_parantethes[c]:
                    error = (c_index,c)
                    break
        if not error:
            l_score = 0
            missing = list(map(lambda x: opening_parantethes[x], reversed(para_stack)))
            for c in missing:
                l_score *= 5
                l_score += auto_complete_values[c]
            scores.append(l_score)
    middle_index = len(scores)//2
    return list(sorted(scores))[middle_index]

if __name__ == "__main__":
    expectedTestOutput = 288957
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
