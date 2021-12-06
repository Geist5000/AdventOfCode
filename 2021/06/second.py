from types import LambdaType
from itertools import count, zip_longest


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    counter = {}
    for n in map(int, lines[0].split(",")):
        if n not in counter:
            counter[n] = 0
        counter[n] += 1
    breeding_time = {}
    days = 256

    for day in range(days):
        day_offset = day % 7
        if day_offset not in counter:
            counter[day_offset] = 0
        c = counter[day_offset]
        breeding_time[(day_offset+2) % 7] = c

        if day_offset in breeding_time:
            counter[day_offset] += breeding_time[day_offset]
            breeding_time[day_offset] = 0

    return sum(counter.values()) + sum(breeding_time.values())


if __name__ == "__main__":
    expectedTestOutput = 26984457539

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
