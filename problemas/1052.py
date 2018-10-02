# Mês
# Problema 1052 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1052

def main ():
  months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
  }

  number = int(input())

  print(months[number])


if __name__ == '__main__':
  main()
