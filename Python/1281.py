# Ida à Feira
# Problema 1281 do URI Judge Online
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1281

inputs = int(input())
for i in range(inputs):
  products = [ input().split() for i in range(int(input())) ]
  shoppingList = [ input().split() for i in range(int(input())) ]

  prices = {}
  for [name, price] in products:
    prices[name] = float(price)
  
  spendings = {}
  for [name, quantity] in shoppingList:
    spendings[name] = prices[name] * int(quantity)
  
  spendings = [ spendings[i] for i in spendings ]

  print('R$ {:.2f}'.format(sum(spendings)))
