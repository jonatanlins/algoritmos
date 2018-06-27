import math

inputNumber = int(input())

factorials = [1]
while factorials[-1] <= inputNumber:
  factorials.append(math.factorial(len(factorials)))
factorials.pop()

operationCounter = 0
while inputNumber != 0:
  if factorials[-1] > inputNumber:
    factorials.pop()
  else:
    inputNumber -= factorials[-1]
    operationCounter += 1

print(operationCounter)