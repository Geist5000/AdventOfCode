from types import LambdaType, MappingProxyType


def loadData(fileName: str, mapFunc: LambdaType = lambda x: x):

    with open(fileName) as f:
        return list(map(lambda l: mapFunc(l.replace("\n", "")), f.readlines()))


def main(fileName: str):
    lines = loadData(fileName)
    # if one is present more than this count it is most common
    width = len(lines[0])
    common_bits = []
    minor_bits = []
    common_match = ""
    minor_match = ""
    # loop characters
    for i in range(width+1):
        common_ones = 0
        minor_ones = 0
        common_match_count = 0
        minor_match_count = 0

        # loop words
        for l in lines:
            # check if line
            if starts_with(l, common_bits):
                common_match_count += 1
                common_match = l
                # check if i is in bounds to catch errors wich happens if the last iteration is reached
                if i<width and l[i] == "1":
                    common_ones += 1
            if starts_with(l, minor_bits):
                minor_match_count += 1
                minor_match = l
                # check if i is in bounds to catch errors wich happens if the last iteration is reached
                if i<width and l[i] == "1":
                    minor_ones += 1
        if minor_ones >= minor_match_count - minor_ones:
            minor_bits.append(0)
        else:
            minor_bits.append(1)

        if common_ones >= common_match_count - common_ones:
            common_bits.append(1)
        else:
            common_bits.append(0)

        # early break because both numbers are found
        if common_match_count <= 1 and minor_match_count <= 1:
            break
    return int(minor_match,2) * int(common_match,2)

def starts_with(bits: str, needle: list[int]):
    """checks if the given string starts with the same number aragement as the given needle"""
    return bits.startswith("".join(map(str,needle)))


def flip_ints(ints: list[int]):
    """returns new list which has a 0 if at the same index the original list had a one"""
    return [0 if i == 1 else 1 for i in ints]


if __name__ == "__main__":
    expectedTestOutput = 230

    testResult = main("testInput.txt")
    print(f"Test result: {testResult}")
    if testResult == expectedTestOutput:
        print("Test result is same as expected output. \nAttemping to solve real dataset:")
        realResult = main("data.txt")
        print(f"Real result is {realResult}")
