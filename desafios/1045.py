# Tipos de Triângulos
# Problema 1045 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

def main ():
  values = [ float(i) for i in input().split() ]
  a, b, c = sorted(values, reverse = True)

  if a >= b + c:
    print('NAO FORMA TRIANGULO')
  else:
    if a**2 == b**2 + c**2:
      print('TRIANGULO RETANGULO')
      
    if a**2 > b**2 + c**2:
      print('TRIANGULO OBTUSANGULO')
      
    if a**2 < b**2 + c**2:
      print('TRIANGULO ACUTANGULO')
      
    if a == b == c:
      print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
      print('TRIANGULO ISOSCELES')

if __name__ == '__main__':
  main()
