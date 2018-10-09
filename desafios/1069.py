# Diamantes e Areia
# Problema 1069 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1069

cases = int(input())

for i in range(cases):
  string = input().replace('.', '')

  result = 0

  while string.find('<>') != -1:
    string = string.replace('<>', '', 1)
    result += 1

  print(result)
