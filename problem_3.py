prime_factors = []
x = 600851475143
factor = 2

if x % 2 == 0:
	x = x/2
	prime_factors.append(2)

factor = 3
while (x != 1):
	print x, factor, x % factor
	if x % factor ==0:
		x = x / factor
		prime_factors.append(factor)
	factor += 2
print prime_factors
	
