# Validação de Nota
# Problema 1117 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1117

def main ():
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


if __name__ == '__main__':
  main()
