from types import LambdaType


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    sum_values = 0
    for index, l in enumerate(lines):
        blueprint, value = l.split(" | ")
        blueprints = blueprint.split(" ")
        values = value.split(" ")
        n_sets = {}
        s_numbers = {}
        for b in filter(lambda x: len(x) in [2, 3, 4, 7], blueprints):
            len_b = len(b)
            set_b = frozenset(b)
            if len_b == 2:
                n_sets[1] = set_b
                s_numbers[set_b] = 1
            if len_b == 3:
                n_sets[7] = set_b
                s_numbers[set_b] = 7
            if len_b == 4:
                n_sets[4] = set_b
                s_numbers[set_b] = 4
            if len_b == 7:
                n_sets[8] = set_b
                s_numbers[set_b] = 8
        for b in filter(lambda x: len(x) in [6,5], blueprints):
            l = len(b)
            s = frozenset(b)
            if l == 6:
                if n_sets[1] <= s:
                    if n_sets[4] <= s:
                        n_sets[9]=s
                        s_numbers[s] = 9
                    else:
                        n_sets[0]=s
                        s_numbers[s] = 0
                else:
                    n_sets[6]=s
                    s_numbers[s] = 6
            if l== 5:
                broken_four = n_sets[4] - n_sets[1]
                if n_sets[1] <= s:
                    n_sets[3] = s
                    s_numbers[s] = 3
                elif broken_four <= s:
                    n_sets[5] = s
                    s_numbers[s] = 5
                else:
                    n_sets[2] = s
                    s_numbers[s] = 2
            
        v = 0
        for i in map(lambda x: s_numbers[frozenset(x)],values):
            v *= 10
            v+=i 
        sum_values += v

    return sum_values
if __name__ == "__main__":
    expectedTestOutput = 61229

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
