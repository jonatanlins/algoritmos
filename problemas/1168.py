# LED
# Problema 1168 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1168

cases = int(input())
leds = {
  '0': 6,
  '1': 2,
  '2': 5,
  '3': 5,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 3,
  '8': 7,
  '9': 6
}

for i in range(cases):
  number = list(input())
  
  result = 0
  for n in number:
    result += leds[n]

  print('{} leds'.format(result))
