from os import path
from types import LambdaType
import re
from typing import List

line_regex = re.compile("([a-zA-Z]+)-([a-zA-Z]+)")

class Cave(object):
    def __init__(self, name:str) -> None:
        super().__init__()
        self.neighbours:set[Cave] = set()
        self.name = name
    def is_big(self):
        return self.name[0].isupper()

    def __repr__(self) -> str:
        return f"{self.name}({len(self.neighbours)})"

class Graph(object):
    def __init__(self,lines:list) -> None:
        super().__init__()
        self.caves:dict[str,Cave] = {}
        self.load_caves(lines)

    def load_caves(self,lines:list):
        for l in lines:
            match = line_regex.fullmatch(l)
            if match:
                first_cave_name = match.group(1)
                second_cave_name = match.group(2)
                if first_cave_name not in self.caves:
                    self.caves[first_cave_name] = Cave(first_cave_name)
                if second_cave_name not in self.caves:
                    self.caves[second_cave_name] = Cave(second_cave_name)
                
                first_cave = self.caves[first_cave_name]
                second_cave = self.caves[second_cave_name]

                first_cave.neighbours.add(second_cave)
                second_cave.neighbours.add(first_cave)

            else:
                print(f"WARNING, regex didn't match on: {l}")


def loadData(fileName:str, mapFunc: LambdaType = lambda x: x):
    
    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n","")),f.readlines()))

def rec(path:List[Cave]):
    current = path[-1]
    visited = dict()

    for c in path:
        if c not in visited:
            visited[c] = 0
        visited[c] += 1

    already_visited_twice = any(map(lambda x: x[1]==2 and not x[0].is_big(), visited.items()))
        
    found_paths = []
    for n in filter(lambda neighbour: neighbour not in visited or not already_visited_twice or neighbour.is_big(), current.neighbours):
        if n.name == "start":
            continue
        
        if n.name == "end":
            found_paths.append(path+[n])
        else:
            found_paths.extend(rec(path+[n]))
    return found_paths

def main(fileName:str):
    lines = loadData(fileName)
    graph = Graph(lines)
    paths  = rec([graph.caves["start"]])
    return len(paths)

if __name__ == "__main__":
    expectedTestOutput = 103
    
    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
