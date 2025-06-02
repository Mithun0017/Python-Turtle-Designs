from turtle import*
from colorsys import*
bgcolor('black')
pensize(3)
speed(0)
h = 0
up()
goto(50,150)
down()
for i in range(12):
     color(hsv_to_rgb(h,1,1))
     circle(50)
     for j in range(26):
          h += 0.005
          fd(50)
          bk(50)
          rt(15)
     up()
     fd(100)
     down()
done()
