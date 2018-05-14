import turtle

def draw_square(sample):
    for i in range(1,5):
        sample.forward(100)
        sample.right(90)

def draw():
    window = turtle.Screen()
    window.bgcolor("red")
    #Square
    andy = turtle.Turtle() 
    andy.shape("circle")
    andy.color("yellow")
    andy.speed(10)
    for i in range(1,37):
        draw_square(andy)
        andy.right(10)

    #josh = turtle.Turtle()
    #josh.shape("arrow")
    #josh.color("white")
    #josh.circle(50)

    #brad = turtle.Turtle()
    #brad.shape("square")
    #brad.color("blue")
    
    
    window.exitonclick()

draw()
