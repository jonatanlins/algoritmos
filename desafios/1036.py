# Fórmula de Bhaskara
# Problema 1036 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

from math import sqrt

def main ():
  a, b, c = [ float(i) for i in input().split() ]

  delta = (b ** 2) - (4 * a * c)

  if delta < 0 or a == 0:
    print('Impossivel calcular')
    return

  r1 = (-b + sqrt(delta)) / (2 * a)
  r2 = (-b - sqrt(delta)) / (2 * a)

  print('R1 = {:.5f}'.format(r1))
  print('R2 = {:.5f}'.format(r2))


if __name__ == '__main__':
  main()
