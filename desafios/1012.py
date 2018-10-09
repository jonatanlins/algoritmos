# Área
# Problema 1012 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

def main ():
  a, b, c = [ float(i) for i in input().split() ]

  pi = 3.14159

  triangle = (a * c) / 2
  circle = pi * c * c
  trapezium = (a + b) / 2 * c
  square = b * b
  rectangle = a * b

  print('TRIANGULO: {:.3f}'.format(triangle))
  print('CIRCULO: {:.3f}'.format(circle))
  print('TRAPEZIO: {:.3f}'.format(trapezium))
  print('QUADRADO: {:.3f}'.format(square))
  print('RETANGULO: {:.3f}'.format(rectangle))


if __name__ == '__main__':
  main()
