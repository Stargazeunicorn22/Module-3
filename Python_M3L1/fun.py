import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Mesh Pattern")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["light pink", "yellow", "light green", "light blue"]

for i in range(120):
    t.pencolor(colors[i % 4])
    t.forward(i * 3)
    t.right(91)

t.hideturtle()

t.speed(2)
t.width(3)
t.pencolor("yellow")
t.fillcolor("yellow")

t.penup()
t.goto(-65, 20)
t.setheading(0)
t.pendown()

t.begin_fill()
for i in range(5):
    t.forward(130)
    t.right(144)
t.end_fill()

t.speed(0)
t.width(1)

for i in range(36):
    t.pencolor(colors[i % 4])
    t.fillcolor(colors[i % 4])
    
    t.begin_fill()
    for _ in range(4):
        t.forward(150)
        t.right(90)
    t.end_fill()
    
    t.right(10)
    
screen.exitonclick()
