primes = [2]
current_test = 3


print sieve_for_primes_to(104759)[10000]

while len(primes) < 10001:
	prime_divisble = False
	for x in primes:
		
		if current_test % x == 0:
			prime_divisble = True
			break

	not_prime = False
	if not prime_divisble:
		
		for x in range(2,current_test):
			if x not in primes:
				if current_test % x == 0:
					not_prime = True
					break

	print len(primes)

	if not_prime == False and prime_divisble == False:
		primes.append(current_test)
	current_test += 2
print primes

