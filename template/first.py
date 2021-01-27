lines = []


with open("testInput.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))


for l in lines:
    print(l)
