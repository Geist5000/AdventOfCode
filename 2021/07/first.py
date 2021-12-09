from types import LambdaType
from statistics import median

def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    m = round(median(map(int, lines[0].split(","))))
    diff = 0
    for i in map(int, lines[0].split(",")):
        diff += abs(m-i)
    

    return diff

if __name__ == "__main__":
    expectedTestOutput = 37
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
