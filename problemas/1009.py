# Salário com Bônus
# Problema 1009 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

input()
salario = float(input())
vendas = float(input())

print('TOTAL = R$ {:.2f}'.format(salario + vendas * 0.15))
