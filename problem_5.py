x = 2520 # we know what the 1-10 is so we can start here
checks = [11,13,17,19,20] 
found = False
while( found == False ):
	
	if all(x % n == 0  for n in checks):
		found = True
		for y in range(2,21): # double check after the inital fall out
			if x % y != 0:
				found = False
	x += 2520 # can increase by this, as we know it has to be a multiple of this

print x


