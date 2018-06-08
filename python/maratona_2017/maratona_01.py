import statistics

numberOfKeys, numberOfChords = [ int(i) for i in input().split() ]

keys = [1] * numberOfKeys

for chord in range(numberOfChords):
  a, b = [ int(i) for i in input().split() ]
  f = statistics.mode(keys[a : b+1])
  # BUG: função statistics.mode dá erro quando não existe única moda
  for i in range(a, b+1):
    keys[i] = (keys[i] + f) % 9

for key in keys:
  print(key)