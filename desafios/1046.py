# Tempo de Jogo
# Problema 1046 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

def main ():
  inicio, fim = [ int(i) for i in input().split() ]

  if fim > inicio:
    print('O JOGO DUROU {} HORA(S)'.format(fim - inicio))
  else:
    print('O JOGO DUROU {} HORA(S)'.format(24 - inicio + fim))


if __name__ == '__main__':
  main()
