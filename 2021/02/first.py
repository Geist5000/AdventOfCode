from types import LambdaType


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName)
    for index,l in enumerate(lines):
        print(l)


if __name__ == "__main__":
    test = True
    if(test):
        fileName = "testInput.txt"
    else:
        fileName = "data.txt"
    main(fileName)