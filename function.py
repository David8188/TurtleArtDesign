def turn(t,y):
    for times in range (100):
      y=100
      t.forward(y)
      t.left(85)

def mini(t,angle,x):
    for times in range(x):
        polygon(t,50,7)
        t.right(angle)

      
def square( t, distance ):
    for times in range(4):
        t.forward(distance)
        t.left(90)
def triangle( t, distance ):
    for times in range(3):
        t.forward(distance)
        t.left(120)
def pentagon( t, distance ):
    for times in range(5):
        t.forward(distance)
        t.left(72)
def polygon (t,distance,side):
    angle=360/side
    for times in range(side):
        t.forward(distance)
        t.left(angle)
def hexagon( t, distance ):
    for times in range(6):
        t.forward(distance)
        t.left(60)
    
        
def move (t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def pow(t,x):
    for times in range(x):
        t.forward(x+1)
        t.left(140)


