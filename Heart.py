"""
------------------------------------------------------------------------
------------------------------------------------------------------------
Author: Ishan Shah

------------------------------------------------------------------------
"""
import turtle as t
pen = t.Turtle()
t.bgcolor('#9966cc')
t.delay(8)
pen.color('#ffe4e1')
pen.begin_fill()
pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-92, 100)
    pen.color('red')
    pen.write('Nisa Da Goat!!!', font=("Comic Sans MS", 16))
txt()
pen.end_fill()
t.exitonclick()

mystr = 'yes'
yourstr = 'no'
mystr += yourstr * 2
print(mystr)