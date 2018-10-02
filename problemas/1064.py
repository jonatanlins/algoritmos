# Positivos e Média
# Problema 1064 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1064

def main ():
  counter = 0
  sum = 0

  for i in range(6):
    value = float(input())
    if value > 0:
      sum += value
      counter += 1

  print('{} valores positivos'.format(counter))
  print('{:.1f}'.format(sum / counter))



if __name__ == '__main__':
  main()
