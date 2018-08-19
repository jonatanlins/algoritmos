# Cálculo Simples
# Problema 1010 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

p1 = [ float(i) for i in input().split() ]
p2 = [ float(i) for i in input().split() ]

print('VALOR A PAGAR: R$ {:.2f}'.format(p1[1] * p1[2] + p2[1] * p2[2]))
