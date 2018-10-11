# Carrega ou não Carrega?
# Problema 1026 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1026

def main ():
  while (True):
    try:
      a, b = [ int(i) for i in input().split() ]

      print(a ^ b)

    except EOFError:
      break



if __name__ == '__main__':
  main()
