# Coordenadas de um Ponto
# Problema 1041 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

def main ():
  x, y = [ float(i) for i in input().split() ]

  if x == 0 and y == 0:
    print('Origem')
  elif x == 0:
    print('Eixo Y')
  elif y == 0:
    print('Eixo X')
  elif x > 0 and y > 0:
    print('Q1')
  elif x < 0 and y > 0:
    print('Q2')
  elif x < 0 and y < 0:
    print('Q3')
  elif x > 0 and y < 0:
    print('Q4')


if __name__ == '__main__':
  main()
