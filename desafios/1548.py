# Fila do Recreio
# Problema 1548 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1548

cases = int(input())

for c in range(cases):
	n = int(input())
	students = [ int(i) for i in input().split() ]

	newOrder = sorted(students)
	newOrder.reverse()

	result = 0
	for i in range(len(newOrder)):
		if newOrder[i] == students[i]:
			result += 1

	print(result)