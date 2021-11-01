from types import LambdaType
from typing import Dict, List


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    tree = {}
    addWord(lines.pop(),tree)
    for l in lines:
        result = search(l,tree)
        if result is not None:
            w = result[0]
            t = result[1]
            if alreadyExistsInAny(w[1:],t.values()):
                i = len(l) - len(w)
                print(l[:i] + w[1:])
                exit(0)
            addWord(w,t)


def search(word:str,tree:dict):
    """Go down the tree until a character is missing
    
    returns the current tree and the remaing word (so basically the arguments of the current function call"""
    if(len(word) == 0):
        return None
    char = word[0]
    if char in tree.keys():
        return search(word[1:],tree[char])
    else:
        return (word,tree)


def alreadyExistsInAny(word:str,trees:List[Dict]):
    return any(map(lambda x: alreadyExists(word,x),trees))

def alreadyExists(word:str, tree:dict):
    """Checks of given word already exists in given tree"""
    if(len(word) == 0):
        return True
    else:
        char = word[0]
        if char in tree.keys():
            return alreadyExists(word[1:],tree[char])
        else:
            return False

def addWord(word:str, tree:dict):
    """Add given word to the given tree"""
    char = word[0]
    if char not in tree.keys():
        tree[char] = {}
    
    if len(word) > 1:
        addWord(word[1:],tree[char])


if __name__ == "__main__":
    test = False
    if(test):
        fileName = "testInput.txt"
    else:
        fileName = "data.txt"
    main(fileName)
