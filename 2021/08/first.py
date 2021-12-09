from types import LambdaType


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    count = 0
    for index, l in enumerate(lines):
        blueprint, value = l.split(" | ")
        blueprints = blueprint.split(" ")
        values = value.split(" ")
        count += sum(map(lambda x: 1 if len(x) in [2,3,4,7] else 0,values))

    return count


if __name__ == "__main__":
    expectedTestOutput = 26

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
