from types import LambdaType
from typing import Iterable, Tuple
from itertools import chain


class HeightMap(object):
    def __init__(self) -> None:
        super().__init__()
        self.width = -1
        self.height = -1
        self.map = []
        self.max_heigth_locs = []

    def load_data(self, lines: list):
        self.map = []
        self.max_heigth_locs = []
        for index, row in enumerate(lines):
            self.height = index
            for i, c in enumerate(row):
                self.width = i
                if index == 0:
                    self.map.append([])
                self.map[i].append(int(c))
                if self.map[i][index] == 9:
                    self.max_heigth_locs.append((i, index))
        self.width += 1
        self.height += 1
        self.low_points = []

    def get_low_points(self) -> list:
        visited_set = set()

        def rec_func(x: int, y: int) -> list[tuple[int, int]]:
            neighbours = self.get_neighbours(x, y)
            visited_set.add((x, y))
            smaller_neighbours_count = 0
            low_points = []
            c_v = self.get_point(x, y)
            for n in neighbours:
                
                v = self.get_point(*n)
                if v <= c_v:
                    smaller_neighbours_count += 1
                    if n in visited_set:
                        continue
                    low_points.extend(rec_func(*n))
            if smaller_neighbours_count == 0:
                return [(x, y)]
            else:
                return low_points
        self.low_points = list(chain.from_iterable(map(lambda h_point: rec_func(*h_point), self.max_heigth_locs)))
        return self.low_points

    def is_x_in_range(self, x):
        return x >= 0 and x < self.width

    def is_y_in_range(self, y):
        return y >= 0 and y < self.height

    def get_point(self, x, y):
        if self.is_x_in_range(x) and self.is_y_in_range(y):
            return self.map[x][y]
        raise Exception("Out of bounds exception")

    def get_neighbours(self, x: int, y: int):
        # TODO check if smaller than zero or bigger than width or height
        neighbours = []
        if x > 0:
            neighbours.append((x-1, y))
        if x < self.width-1:
            neighbours.append((x+1, y))
        if y > 0:
            neighbours.append((x, y-1))
        if y < self.height-1:
            neighbours.append((x, y+1))
        return neighbours
    def __repr__(self) -> str:
        lines = ""
        for y in range(self.height):
            l = ""
            for x in range(self.width):
                v = str(self.get_point(x,y))
                l += f"[{v}]" if (x,y) in self.low_points else f" {v} "
            lines += l + "\n"

        return lines


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    hm = HeightMap()
    hm.load_data(lines)
    low_points = hm.get_low_points()  
    print(hm)

    return calc_risk_lvl(hm,low_points)


def calc_risk_lvl(height_map: HeightMap, low_points: Iterable[Tuple[int, int]]):
    return sum(map(lambda x: height_map.get_point(*x), low_points)) + len(low_points)


if __name__ == "__main__":
    expectedTestOutput = 15

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
