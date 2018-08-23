# Criptografia
# Problema 1024 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1024

import re
import math

cases = int(input())

for i in range(cases):
  text = list(input())

  middle = math.ceil(len(text) / 2)

  for i, v in enumerate(text):
    text[i] = ord(v)
    if re.match(r'[a-zA-Z]', v):
      text[i] += 3
    if i < middle:
      text[i] -= 1
    text[i] = chr(text[i])

  text.reverse()

  print(''.join(text))
