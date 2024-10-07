import turtle

# Inisialisasi turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")  

# Buat turtle object untuk menggambar
pen = turtle.Turtle()
pen.speed(2) 

# Fungsi untuk menggambar persegi panjang (untuk lapisan kue)
def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Menggambar lapisan kue bagian bawah
pen.penup()
pen.goto(-100, -100)  
pen.pendown()
draw_rectangle(pen, 200, 50, "chocolate")

# Menggambar lapisan kue bagian tengah
pen.penup()
pen.goto(-80, -50)
pen.pendown()
draw_rectangle(pen, 160, 50, "pink")

# Menggambar lapisan kue bagian atas
pen.penup()
pen.goto(-60, 0)
pen.pendown()
draw_rectangle(pen, 120, 50, "yellow")

# Menggambar lilin
pen.penup()
pen.goto(-10, 50)
pen.pendown()
pen.fillcolor("blue")
pen.begin_fill()
pen.left(90)
pen.forward(40)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(40)
pen.right(90)
pen.forward(10)
pen.end_fill()

# Menggambar api lilin
pen.penup()
pen.goto(-5, 90)
pen.pendown()
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# Menggambar tulisan "Happy Birthday"
pen.penup()
pen.goto(-70, -150)
pen.pendown()
pen.color("purple")
pen.write("Happy Birthday 🥳🎉", font=("Arial", 24, "bold"))

# Menyembunyikan turtle
pen.hideturtle()


turtle.done()
