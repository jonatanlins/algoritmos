# Lanche
# Problema 1038 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

def main ():
  code, quantity = [ int(i) for i in input().split() ]

  prices = {
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5
  }

  print('Total: R$ {:.2f}'.format(prices[code] * quantity))


if __name__ == '__main__':
  main()
