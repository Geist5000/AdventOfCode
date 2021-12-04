from types import LambdaType


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    # if one is present more than this count it is most common
    count = len(lines)/2
    width = len(lines[0])
    most_bit_bin = ""
    minor_bit_bin = ""
    for i in range(width):
        ones = 0
        for index, l in enumerate(lines):
            if l[i] == "1":
                ones += 1
            if ones > count:
                break
        most_bit_bin += "1" if ones > count else "0"
        minor_bit_bin += "0" if ones > count else "1"
    most_bit = int(most_bit_bin,2)
    minor_bit = int(minor_bit_bin,2)

    return most_bit * minor_bit


if __name__ == "__main__":
    expectedTestOutput = 198

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
