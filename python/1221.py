# Primo Rápido
# Problema 1221 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1221

from math import sqrt, ceil

def is_prime(n):
  for i in range(2, ceil(sqrt(n))):
    if n % i == 0:
      return False
  return True

def main ():
  cases = int(input())
  for i in range(cases):
    number = int(input())

    print('Prime' if is_prime(number) else 'Not Prime')

if __name__ == '__main__':
  main()