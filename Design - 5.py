from turtle import*
bgcolor('black')
pensize(4)
tracer(100)
c = ['black', 'red', 'black', 'green', 'black', 'blue']
for i in range(500):
     color(c[i%6])
     fd(7)
     lt(88)
     fd(i*3)
     circle(10)
     lt(10)
done()
