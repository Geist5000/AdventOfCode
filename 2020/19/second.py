import re

rules = {}


def matchesAll(alt, value):  # 1 2 8
    global rules

    index = 0
    allmatches = []
    rule = rules[int(alt[0])]
    listLength = rule.applies(value[index:])
    if(len(alt)>1):
        for length in listLength:
            allmatches.extend(matchesAll(alt[1:], value[length:]))
    else:
        allmatches.extend(listLength)
    return allmatches


class Rule:

    def __init__(self, rule) -> None:
        self.rule = rule

    def applies(self, value):
        if self.hasDependencies():
            dependencies = self.getDependencies()
            matching = []
            for alt in dependencies:
                matches = matchesAll(alt, value)
                matching.extend(matches)
            return matching

        else:
            if value.startswith(self.getRuleChar()):
                return [1]
            else:
                return []

    def getRuleChar(self):
        return re.search("\"([a-zA-Z]+)\"", self.rule).group(1)

    def getDependencies(self):
        return [i.split() for i in self.rule.split("|")]

    def hasDependencies(self):
        return "\"" not in self.rule


lines = []


with open("testInput.txt") as f:
    lines = list(map(lambda l: l.replace("\n", ""), f.readlines()))


valid = []

for l in lines:
    regex = r"^([0-9]+):(.*)$"
    m = re.match(regex, l)

    if(m):
        rules[int(m.group(1))] = Rule(m.group(2))
    elif(len(l) > 0):
        if any(map(lambda x: x == len(l), rules[0].applies(l))):
            valid.append(l)
print(len(valid))
