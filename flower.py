import turtle as tur

s = tur.Screen()
s.setup(800, 800)
s.bgcolor('#262626')


tur.pencolor('#540d6e')
tur.speed(-10)
tur.tracer(100)  
tur.pensize(1)


col = ('#FF7F3F', '#FBDF07', '#89CFFD', '#F94892')


for i in range(2):
    for n in range(400):
        tur.color(col[n % 4])
        tur.circle(190 - n / 2, 90)
        tur.left(90)
        tur.circle(190 - n / 2, 90)
        tur.color(col[n % 4])
    tur.left(30)


s.exitonclick()  
