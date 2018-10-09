# Distância Entre Dois Pontos
# Problema 1015 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

from math import sqrt

def main ():
  x1, y1 = [ float(i) for i in input().split() ]
  x2, y2 = [ float(i) for i in input().split() ]

  distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

  print('{:.4f}'.format(distance))


if __name__ == '__main__':
  main()
