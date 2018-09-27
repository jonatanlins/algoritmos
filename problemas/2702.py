# Escolha Difícil
# Problema 2702 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2702

def main ():
  alimentos = [ int(i) for i in input().split() ]
  passageiros = [ int(i) for i in input().split() ]

  faltas = 0
  for i in range(3):
    if passageiros[i] > alimentos[i]:
      faltas += (passageiros[i] - alimentos[i])

  print(faltas) 


if __name__ == '__main__':
  main()
