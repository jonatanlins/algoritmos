# Animal
# Problema 1049 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

def main ():
  if (input() == 'vertebrado'):
    if (input() == 'ave'):
      if (input() == 'carnivoro'):
        print('aguia')
      else:
        print('pomba')
    else:
      if (input() == 'onivoro'):
        print('homem')
      else:
        print('vaca')
  else:
    if (input() == 'inseto'):
      if (input() == 'hematofago'):
        print('pulga')
      else:
        print('lagarta')
    else:
      if (input() == 'hematofago'):
        print('sanguessuga')
      else:
        print('minhoca')


if __name__ == '__main__':
  main()
