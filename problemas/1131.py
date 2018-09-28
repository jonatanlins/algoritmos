# Grenais
# Problema 1131 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1131

from collections import Counter

def grenal ():
  resultado = [ int(i) for i in input().split() ]
  if resultado[0] > resultado[1]:
    return 'inter'
  elif resultado[1] > resultado[0]:
    return 'gremio'
  else:
    return 'empate'


def querContinuar ():
  while True:
    print('Novo grenal (1-sim 2-nao)')
    opcao = input()

    if opcao == '1':
      return True
    elif opcao == '2':
      return False



def main ():
  grenais = []

  while True:
    grenais.append(grenal())

    if not querContinuar():
      print('{} grenais'.format(len(grenais)))
      
      grenais = Counter(grenais)

      print('Inter:{}'.format(grenais['inter']))
      print('Gremio:{}'.format(grenais['gremio']))
      print('Empates:{}'.format(grenais['empate']))

      if grenais['inter'] > grenais['gremio']:
        print('Inter venceu mais')
      elif grenais['gremio'] > grenais['inter']:
        print('Gremio venceu mais')
      else:
        print('Nao houve vencedor')

      break



if __name__ == '__main__':
  main()
