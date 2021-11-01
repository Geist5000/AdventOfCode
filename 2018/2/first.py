from types import LambdaType


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName, countLetters)
    count2 = 0
    count3 = 0
    for l in lines:
        c2 = False
        c3 = False
        for c,count in l.items():
            if(count == 2):
                c2 = True
            elif count == 3:
                c3 = True
        if c2:
            count2+= 1
        if c3:
            count3+= 1
    print(count2*count3)
        

def countLetters(id:str):
    count = {}
    for c in id:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    return count


if __name__ == "__main__":
    test = False
    if(test):
        fileName = "testInput.txt"
    else:
        fileName = "data.txt"
    main(fileName)