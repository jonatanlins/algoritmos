# PUM
# Problema 1142 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1142

def main ():
  n = int(input()) * 4

  for i in range(1, n + 1):
    if i % 4 == 0:
      print('PUM')
    else:
      print('{} '.format(i), end = '')


if __name__ == '__main__':
  main()
