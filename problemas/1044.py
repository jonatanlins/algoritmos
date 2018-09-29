# Múltiplos
# Problema 1044 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

def main ():
  a, b = [ int(i) for i in input().split() ]

  if (a % b == 0) or (b % a == 0):
    print('Sao Multiplos')
  else:
    print('Nao sao Multiplos')


if __name__ == '__main__':
  main()
