# Sequencia IJ 4
# Problema 1098 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1098

def main ():
  for i in range(0, 11):
    i /= 5
    if i == int(i):
      i = int(i)

    for j in range(1, 4):
      j += i
      if j == int(j):
        j = int(j)
        
      print('I={} J={}'.format(i, j))


if __name__ == '__main__':
  main()
