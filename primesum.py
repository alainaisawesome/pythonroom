n = 504 
tests = range(1, 503)
prime = True
for t in tests:
	if n % t == 0:
		prime = False 

if prime == True:
	print str(n) + " is prime!"
	
if prime == False:
	print str(n) + " is not prime!"