# Imposto de Renda
# Problema 1051 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1051

value = float(input())

if value <= 2000:
  print('Isento')
elif value <= 3000:
  print('R$ {:.2f}'.format((value - 2000) * 0.08))
elif value <= 4500:
  print('R$ {:.2f}'.format((value - 3000) * 0.18 + 1000 * 0.08))
else:
  print('R$ {:.2f}'.format((value - 4500) * 0.28 + 1000 * 0.08 + 1500 * 0.18))
