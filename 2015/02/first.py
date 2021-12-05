from types import LambdaType


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    all_areas = 0
    for index,l in enumerate(lines):
        l,w,h = map(int, l.split("x"))
        sites = [l*w,l*h,w*h]

        area = sum(sites)*2 + min(sites)
        all_areas += area

    return all_areas

if __name__ == "__main__":
    expectedTestOutput = 101
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
