from types import LambdaType


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName, int)

    last = None
    last_entries = []
    inc_count = 0
    dec_count = 0
    same_count = 0
    for n in lines:
        last_entries.append(n)
        if len(last_entries) == 4:
            last_entries.pop(0)
        elif len(last_entries)<3:
            continue
        
        s = sum(last_entries)
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
