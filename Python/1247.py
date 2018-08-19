# Guarda Costeira
# Problema 1247 do URI Judge Online
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1247

import math

while True:
	try:
		data = input()
		if data == '': break
		d, vf, vg = [ int(i) for i in data.split() ]

		tf = 12 / vf
		tg = math.sqrt(144 + (d * d)) / vg

		if tf < tg:
			print('N')
		else:
			print('S')
	except EOFError:
		break