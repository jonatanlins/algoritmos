# Desvendando Monty Hall
# Problema 2879 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2879

def main ():
  cases = int(input())
  counter = 0

  for _ in range(cases):
    door = int(input())

    if door != 1:
      counter += 1

  print(counter)


if __name__ == '__main__':
  main()
