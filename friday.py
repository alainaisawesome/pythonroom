# author: alainaisawesome

print "welcome to fan world, today you will pick a fan!"
input("what fan do you want to buy?")
print "ok, here we go, you have three choices!"
fans = [ " circle fan "," square fan "," diamond fan " ]
for fan in fans:
	answer = input("Do you want to buy" + fan + "?")
	if answer == "yes":
		print " then order" + fan + "good choice!"
	if answer == "no":
		print "Then don't order it!"
		


	