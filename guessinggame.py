import random

# author: alainaisawesome
min_num = int(input("What is the minimum?"))
max_num = int(input("What is the maximum?"))
print "think of a number between " + str(min_num) + " and " + str(max_num)
chances = int(input("How many chances do I get?"))  


for i in range(chances):
	answer = (min_num + max_num)/2
	
	print "My guess is " + str(answer)
	
	x = input ("is my answer correct, too low, or too high?")
	
	if x == "high":
		max_num = answer
	elif x == "low":
		
		min_num = answer
	elif x == "correct":
		print "I win"
		break
	else:
		print "I don't recognize that number"
	
