lines = []


with open("testInput.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))
