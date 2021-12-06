from types import LambdaType


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    numbers = list(map(int, lines[0].split(",")))
    new_numbers = []
    days = 80
    for day in range(days):
        new_numbers = []
        for n in numbers:
            if n == 0:
                new_numbers.append(6)
                new_numbers.append(8)
            else:
                new_numbers.append(n-1)
        numbers = new_numbers
    return len(numbers)
    

    

if __name__ == "__main__":
    expectedTestOutput = 5934
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
