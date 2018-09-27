# Volume da TV
# Problema 2444 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2444

def main ():
  volume, _ = [ int(i) for i in input().split() ]
  changes = [ int(i) for i in input().split() ]

  for change in changes:
    volume += change
    if volume < 0:
      volume = 0
    if volume > 100:
      volume = 100

  print(volume)


if __name__ == '__main__':
  main()
