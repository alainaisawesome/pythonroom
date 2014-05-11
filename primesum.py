total = 0

for n in range(1, 1001):
	tests = range(2, n - 1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False 
	
	if prime == True:
		print str(n) + " is prime!"
		
