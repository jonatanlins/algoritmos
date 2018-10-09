# Sequencia IJ 3
# Problema 1097 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1097

def main ():
  for i in range(1, 10, 2):
    for j in range(i + 6, i + 3, -1):
      print('I={} J={}'.format(i, j))


if __name__ == '__main__':
  main()
