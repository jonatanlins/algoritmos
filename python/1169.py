# Trigo no Tabuleiro
# Problema 1169 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1169

def main ():
  cases = int(input())

  for _ in range(cases):
    n = int(input())

    result = (2 ** (n)) // 12000

    print('{} kg'.format(result))

if __name__ == '__main__':
  main()