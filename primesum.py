n = 500

flowers = range(1, 1001)
for flower in flowers:
	tests = range(2, flower - 1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False 
	
	if prime == True:
		print str(n) + " is prime!"
		
	if prime == False:
		print str(n) + " is not prime!"