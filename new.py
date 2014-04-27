# author: alainaisawesome
total = 0 
month = 1
days = 1
year = 1900

while year < 2015:
	total = total + 1
	if month == 12 and date == 31:
		year = year + 1
		month = 1
		day = 1
	else:
		month = month + 1
		