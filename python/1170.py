# Blobs
# Problema 1170 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1170

def main ():
  cases = int(input())

  for _ in range(cases):
    n = float(input())
    result = 0

    while n > 1:
      n /= 2
      result += 1

    print('{} dias'.format(result))

if __name__ == '__main__':
  main()