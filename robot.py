import turtle as t

# Function to draw a rectangle
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

# Function to draw a circle
def circle(radius, color, x, y):
    t.penup()
    t.goto(x, y - radius)  # Move to the starting position
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

# Function to draw the turtle
def draw_turtle():
    # Set the background color and the turtle's speed
    t.speed('slow')
    t.bgcolor('Dodger blue')
    
    # Draw the feet
    t.goto(-100, -150)
    rectangle(50, 20, 'green')
    
    t.goto(-30, -150)
    rectangle(50, 20, 'green')
    
    # Draw the legs
    t.goto(-28, -50)  
    rectangle(15, 100, 'grey')
    
    t.goto(-65, -50)
    rectangle(15, 100, 'grey')
    
    # Draw the body
    t.goto(-90, 100)
    rectangle(100, 150, 'red')
    
    # Draw the arms
    t.goto(-150, 70)
    rectangle (60, 15, 'grey') 
    t.goto(-150, 110)
    rectangle (15, 40, 'grey')

    t.goto (10, 70)
    rectangle (60, 15, 'grey') 
    t.goto (55, 110) 
    rectangle (15, 40, 'grey')

    # Draw the neck
    t.goto(-50, 120)
    rectangle(15, 20, 'grey')
    
    # Draw the head
    t.goto(-85, 170)
    rectangle(80, 50, 'green')
    
    # Draw the eyes
    t.goto(-60, 160)
    rectangle(30, 10, 'white')
    
    t.goto(-55, 155)
    rectangle(5, 5, 'black')
    
    t.goto(-40, 155)
    rectangle(5, 5, 'black')
    
    # Draw the mouth
    t.goto(-65, 135)
    t.right(5)
    rectangle(40, 5, 'black')
    
    # Draw a smile
    t.goto(-65, 130)
    t.setheading(-60)
    t.circle(20, 120)  # Smiling arc

    
# Set up the turtle
t.penup()


# Draw the turtle
draw_turtle()

# Hide the turtle and finish
t.hideturtle()
t.done()
