a1, a2, a3 = [ int(input()) for i in range(3) ]

time = [ 2*a1+a2, a1+a3, a2+2*a3 ]

print(min(time) * 2)