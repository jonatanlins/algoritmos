# Array Hash
# Problema 1257 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1257

cases = int(input())

for i in range(cases):
  lines = [ list(input()) for l in range(int(input())) ]

  lines = [ [ ord(c) - 65 for c in l ] for l in lines ]
  lines = [
    sum(l) + sum(range(len(l))) + (len(l) * i) for i, l in enumerate(lines)
  ]

  print(sum(lines))