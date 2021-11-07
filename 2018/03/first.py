from types import LambdaType
import re
from dataclasses import dataclass


@dataclass
class Claim:
    id: int
    x: int
    y: int
    width: int
    height: int

    def forEach(self):
        for x in range(self.x, self.x+self.width):
            for y in range(self.y, self.y+self.height):
                yield x, y


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    lines = loadData(fileName)
    claims = list()
    xDict = dict()
    overlappCount = 0
    for index, l in enumerate(lines):
        claim = parseClaim(regex, l)
        for x, y in claim.forEach():
            if x not in xDict.keys():
                xDict[x] = dict()
            yDict:dict = xDict[x]
            if y in yDict:
                if yDict[y] == 1:
                    overlappCount += 1
                yDict[y]+=1
                claim.overlappCount += 1
            else:
                yDict[y] = 1
    return overlappCount


def parseClaim(regex: re.Pattern, claim: str):
    match = regex.fullmatch(claim)
    return Claim(int(match[1]), int(match[2]), int(match[3]), int(match[4]), int(match[5]))


if __name__ == "__main__":
    test = False
    if(test):
        fileName = "testInput.txt"
    else:
        fileName = "data.txt"
    print(main(fileName))
