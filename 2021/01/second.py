from types import LambdaType


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName, int)

    last = None
    inc_count = 0
    dec_count = 0
    same_count = 0
    for n in zip(lines[:-2],lines[1:-1],lines[2:]):
        s = sum(n)
        if last is None:
            last = s
            continue
        
        if last < s:
            inc_count += 1
        elif last > s:
            dec_count += 1
        else:
            same_count += 1
        last = s

    print(f"Increased Count: {inc_count}")


if __name__ == "__main__":
    test = False
    if(test):
        fileName = "testInput.txt"
    else:
        fileName = "data.txt"
    main(fileName)
