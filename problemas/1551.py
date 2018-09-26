# Frase Completa
# Problema 1551 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1551

from collections import Counter

def main ():
  cases = int(input())
  for _ in range(cases):
    phrase = list(input())
    phrase = [ c for c in phrase if (c != ' ') and (c != ',') ]
    phrase = Counter(phrase)
    length = len(phrase)

    if length < 13:
      print('frase mal elaborada')
    elif length < 26:
      print('frase quase completa')
    else:
      print('frase completa')


if __name__ == '__main__':
  main()
