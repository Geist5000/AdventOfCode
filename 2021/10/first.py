from types import LambdaType

opening_parantethies = {
    "(":")",
    "{":"}",
    "[":"]",
    "<":">"
}

closing_parantethies = {
    ")":"(",
    "}":"{",
    "]":"[",
    ">":"<"
}

parantethies_values = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    score = 0
    for index,l in enumerate(lines):
        error = has_syntax_error(l)
        if error:
            i, c = error
            score += parantethies_values[c]
    return score


def has_syntax_error(line:str):
    para_stack = list()
    for index,c in enumerate(line):
        if c in opening_parantethies:
            para_stack.append(c)
        elif c in closing_parantethies:
            if para_stack.pop() != closing_parantethies[c]:
                return (index,c)
            

    return None

if __name__ == "__main__":
    expectedTestOutput = 26397
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
