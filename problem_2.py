x = 0
y = 1
temp = x
sum_val =0
while(x <= 4000001):
	print x,y, x + y, (x + y)% 2
	if (x + y ) % 2 == 0:
		sum_val += x + y
	temp = x + y
	y = x
	x = temp
print sum_val