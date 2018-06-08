import math

capacity = int(input())
students = int(input())

result = math.ceil(students / (capacity - 1))

print(result)