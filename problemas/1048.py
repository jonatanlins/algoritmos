# Aumento de Salário
# Problema 1048 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

def obterReajuste (salario):
  if salario <= 400:
    return 0.15
  elif 400 < salario <= 800:
    return 0.12
  elif 800 < salario <= 1200:
    return 0.10
  elif 1200 < salario <= 2000:
    return 0.07
  else:
    return 0.04


def main ():
  salario = float(input())
  reajuste = obterReajuste(salario)

  print('Novo salario: {:.2f}'.format(salario * (reajuste + 1)))
  print('Reajuste ganho: {:.2f}'.format(salario * reajuste))
  print('Em percentual: {} %'.format(int(reajuste * 100)))



if __name__ == '__main__':
  main()
