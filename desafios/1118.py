# Várias Notas Com Validação
# Problema 1118 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1118

def obterMedia ():
  notas = []

  while True:
    nota = float(input())

    if nota > 10 or nota < 0:
      print('nota invalida')
    else:
      notas.append(nota)

    if len(notas) >= 2:
      print('media = {:.2f}'.format(sum(notas) / 2))
      break


def querContinuar ():
  while True:
    print('novo calculo (1-sim 2-nao)')
    opcao = input()

    if opcao == '1':
      return True
    elif opcao == '2':
      return False



def main ():
  while True:
    obterMedia()

    if not querContinuar():
      break



if __name__ == '__main__':
  main()





