# Divisão da Nlogônia
# Problema 1091 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1091

def main ():
  while (True):
    cases = int(input())
    if cases == 0: break

    centerX, centerY = [ int(i) for i in input().split() ]
    for i in range(cases):
      houseX, houseY = [ int(i) for i in input().split() ]
      houseX -= centerX
      houseY -= centerY

      if houseX == 0 or houseY == 0:
        print('divisa')
      elif houseX > 0 and houseY > 0:
        print('NE')
      elif houseX > 0 and houseY < 0:
        print('SE')
      elif houseX < 0 and houseY > 0:
        print('NO')
      elif houseX < 0 and houseY < 0:
        print('SO')




if __name__ == '__main__':
  main()
