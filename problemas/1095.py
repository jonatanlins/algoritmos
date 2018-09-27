# Sequencia IJ 1
# Problema 1095 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1095

def main ():
  for i in range(13):
    print('I={} J={}'.format((i * 3 + 1), (60 - i * 5)))


if __name__ == '__main__':
  main()
