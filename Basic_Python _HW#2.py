Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> def Cir():
	tao.circle(20)

	
>>> def Go(x,y):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()

	
>>> tao.color("green")
>>> tao.shape("turtle")
>>> x=0
>>> y=0
>>> n=5
>>> count=0
>>> while n > 0:
	tao.begin_fill()
	Cir()
	tao.end_fill()
	n = n -1
	x = x+50
	Go(x,y)
	if n == 0 and count !=3:
		n = n + 5
		x = 0
		y = y - 50
		if tao.color() ==('green', 'green'):
			tao.color("red")
		else:
			tao.color("green")
		Go(x,y)
		count = count + 1

		
>>> 
