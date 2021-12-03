from types import LambdaType
import re


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    regex = re.compile("(forward|down|up) (-?\d+)")
    x = 0
    y = 0
    aim = 0
    for index,l in enumerate(lines):
        ma = regex.fullmatch(l)
        action = ma.group(1)
        amount = int(ma.group(2))
        if action == "forward":
            x += amount
            y += aim * amount
        elif action == "down":
            aim += amount
        elif action == "up":
            aim -= amount
    print(f"{x} * {y} = {x*y}")


if __name__ == "__main__":
    test = True
    if(test):
        fileName = "testInput.txt"
    else:
        fileName = "data.txt"
    main(fileName)