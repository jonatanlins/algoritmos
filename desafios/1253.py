# Cifra de César
# Problema 1253 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1253

inputs = int(input())

for i in range(inputs):
  text = list(input())
  shift = int(input())

  text = [ ord(c) - shift for c in text ]
  text = [ chr(c) if c >= 65 else chr(c + 26) for c in text ]
  text = ''.join(text)

  print(text)
