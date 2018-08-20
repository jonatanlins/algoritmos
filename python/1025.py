# Onde está o Mármore?
# Problema 1025 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1025


# algoritmo de busca binária
def binarySearch (array, value):
  left = 0
  right = len(array)
  while True:
    middle = (left + right) // 2
    curr = array[middle]
    if curr == value:
      while array[middle - 1] == value:
        middle -= 1
      return middle
    elif left == middle:
      return -1
    elif curr > value:
      right = middle
    else:
      left = middle


case = 0
while True:
  # incrementa o contador de casos
  case += 1

  # entrada de dados
  n, q = [ int(i) for i in input().split() ]
  marbles = [ int(input()) for i in range(n) ]
  checks = [ int(input()) for i in range(q) ]
  
  # condição para parar o loop
  if n == 0 and q == 0: break

  # ordena os mármores
  marbles.sort()

  # início da saída de dados
  print('CASE# {}:'.format(case))

  # exibe a posição de cada mármore
  for c in checks:
    position = binarySearch(marbles, c)
    if position != -1:
      print('{} found at {}'.format(c, position + 1))
    else:
      print('{} not found'.format(c))
