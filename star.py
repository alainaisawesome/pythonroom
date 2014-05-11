import turtle


world  = turtle.Screen()
world.bgcolor("red")

t1 = turtle.Turtle()
t1.color("white")
t1.left(30)
t1.hideturtle()
t2 = turtle.Turtle()
t2.color("white")
t2.left(150)
t2.hideturtle()

for i in range(22):
	t1.left(i)
	t1.forward(8)
	

for j in range(22):
	t2.right(j)
	t2.forward(8)
	
t3 = turtle.Turtle()
t3.hideturtle()
t3.setpos(-50, -50)
t3.write("I love you mom, HAPPY MOTHER'S DAY!")
