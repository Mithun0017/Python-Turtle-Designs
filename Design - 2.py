import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
t.pensize(8)
def draw():
     h = 0.9
     n = 98
     for i in range(679):
          c = colorsys.hsv_to_rgb(h,1,0.9)
          h += 1/n
          t.color(c)
          t.fillcolor('black')
          t.begin_fill()
          t.circle(43)
          t.rt(20)
          t.bk(45)
          t.up()
          t.goto(7,56)
          t.down()
          t.circle(i,23)
          t.rt(55)
          t.fd(i)
          t.end_fill()
draw()
t.done()
