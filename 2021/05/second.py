from types import LambdaType
from itertools import zip_longest
import re


class Area(object):
    def __init__(self,cb: LambdaType = lambda x: True) -> None:
        super().__init__()
        self.d = {}
        self.count_cb = cb
        self.count = 0

    def increment(self, x: int, y: int):
        if x not in self.d:
            self.d[x] = {}
        x_area = self.d[x]
        if y not in x_area:
            x_area[y] = 0
        already_counted = self.count_cb(x_area[y])
        x_area[y] += 1
        if not already_counted and self.count_cb(x_area[y]):
            self.count += 1


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    line_regex = re.compile("(\d+),(\d+) -> (\d+),(\d+)")
    interceptions = 0
    area = Area(lambda x: x >= 2)
    for index, l in enumerate(lines):
        line_match = line_regex.fullmatch(l)

        if line_match is not None:
            x1, y1, x2, y2 = map(int, line_match.groups())
            # check if line is horizontal or vertical
        
            x_step = -1 if x1>x2 else 1
            y_step = -1 if y1>y2 else 1
            for x, y in zip_longest(range(x1, x2+x_step, x_step), range(y1, y2+y_step, y_step)):
                if x is None:
                    x = x2
                if y is None:
                    y = y2
                area.increment(x, y)
        else:
            print("WARNING line had different formatting than expected:" + l)
    return area.count


if __name__ == "__main__":
    expectedTestOutput = 12

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
