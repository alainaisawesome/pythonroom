#average distance between prime numbers
#largest distance between prime numbers 
#smallest distance between prime numbers
#how many twin primes

total = 0
lastPrime = 2
for n in range(2, 1001):
	tests = range(2, n - 1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False 
	
	if prime == True:
		total = total + ( n - lastPrime )
		print lastPrime
		
print total
		
