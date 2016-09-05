large_val = 0
for x in range(100,1000):
	for y in range(x,1000):
		
		if str(x * y)[::-1] ==  str(x * y):
			if large_val <= x * y:
				large_val = x * y
print large_val