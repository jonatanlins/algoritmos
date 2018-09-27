# Esfera
# Problema 1011 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1011

def main ():
  r = int(input())
  pi = 3.14159
  volume = (4/3) * pi * (r ** 3)

  print('VOLUME = {:.3f}'.format(volume))

if __name__ == '__main__':
  main()
