import turtle as t

scale=100
t.penup()
t.goto(-200,0)
t.pendown()

def move_to(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()

def draw_siot(xs = 1):
	x, y = t.pos()
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale * xs / 2, y)
	t.goto(x + scale * xs, y2)
	move_to(x, y)

def draw_o():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.5)
	t.left(90)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_ieung(xs = 1):
	x, y = t.pos()
	move_to(x + scale * xs * 0.5, y - scale * 2.2)
	t.setheading(0)
	t.circle(scale * 0.4)
	move_to(x, y)

def draw_hieut(xs = 1):
	x, y = t.pos()
	t.penup()
	t.setheading(0)
	t.forward(scale * xs * 0.4)
	t.pendown()
	t.forward(scale * xs * 0.2)
	move_to(x + scale * xs * 0.2, y - scale * 0.1)
	t.forward(scale * xs * 0.6)
	move_to(x + scale * xs * 0.5, y - scale * 0.8)
	t.circle(scale * 0.3)
	move_to(x, y)

def draw_yeo():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(180)
	move_to(x2, y - scale * 0.4)
	t.forward(scale * 0.2)
	move_to(x2, y - scale * 0.6)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_nieun(xs = 1):
	x, y = t.pos()
	move_to(x+scale*xs*0.3,y-scale*1.5)
	t.pendown()
	t.setheading(270)
	t.forward(scale / 2)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

def draw_jieut(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.forward(scale)
	t.setheading(225)
	t.forward(scale)
	t.backward(scale * 0.5)
	t.left(90)
	t.forward(scale * 0.5)
	move_to(x, y)

def draw_i():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	move_to(x, y)


def draw_final(func=None):
    x,y=t.pos()
    if func!=None:
        move_to(x,y)
        func()
    move_to(x+scale*1.7,y)


draw_siot()
draw_o()
draw_final(draw_ieung())
draw_hieut()
draw_yeo()
draw_final(draw_nieun())
draw_jieut()
draw_i()
draw_final(draw_nieun())

t.exitonclick()
