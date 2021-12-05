from types import LambdaType


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    floor = 0
    for index,l in enumerate(lines):
        for pos,c in enumerate(l):
            floor += 1 if c == "(" else -1
            if floor == -1:
                break

    return pos + 1

if __name__ == "__main__":
    expectedTestOutput = 5
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
