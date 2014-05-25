import turtle
t = turtle.Turtle()
distances = range(10,100)
colors = [ "red", "green", "blue", "pink" ]
for distance in distances:
	t.left(10)
	for color in colors:
		t.speed(0)
		t.color(color)
		t.forward(distance)
		t.forward(10)
		t.left(90)
	



	
	