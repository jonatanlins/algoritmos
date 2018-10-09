# Tempo de Jogo com Minutos
# Problema 1047 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1047

def main ():
  horarios = [ int(i) for i in input().split() ]

  momentoInicial = horarios[0] * 60 + horarios[1]
  momentoFinal = horarios[2] * 60 + horarios[3]

  if momentoInicial >= momentoFinal:
    momentoFinal += (24 * 60)

  horas = (momentoFinal - momentoInicial) // 60
  minutos = (momentoFinal - momentoInicial) % 60

  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))



if __name__ == '__main__':
  main()
