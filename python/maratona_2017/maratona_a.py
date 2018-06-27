import collections

numberOfKeys, numberOfChords = [ int(i) for i in input().split() ]

keys = [1] * numberOfKeys

for chord in range(numberOfChords):
  keyA, keyB = [ int(i) for i in input().split() ]
  counts = collections.Counter(keys[keyA : keyB+1])
  maxValue = max(counts.values())
  mostCommonNotes = []
  for key,value in dict(counts).items():
    if value == maxValue:
      mostCommonNotes.append(key)
  mostCommonNote = max(mostCommonNotes)
  # f = statistics.mode(keys[keyA : keyB+1])
  for i in range(keyA, keyB+1):
    keys[i] = (keys[i] + mostCommonNote) % 9

for key in keys:
  print(key)