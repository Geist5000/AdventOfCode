import re

rules = {}


def matchesAll(alt, value):
    global rules
    index = 0
    for ruleId in alt:
        rule = rules[int(ruleId)]
        l, valid = rule.applies(value[index:])
        index += l
        if not valid:
            return 0,False
    return index,True


class Rule:

    def __init__(self, rule) -> None:
        self.rule = rule

    def applies(self, value):
        if self.hasDependencies():
            dependencies = self.getDependencies()

            for alt in dependencies:
                l , valid = matchesAll(alt,value)
                if valid:
                    return l, True

            return 0,False

        else:
            return (1, value.startswith(self.getRuleChar()))

    def getRuleChar(self):
        return re.search("\"([a-zA-Z]+)\"", self.rule).group(1)

    def getDependencies(self):
        return [i.split() for i in self.rule.split("|")]

    def hasDependencies(self):
        return "\"" not in self.rule

    def length(self):
        if self.hasDependencies():
            return len(self.getDependencies()[0])
        else:
            return len(self.getRuleChar())


lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n", ""), f.readlines()))


valid = []

for l in lines:
    regex = r"^([0-9]+):(.*)$"
    m = re.match(regex,l)

    if(m):
        rules[int(m.group(1))] = Rule(m.group(2))
    elif(len(l)>0):
        length, v = rules[0].applies(l)
        if v and length == len(l):
            valid.append(l)


print(len(valid))
        


