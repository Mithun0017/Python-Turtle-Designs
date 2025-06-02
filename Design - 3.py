from turtle import*
from colorsys import*
bgcolor('black')
tracer(50)
pensize(4)
h = 0
for i in range(600):
     color(hsv_to_rgb(h,1,1))
     h += 0.005
     fd(i)
     circle(20,70)
     if i%2 == 0:
          circle(20,70)
done()
