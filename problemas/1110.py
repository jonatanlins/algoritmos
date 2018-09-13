# Jogando Cartas Fora
# Problema 1110 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1110

while True:
  stack = list(range(1, 1 + int(input())))
  if len(stack) == 0: break

  discard = []

  while len(stack) > 1:
    discard.append(stack.pop(0))
    stack.append(stack.pop(0))

  discard = ', '.join([ str(i) for i in discard ])
  
  print('Discarded cards: {}'.format(discard))
  print('Remaining card: {}'.format(stack[0]))