with   open("problem_8_input.dat","r") as f:
	data = f.read()
	lists = []
	list_vals = []

	for x in range(1,988):
		lists.append(data[x:x+13])
	
	for x in lists:
		if "0"  not in str(x):
			val = 1;
			for y in x:
				val *= int(y)
			list_vals.append(val)
	print max(list_vals)


