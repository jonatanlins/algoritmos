# DDD
# Problema 1050 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1050

def main ():
  tabela = {
    '61': 'Brasilia',
    '71': 'Salvador',
    '11': 'Sao Paulo',
    '21': 'Rio de Janeiro',
    '32': 'Juiz de Fora',
    '19': 'Campinas',
    '27': 'Vitoria',
    '31': 'Belo Horizonte',
  }

  ddd = input()

  try:
    print(tabela[ddd])
  except KeyError:
    print('DDD nao cadastrado')


if __name__ == '__main__':
  main()
