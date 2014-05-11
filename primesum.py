n = 500

for flower in range(1, 1001):
	tests = range(2, flower - 1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False 
	
	if prime == True:
		print str(n) + " is prime!"
		
	if prime == False:
		print str(n) + " is not prime!"