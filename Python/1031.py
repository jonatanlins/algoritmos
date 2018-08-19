# Crise de Energia
# Problema 1031 do URI Judge Online
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1031

while True:
	n = int(input())
	if n == 0:
		break

	m = 1

	while True:
		ultimo = 0
		regioes = list(range(2, n + 1))
		while len(regioes) > 1:
			ultimo = (m + ultimo - 1) % len(regioes)
			regioes.pop(ultimo)

		if regioes == [13]:
			print(m)
			break
		m += 1
