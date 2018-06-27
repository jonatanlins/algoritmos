from functools import reduce

# mínimo múltiplo comum (least commom multiple)
def lcm(numbers):
  a = numbers[0]
  b = numbers[1] if (len(numbers) == 2) else lcm(numbers[1:])
  return [ x for x in range(max(a, b), (a*b)+1) if (x%a==0) and (x%b==0) ][0]

# calculo de múltiplos de um número
def multiples(number, limit):
  return list(range(number, limit + 1, number))

# calculo de divisores de um número
def divisors(number):
  return [ x for x in range(1, number + 1) if (number%x==0) ]

def firstIteration(lifeCycle, iterations):
  for i in iterations:
    if i % lifeCycle == 0:
      return i


populations, limit = [ int(i) for i in input().split() ]
lifeCycles = [ int(i) for i in input().split() ]

iterations = multiples(lcm(lifeCycles), limit)
possibilities = [ set(divisors(i)) for i in iterations ]
possibilities = reduce(lambda a, b: a | b, possibilities)
possibilities = [ (i, firstIteration(i, iterations)) for i in possibilities ]
resolution = max([ i for (_, i) in possibilities ])
resolution = [ a for (a, b) in possibilities if b == resolution ][0]


print(resolution)