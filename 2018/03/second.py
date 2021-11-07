from os import O_SHORT_LIVED
from types import LambdaType
import re
from dataclasses import dataclass
from typing import List, Match, Set


@dataclass
class Claim:
    identifier: int
    x: int
    y: int
    width: int
    height: int

    def forEach(self):
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                yield x, y

    def isLine(self):
        return self.width == 0 or self.height == 0

    def doesOverlapp(self, other: 'Claim'):
        xDiff = self.x - other.x
        yDiff = self.y - other.y

        return (
            (
                xDiff == 0 or
                xDiff > 0 and xDiff < other.width or
                xDiff < 0 and abs(xDiff) < self.width
            ) and (
                yDiff == 0 or
                yDiff > 0 and yDiff < other.height or
                yDiff < 0 and abs(yDiff) < self.height
            )
        )


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    lines = loadData(fileName)

    claims: List[Claim] = list()

    noOverlapClaims: List[Claim] = list()
    # possible optimisations:
    # chunk claims together so I can access only the claims which could possibly overlap and check if they really are
    # merge claims together if 

    for index, l in enumerate(lines):
        claim = parseClaim(regex, l)

        overlapped = False
        for c in claims:
            if claim.doesOverlapp(c):
                if c in noOverlapClaims:
                    noOverlapClaims.remove(c)
                overlapped = True
        claims.append(claim)
        if not overlapped:
            noOverlapClaims.append(claim)
    return noOverlapClaims[0].identifier


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
