players, rounds = [ int(i) for i in input().split() ]
points = [ int(i) for i in input().split() ]

result = [0] * players

for _ in range(rounds):
  for player in range(players):
    result[player] += points.pop(0)

winner = 0
for player in range(players):
  if result[player] >= result[winner]:
    winner = player
winner += 1


print(winner)