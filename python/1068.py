# Balanço de Parênteses I
# Problema 1068 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1068

# loop que para ao detectar fim de arquivo (EOF)
while True:
  try:

    # entrada de dados
    expression = list(input())

    parentheses = 0

    for c in expression:
      if parentheses < 0:
        break
      elif c == '(':
        parentheses += 1
      elif c == ')':
        parentheses -= 1

    print('correct' if parentheses == 0 else 'incorrect')

  except EOFError:
    break