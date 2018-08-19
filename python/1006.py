# Média 2
# Problema 1006 do URI Online Judge
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

a, b, c = [ float(input()) for i in range(3) ]

media = (a * 2 + b * 3 + c * 5) / 10

print('MEDIA = {:.1f}'.format(media))
