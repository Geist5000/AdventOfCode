from types import LambdaType


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def main(fileName:str):
    lines = loadData(fileName,int)

    last = lines[0]
    inc_count = 0
    dec_count = 0
    same_count = 0
    for n in lines[1:]:
        if last < n:
            inc_count += 1
        elif last > n:
            dec_count += 1
        else:
            same_count += 1
        last = n
    
    print(f"Increased Count: {inc_count}")



if __name__ == "__main__":
    test = False
    if(test):
        fileName = "testInput.txt"
    else:
        fileName = "data.txt"
    main(fileName)