import re

def calculateNumbers(firstNumber,secondNumber,operation):
    if("*" in operation):
        return firstNumber * secondNumber
    elif("+" in operation):
        return firstNumber + secondNumber
def placeParentheses(expression):
    return expression
def computeResult(expression):
    # going for a performant iterative solution rather than the easy recursive one
    expression = expression.replace(" ","")
    prevNumberStack=[None] # each number of each calculation group
    operationStack = [] 
    currentLoc = 0

    while(currentLoc < len(expression)):
        if(expression[currentLoc] == "+"):
            prevNumberStack.insert(-2,None)
        if(expression[currentLoc] == "("):
            prevNumberStack.append(None)
            currentLoc += 1
        else:
            numberMatch = re.compile(r"([0-9]+)").match(expression,currentLoc)
            if(numberMatch):
                currentLoc += len(numberMatch.group(0))
                number = int(numberMatch.group(1))
                prevNumberStack.append(number)
            else:
                operation = expression[currentLoc]
                currentLoc += 1
                if(prevNumberStack[-2]):
                    op = operationStack.pop()
                    
                    result = calculateNumbers(prevNumberStack.pop(),prevNumberStack.pop(),op)
                    if(op == "+"):
                        prevNumberStack.pop()
                    prevNumberStack.append(result)
                if(operation == ")"):
                    prevNumberStack.pop(-2)
                else:
                    operationStack.append(operation)
    return calculateNumbers(prevNumberStack.pop(),prevNumberStack.pop(),operationStack.pop())
                





    



lines = []


with open("data.txt") as f:
    lines = list(map(lambda l: l.replace("\n",""),f.readlines()))

print(sum(map(computeResult,lines)))
