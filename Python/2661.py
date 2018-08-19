# Despojados
# Problema 2661 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2661

## resolução detalhada em: https://goo.gl/guaacw

from math import sqrt

x = int(input()) # leitura do número
count = 0 # contador de fatores primos
k = 2 # candidato a primo
root = sqrt(x) # raiz da entrada

# enquanto o número não tiver sido fatorado por completo, ou o
# candidato a primo for menor ou igual a raiz de x, continue fatorando
while x > 1 and k <= root:
  if x % k == 0:
    # Se x é divisível pelo primo k, incremente o contador
    count += 1
    while x % k == 0:
      # divida x pelo primo até não conseguir mais
      x //= k
  # passe para o próximo candidato a primo
  k += 1

# Se a fatoração terminou com x > 1, significa que k > raiz e portanto,
# o que sobrou em x é primo
if x > 1:
  count += 1

print((2 ** count) - count - 1)