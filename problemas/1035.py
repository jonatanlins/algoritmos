# Teste de Seleção 1
# Problema 1035 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

def main ():
  a, b, c, d = [ int(i) for i in input().split() ]

  # se B for maior do que C
  # e se D for maior do que A
  # e a soma de C com D for maior que a soma de A e B
  # e se C e D, ambos, forem positivos
  # e se a variável A for par
  if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
  else:
    print('Valores nao aceitos')


if __name__ == '__main__':
  main()
