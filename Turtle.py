
# Khai bao thu vien
import turtle

# Khoi tao man hinh
screen = turtle.Screen()

# Thay doi mau nen
screen.bgcolor(rgb(100,100,100))

# Khoi tao net vet - but
pen = turtle.Turtle()

# Thiet lap mau cua but
pen.color("blue")

# Thiet lap net but
pen.width(5)

# Thiet lap kieu but
pen.shape("turtle")

# An net ve
# pen.hideturtle()
# Bat dau ve hinh vuong
"""
for i in range(4):
    pen.forward(200)
    pen.left(90)
"""
# Ve hinh tam giac
"""pen.forward(200)
pen.left(120)
pen.forward(200)"""
# Ve hinh ngu giac deu
"""
for i in range(5):
    pen.forward(200)
    pen.left(72)"""
# Ve hinh luc giac deu
# Ve hinh ngoi sao - 144
"""
for i in range(5):
    pen.backward(200)
    pen.right(360*2/5)"""
# Nhac but le
"""
pen.penup()
pen.goto(100, 100)
# Ha but xuong
pen.pendown()
# Ve hinh tron circle(bk)
pen.circle(50)"""

# To mau cho hinh
pen.color("yellow")
pen.begin_fill()
for i in range(5):
    pen.backward(200)
    pen.right(144)
pen.end_fill()


# Tao vong lap hien thi
screen.mainloop()

