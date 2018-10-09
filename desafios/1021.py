# Notas e Moedas
# Problema 1021 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

def main ():
  value = float(input())

  notas = int(value)
  print('NOTAS:')

  print('{} nota(s) de R$ 100.00'.format(notas // 100))
  notas %= 100
  print('{} nota(s) de R$ 50.00'.format(notas // 50))
  notas %= 50
  print('{} nota(s) de R$ 20.00'.format(notas // 20))
  notas %= 20
  print('{} nota(s) de R$ 10.00'.format(notas // 10))
  notas %= 10
  print('{} nota(s) de R$ 5.00'.format(notas // 5))
  notas %= 5
  print('{} nota(s) de R$ 2.00'.format(notas // 2))
  notas %= 2


  moedas = int((value * 100) % 100) + (notas * 100)
  print('MOEDAS:')

  print('{} moeda(s) de R$ 1.00'.format(moedas // 100))
  moedas %= 100
  print('{} moeda(s) de R$ 0.50'.format(moedas // 50))
  moedas %= 50
  print('{} moeda(s) de R$ 0.25'.format(moedas // 25))
  moedas %= 25
  print('{} moeda(s) de R$ 0.10'.format(moedas // 10))
  moedas %= 10
  print('{} moeda(s) de R$ 0.05'.format(moedas // 5))
  moedas %= 5
  print('{} moeda(s) de R$ 0.01'.format(moedas // 1))
  moedas %= 1



if __name__ == '__main__':
  main()
