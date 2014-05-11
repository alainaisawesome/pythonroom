n = 504 
tests = range(2, 503)
for t in tests:
	if n % t == 0:
		print ("This number is not prime")
	else:
		print ("this number is prime!")