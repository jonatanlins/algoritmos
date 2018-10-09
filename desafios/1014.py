# Consumo
# Problema 1014 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

def main ():
  distance = int(input())
  fuel = float(input())

  print('{:.3f} km/l'.format(distance / fuel))


if __name__ == '__main__':
  main()
