# Idade em Dias
# Problema 1020 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

def main ():
  days = int(input())

  years = days // 365
  days -= years * 365

  months = days // 30
  days -= months * 30

  print('{} ano(s)'.format(years))
  print('{} mes(es)'.format(months))
  print('{} dia(s)'.format(days))


if __name__ == '__main__':
  main()
