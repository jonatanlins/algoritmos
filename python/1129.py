# Leitura Ótica
# Problema 1129 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1129

while True:
	n = int(input())
	if n == 0: break

	for q in range(n):
		questions = [ int(i) for i in input().split() ]

		questions = [ 1 if (i <= 127) else 0 for i in questions ]

		if sum(questions) != 1:
			print('*')
		else:
			print(chr(65 + questions.index(1)))
