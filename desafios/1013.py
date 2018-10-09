# O Maior
# Problema 1013 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

def main ():
  a, b, c = [ int(i) for i in input().split() ]

  print('{} eh o maior'.format(max(a, b, c)))


if __name__ == '__main__':
  main()
