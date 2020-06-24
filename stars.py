import turtle

chelsea = turtle.Turtle()
chelsea.getscreen().bgcolor("#994444")

chelsea.penup()
chelsea.goto(-200, 100)
chelsea.pendown()

chelsea.speed(0)

def star(turtle, size):
	if size <= 10:
		return 
	else:	
		turtle.begin_fill()
		for i in range(5):
			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()	


star(chelsea, 360)



turtle.done()