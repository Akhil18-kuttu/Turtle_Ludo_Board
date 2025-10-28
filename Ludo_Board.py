import turtle

t=turtle.Turtle()
t.speed(0) 
t.pensize(5)
t.penup()
t.goto(-250, 250) 
t.pendown()

for _ in range(4):
    t.forward(600)
    t.right(90)
t.forward(600)

#right up coloum
t.fillcolor("green")
t.begin_fill()
for _ in range(4):
    t.right(90)
    t.forward(240)
t.end_fill()

t.penup()
t.right(90)
t.forward(600)
t.pendown()

#left up coloum
t.fillcolor("red")
t.begin_fill()
for _ in range(4):
    t.right(90)
    t.forward(240)
t.end_fill()
   

t.penup()
t.right(90)
t.forward(600)
t.pendown()

#right down coloum
t.fillcolor("yellow")
t.begin_fill()
for _ in range(4):
    t.right(90)
    t.forward(240)
t.end_fill()

t.penup()
t.right(90)
t.forward(600)
t.pendown()

#left down coloum
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.right(90)
    t.forward(240)
t.end_fill()

# up coloum 
t.penup()
t.right(90)
t.forward(360)
t.right(90)
t.forward(40)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for _ in range(6):
    for _ in range(4):
        t.right(90)
        t.forward(40)
    t.forward(40)
t.forward(80)
t.end_fill()

t.penup()
t.left(90)
t.forward(240)
t.left(90)
t.forward(120)
t.left(90)
t.forward(40)
t.pendown()

for _ in range(6):
    for _ in range(4):
        t.left(90)
        t.forward(40)
    t.forward(40)
t.forward(80)

t.penup()
t.forward(240)
t.left(90)
t.forward(120)
t.left(90)
t.forward(40)
t.pendown()

for _ in range(6):
    for _ in range(4):
        t.left(90)
        t.forward(40)
    t.forward(40)
t.forward(80)

t.penup()
t.right(90)
t.forward(240)
t.right(90)
t.forward(120)
t.right(90)
t.forward(40)
t.pendown()

for _ in range(6):
    for _ in range(4):
        t.right(90)
        t.forward(40)
    t.forward(40)
t.forward(80)

t.penup()
t.forward(200)
t.left(180)
t.pendown()
for _ in range(6):
    for _ in range(4):
        t.left(90)
        t.forward(40)
    t.forward(40)

t.penup()
t.right(90)
t.forward(240)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.pendown()
for _ in range(6):
    for _ in range(4):
        t.right(90)
        t.forward(40)
    t.forward(40)

t.penup()
t.forward(320)
t.right(90)
t.forward(120)
t.right(90)
t.forward(40)
t.pendown()
for _ in range(6):
    for _ in range(4):
        t.right(90)
        t.forward(40)
    t.forward(40)

t.penup()
t.left(90)
t.forward(240)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.pendown()

for _ in range(6):
    for _ in range(4):
        t.left(90)
        t.forward(40)
    t.forward(40)

t.penup()
t.right(90)
t.forward(160)
t.pendown()

t.right(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)

for _ in range(5):
    for _ in range(4):
        t.left(90)
        t.forward(40)
    t.forward(40)

# red Arrow
t.right(90)
t.fillcolor("red")
t.begin_fill()
t.forward(40)
t.left(135)
t.forward(85)
t.left(90)
t.forward(85)
t.left(135)
t.forward(40)
t.right(90)
t.forward(160)
t.right(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.end_fill()

#green Arrow
t.penup()
t.forward(40)
t.left(90)
t.forward(200)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.forward(40)
t.right(90)
t.forward(160)
t.right(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(200)
t.right(90)
t.forward(40)
t.left(135)
t.forward(85)
t.left(90)
t.forward(85)
t.end_fill()

t.penup()
t.left(135)
t.forward(120)
t.pendown()

#Blue Arrow
t.fillcolor("blue")
t.begin_fill()
t.left(90)
t.forward(40)
t.right(90)
t.forward(160)
t.right(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(200)
t.right(90)
t.forward(40)
t.left(135)
t.forward(85)
t.left(90)
t.forward(85)
t.end_fill()

t.penup()
t.left(135)
t.forward(120)
t.left(90)
t.pendown()

#Yellow Arrow
t.fillcolor("yellow")
t.begin_fill()
t.forward(40)
t.right(90)
t.forward(160)
t.right(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(200)
t.right(90)
t.forward(40)
t.left(135)
t.forward(85)
t.left(90)
t.forward(85)
t.end_fill()

t.penup()
t.right(45)
t.forward(40)
t.left(90)
t.forward(40)
t.pendown()

##yellow inside box
t.fillcolor("white") 
t.begin_fill()                                      
for _ in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

t.penup()
t.left(90)
t.forward(200)
t.pendown()

##red inside box
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

t.penup()
t.left(90)
t.forward(200)
t.pendown()

##green inside box
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

t.penup()
t.left(90)
t.forward(200)
t.pendown()

##blue inside box
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

t.right(90)
t.forward(200)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(80)

for i in range(5):
    t.right(90)
    t.forward(40)
t.forward(40)
for i in range(4):
    t.right(90)
    t.forward(40)
t.forward(40)
for i in range(4):
    t.right(90)
    t.forward(40)
t.forward(40)
for i in range(4):
    t.right(90)
    t.forward(40)
t.forward(40)
for i in range(3):
    t.right(90)
    t.forward(40)
t.forward(40)

t.right(90)
t.forward(120)
t.left(90)
t.forward(40)

for _ in range(5):
  
  for _ in range(4):
    t.left(90)
    t.forward(40)
  t.forward(40)

t.penup()
t.right(90)
t.forward(40)
t.right(90)
t.forward(320)
t.left(90)
t.forward(40)
t.pendown()

for _ in range(5):
  for _ in range(4):
    t.left(90)
    t.forward(40)
  t.forward(40)

t.penup()
t.right(90)
t.forward(40)
t.right(90)
t.forward(320)
t.left(90)
t.forward(40)
t.pendown()

for _ in range(5):
  for _ in range(4):
    t.left(90)
    t.forward(40)
  t.forward(40) 

t.penup()
t.forward(20)
t.right(90)
t.forward(300)
t.pendown()

for _ in range(4):
    t.pensize(10)
    t.right(90)
    t.forward(640)


import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.penup()

# Coordinates for square corners blue
positions = [(-100, 80), (-200, 80), (-100, 180), (-200, 180)]

for x, y in positions:
    t.goto(x, y)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()

# Coordinates for square corners green
positions = [(200, 80), (300, 80), (200, 180), (300, 180)]

for x, y in positions:
    t.goto(x, y)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()

# Coordinates for square corners yellow
positions = [(-100, -220), (-100, -320), (-200, -220), (-200, -320)]

for x, y in positions:
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()

# Coordinates for square corners red
positions = [(200, -220), (200, -320), (300, -220), (300, -320)]

for x, y in positions:
    t.goto(x, y)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()

turtle.done()
