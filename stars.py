import turtle

chelsea = turtle.Turtle()
chelsea.getscreen().bgcolor("#994444")

def star(turtle, size):
	if size <= 10:
		return 
	else:	
		for i in range(5):
			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)


star(chelsea, 360)



turtle.done()