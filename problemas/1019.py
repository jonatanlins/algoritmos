# Conversão de Tempo
# Problema 1019 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

def main ():
  seconds = int(input())

  hours = seconds // 60 // 60
  minutes = seconds // 60 % 60
  seconds = seconds % 60 % 60

  print('{}:{}:{}'.format(hours, minutes, seconds))


if __name__ == '__main__':
  main()
