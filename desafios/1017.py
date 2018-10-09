# Gasto de Combustível
# Problema 1017 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

def main ():
  time = int(input())
  velocity = int(input())

  consumption = (velocity * time) / 12

  print('{:.3f}'.format(consumption))


if __name__ == '__main__':
  main()
