from turtle import*
def draw(x,y):
     rt(x)
     fd(y)
tracer(5)
fd(100)
bgcolor('black')
width(4)
color('green')
for i in range(2001):
     fd(i)
     draw(90,i)
     draw(90,i)
     draw(270,i)
     draw(90,i)
     circle(100,90)
done()
