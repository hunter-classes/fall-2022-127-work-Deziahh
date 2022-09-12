import turtle

def hexagon(t,x,y,w,color,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()

  for i in range(8):
    t.forward(sidelen)
    t.right(45)

def ngon(t,numsides,x,y,color,width,sidelen):
  t.penup()
  t.goto(x,y)
  t.width(width)
  t.color(color)
  t.pendown()
  for i in range(numsides):
    t.forward(sidelen)
    t.right(360/numsides)

wn = turtle.Screen()

hex = turtle.Turtle()
n = turtle.Turtle()
hexagon(hex, 20, 20, 5, "red", 100)
ngon(n, 6, 45, 20, "blue", 5, 50)
