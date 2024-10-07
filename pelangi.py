import random
import turtle as tur

def get_turn_size():
    turn_size = input('enter turn size (wide, square, narrow): ')
    return turn_size

def get_line_length():
    choice = input('enter line length (long, medium, short): ')
    if choice == 'long':
        line_length = 250
    elif choice == 'medium':
        line_length = 200
    else:
        line_length = 100
    return line_length

def get_line_width():
    choice = input('enter line width (superthick, thick, thin): ')
    if choice == 'superthick':
        line_width = 40
    elif choice == 'thick':
        line_width = 25
    else:
        line_width = 10
    return line_width

def inside_window():
    left_limit = (-tur.window_width() / 2) + 100
    right_limit = (tur.window_width() / 2) - 100
    top_limit = (tur.window_height() / 2) - 100
    bottom_limit = (-tur.window_height() / 2) + 100
    (x, y) = tur.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

def move_turtle(line_length, turn_size):
    # Daftar warna-warna yang akan digunakan
    pen_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    
    # Pilih warna acak dari daftar pen_colors untuk warna garis
    tur.pencolor(random.choice(pen_colors))
    
    tur.colormode(255)  # Mode warna 255 (RGB)
    
    # Warna acak untuk fill color
    tur.fillcolor(random.choice(pen_colors))
    tur.shapesize(3, 3, 1)  # Ukuran turtle
    tur.stamp()  # Stempel turtle pada posisi saat ini

    if inside_window():
        if turn_size == 'wide':
            angle = random.randint(120, 150)
        elif turn_size == 'square':
            angle = random.randint(80, 90)
        else:
            angle = random.randint(20, 40)
        tur.right(angle)
        tur.forward(line_length)
    else:
        tur.backward(line_length)

# Ambil panjang garis, ketebalan garis, dan ukuran belokan dari user
line_length = get_line_length()
line_width = get_line_width()
turn_size = get_turn_size()

# Inisialisasi turtle
tur.shape('turtle')
tur.fillcolor('green')
tur.bgcolor('black')
tur.speed('fastest')
tur.pensize(line_width)

# Loop untuk menggambar terus menerus dengan garis warna-warni
while True:
    move_turtle(line_length, turn_size)
