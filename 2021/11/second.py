from types import LambdaType
from typing import List


class Cavern(object):

    def __init__(self, lines: list) -> None:
        super().__init__()
        self.octopuses = list()
        self.load_data(lines)
        self.flashed = set()
        self.flash_count = 0

    def charge_all(self):
        
        for x, column in enumerate(self.octopuses):
            for y in range(len(column)):
                self.charge_octopus(x, y)
        all_flashed = False
        if len(self.flashed) == len(self.octopuses) * len(self.octopuses[0]):
            all_flashed = True

        for x, y in self.flashed:
            self.octopuses[x][y] = 0
        self.flashed = set()
        return all_flashed

    def charge_octopus(self, x, y):
        v = self.octopuses[x][y]
        if v >= 9:
            self.flash_octopus(x, y)
        else:
            self.octopuses[x][y] += 1

    def flash_octopus(self, x, y):
        if (x, y) not in self.flashed:
            self.flashed.add((x, y))
            self.flash_count += 1
            for n in self.get_neighbours(x, y):
                self.charge_octopus(*n)

    def get_neighbours(self, x: int, y: int):
        coords = set()
        for x_diff in range(-1, 2):
            for y_diff in range(-1, 2):
                new_x = x + x_diff
                new_y = y + y_diff
                if x_diff == y_diff == 0:
                    continue
                if new_x < 0 or new_y < 0:
                    continue
                if new_x >= len(self.octopuses) or new_y >= len(self.octopuses[new_x]):
                    continue

                coords.add((new_x, new_y))

        return coords

    def load_data(self, lines: list):
        for y, l in enumerate(lines):
            for x, c in enumerate(map(int, l)):
                if y == 0:
                    self.octopuses.append(list())
                self.octopuses[x].append(c)


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    cavern = Cavern(lines)
    iteration = 1
    while not cavern.charge_all():
        iteration += 1
    
    return iteration


if __name__ == "__main__":
    expectedTestOutput = 195

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
