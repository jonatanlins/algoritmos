# Intervalo
# Problema 1037 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

def main ():
  value = float(input())

  # [0,25], (25,50], (50,75], (75,100]
  if value >= 0 and value <= 25:
    print('Intervalo [0,25]')
  elif value > 25 and value <= 50:
    print('Intervalo (25,50]')
  elif value > 50 and value <= 75:
    print('Intervalo (50,75]')
  elif value > 75 and value <= 100:
    print('Intervalo (75,100]')
  else:
    print('Fora de intervalo')


if __name__ == '__main__':
  main()
