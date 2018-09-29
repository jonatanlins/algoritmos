# Média 3
# Problema 1040 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

def main ():
  notas = [ float(i) for i in input().split() ]

  media = (notas[0]*2 + notas[1]*3 + notas[2]*4 + notas[3]*1) / 10

  print('Media: {:.1f}'.format(media))

  if media >= 7:
    print('Aluno aprovado.')
  elif media < 5:
    print('Aluno reprovado.')
  else:
    print('Aluno em exame.')

    notaExame = float(input())

    print('Nota do exame: {:.1f}'.format(notaExame))

    media = (media + notaExame) / 2

    if media >= 5:
      print('Aluno aprovado.')
    else:
      print('Aluno reprovado.')

    print('Media final: {:.1f}'.format(media))
    

if __name__ == '__main__':
  main()
