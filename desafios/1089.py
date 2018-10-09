# Loop Musical
# Problema 1089 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1089

while True:
  # loop que só para quando recebe zero na entrada
  number = int(input())
  if number == 0: break

  # entrada de dados
  values = [ int(i) for i in input().split() ]

  # cria um início de loop no fim da lista
  values.append(values[0])
  values.append(values[1])

  # loop que conta quantos picos existem na sequência
  result = 0
  for i in range(1, number + 1):
    curr = values[i]
    next = values[i + 1]
    prev = values[i - 1]
    # verifica se é um pico
    if (prev > curr and next > curr) or (prev < curr and next < curr):
      result += 1

  # resposta
  print(result)