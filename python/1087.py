# Dama
# Problema 1087 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1087

def main ():
  while True:
    x1, y1, x2, y2 = [ int(i) for i in  input().split() ]
    if not x1: break

    if x1 == x2 and y1 == y2:
      print(0)
    elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2 or x1 == x2 or y1 == y2:
      print(1)
    else:
      print(2)


if __name__ == '__main__':
  main()
