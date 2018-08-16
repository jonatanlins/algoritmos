from collections import Counter

# leitura de dados
players = int(input())
minimum = int(input())
points = []
for i in range(players):
  points.append(int(input()))

points = dict(Counter(points))
finalists = 0
while minimum > finalists:
  finalists += points.pop(max(points.keys()))

print(finalists)