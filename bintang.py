import turtle
import random

# Inisialisasi layar
screen = turtle.Screen()
screen.bgcolor("#003366")  # Menggunakan warna biru tua untuk langit malam
screen.title("Gambar Bintang Acak")

# Fungsi untuk menggambar bintang dengan jumlah titik acak
def draw_star(turtle_obj, x, y, points, size, color):
    angle = 180 - (180 / points)
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    
    # Menggambar bintang
    for _ in range(points):
        turtle_obj.forward(size)
        turtle_obj.right(angle)

# Fungsi utama untuk menggambar bintang acak
def random_star():
    t = turtle.Turtle()
    t.speed(0)  # Kecepatan maksimum
    t.hideturtle()  # Sembunyikan turtle
    
    # Pilih warna acak
    colors = ['yellow', 'white', 'blue', 'red']
    
    # Pilih jumlah bintang
    for _ in range(random.randint(50, 100)):  # Jumlah bintang acak antara 50 dan 100
        x = random.randint(-300, 300)  # Posisi X acak
        y = random.randint(-300, 300)  # Posisi Y acak
        points = random.randint(5, 8)  # Jumlah titik acak antara 5 hingga 8
        size = random.randint(10, 50)  # Ukuran acak antara 10 hingga 50
        color = random.choice(colors)  # Warna acak
        
        draw_star(t, x, y, points, size, color)

# Jalankan fungsi utama
random_star()

# Tutup layar saat diklik
screen.exitonclick()
