sum = 1000
a = 1
for a in range(1, sum /3):
	b = a +1
	for b  in range(1,sum/2):
		c = sum - a - b
		if (a * a + b * b == c * c):
			print a,b,c
			print a * b * c