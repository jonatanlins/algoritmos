# Triângulo
# Problema 1043 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

def isATriangle (a, b, c):
  return (a + b > c) and (b + c > a) and (a + c > b)

def main ():
  a, b, c = [ float(i) for i in input().split() ]

  if isATriangle(a, b, c):
    print('Perimetro = {:.1f}'.format(a + b + c))
  else:
    print('Area = {:.1f}'.format((a + b) / 2 * c))


if __name__ == '__main__':
  main()
