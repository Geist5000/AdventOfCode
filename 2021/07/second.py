import numbers
from types import LambdaType
from statistics import median

def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    numbers = list(map(int, lines[0].split(",")))
    
    return min(map(lambda x: fuel(x,numbers),range(min(numbers),max(numbers)+1)))

def fuel(pos:int, ints:list[int]):
    diff = 0
    for i in ints:
        diff += (abs(pos-i)+1)*(abs(pos-i)/2.0)
    return diff


if __name__ == "__main__":
    expectedTestOutput = 168
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
