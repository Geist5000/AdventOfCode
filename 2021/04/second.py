from types import LambdaType
import re
from typing import Tuple


class BingoBoard(object):
    def __init__(self, bingo_rows: list[list[int]]) -> None:
        super().__init__()
        self.rows = bingo_rows
        self.width = len(self.rows[0])
        self.heigth = len(self.rows)
        self.numbers_dict = {}
        self.sum_all = 0
        self.__build_dict()
        self.marked = []

    def __build_dict(self):
        """fills the dict at self.numbers_dict with all numbers as keys and an array of all locations in the board this numberis present"""
        self.numbers_dict = {}
        self.sum_all = 0
        for y, r in enumerate(self.rows):
            for x, n in enumerate(r):
                self.sum_all += n
                if n not in self.numbers_dict:
                    self.numbers_dict[n] = []
                self.numbers_dict[n].append((y, x))

    def mark_number(self, number: int) -> bool:
        """Marks number on board, if the board did win True is returned, False otherwise"""
        if number in self.numbers_dict:
            self.marked.append(number)
            locations = self.numbers_dict[number]
            for loc in locations:
                if self.check_if_won(loc):
                    return True
        return False

    def check_if_won(self, loc: Tuple[int, int]):
        y,x = loc
        if self.check_line(loc, 1, 0):
            return True
        if self.check_line(loc, 0, 1):
            return True
        return False

    def check_line(self, loc: Tuple[int, int], x_speed: int, y_speed: int):
        # walk left
        y, x = loc
        while(self.is_inbound((y, x))):
            n = self.rows[y][x]
            if n not in self.marked:
                return False
            y += y_speed*-1
            x += x_speed*-1
        y, x = loc
        y += y_speed
        x += x_speed

        # walk right
        while(self.is_inbound((y, x))):
            n = self.rows[y][x]
            if n not in self.marked:
                return False
            y += y_speed
            x += x_speed
        # all numbers are marked, so board did win
        return True

    def is_inbound(self, loc: Tuple[int, int]):
        y, x = loc
        return y >= 0 and y < self.heigth and x >= 0 and x < self.width
    def sum_marked(self):
        s = 0
        for n in self.marked:
            s += n * len(self.numbers_dict[n])
        return s
    
    def sum_unmarked(self):
        return self.sum_all - self.sum_marked()
    def score(self):
        return self.marked[-1] * self.sum_unmarked()



def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    bingo_row_regex = re.compile("\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)")
    drawn_numbers = list(map(int, lines[0].split(",")))
    boards:list[BingoBoard] = list()
    bingo_rows = []
    for index, l in enumerate(lines[2:]):
        match = bingo_row_regex.fullmatch(l)
        if match is None:
            boards.append(BingoBoard(bingo_rows))
            bingo_rows = []
            continue
        row = [n for n in map(int, match.groups())]
        bingo_rows.append(row)

    
    boards.append(BingoBoard(bingo_rows))

    for number in drawn_numbers:
        to_delte = []
        for b in boards:
            if b.mark_number(number):
                to_delte.append(b)
        if len(to_delte) == len(boards):
            return to_delte[-1].score()
        else:
            for d in to_delte:
                boards.remove(d)
    

    return 0


if __name__ == "__main__":
    expectedTestOutput = 1924

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
