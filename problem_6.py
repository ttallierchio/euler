val_sum_squared = sum(map(lambda x: x**2,range(1,101)))
val_sum =sum(range(1,101))
t = 0
for x in range(1,101):
	t = t + x **2
print t, val_sum_squared,val_sum **2
print (val_sum **2) - val_sum_squared 