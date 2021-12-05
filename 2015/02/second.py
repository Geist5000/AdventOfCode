from types import LambdaType


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    all_areas = 0
    all_ribbon_length = 0
    for index,l in enumerate(lines):
        dimensions = list(map(int, l.split("x")))
        l,w,h = dimensions
        sites = [l*w,l*h,w*h]

        area = sum(sites)*2 + min(sites)
        all_areas += area

        ribbon_length = l*w*h + sum(dimensions) * 2 - max(dimensions)*2
        all_ribbon_length += ribbon_length

    return all_ribbon_length

if __name__ == "__main__":
    expectedTestOutput = 48
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
