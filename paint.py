import turtle
def draw_square(some_turtle):
	for x in range(1,4):
		some_turtle.forward(120)
		some_turtle.right(90)
	some_turtle.forward(120)
	some_turtle.right(95)
 
def draw_trigle(some_tringle):
	for i in range(1,3):
		some_tringle.forward(100)
		some_tringle.right(120)
	some_tringle.forward(100)
	some_tringle.right(125)
def draw_art ():
	window = turtle.Screen()
	window.bgcolor("gray")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(50)
	i = 1
	while i < 74:
		draw_square(brad)
		i += 1

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("red")
	angie.speed(50)
	i = 1
	while i < 74:
		angie.circle(140)
		angie.right(5)
		i += 1

	magi = turtle.Turtle()
	magi.color("yellow")
	magi.speed(50)
	i = 1
	while i < 74:
		draw_trigle(magi)
		i += 1

	window.exitonclick()

draw_art()