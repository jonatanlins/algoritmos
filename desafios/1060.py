# Números Positivos
# Problema 1060 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1060

def main ():
  counter = 0

  for i in range(6):
    if float(input()) > 0:
      counter += 1

  print('{} valores positivos'.format(counter))


if __name__ == '__main__':
  main()
