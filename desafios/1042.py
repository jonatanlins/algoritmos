# Sort Simples
# Problema 1042 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

def main ():
  values = [ int(i) for i in input().split() ]

  for i in sorted(values):
    print(i)

  print()

  for i in values:
    print(i)


if __name__ == '__main__':
  main()
