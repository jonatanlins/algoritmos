# Cédulas
# Problema 1018 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

def main ():
  value = int(input())

  print(value)

  print('{} nota(s) de R$ 100,00'.format(value // 100))
  value %= 100

  print('{} nota(s) de R$ 50,00'.format(value // 50))
  value %= 50

  print('{} nota(s) de R$ 20,00'.format(value // 20))
  value %= 20

  print('{} nota(s) de R$ 10,00'.format(value // 10))
  value %= 10

  print('{} nota(s) de R$ 5,00'.format(value // 5))
  value %= 5

  print('{} nota(s) de R$ 2,00'.format(value // 2))
  value %= 2

  print('{} nota(s) de R$ 1,00'.format(value // 1))
  value %= 1


if __name__ == '__main__':
  main()
