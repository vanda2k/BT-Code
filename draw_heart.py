# import turtle
# def TamTinhTao():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)
# turtle.color("skyblue")
# turtle.begin_fill()
# turtle.left(140)
# turtle.forward(111.65)
# TamTinhTao()
# turtle.left(120)
# TamTinhTao()
# turtle.forward(111.65)
# turtle.end_fill()
# turtle.mainloop()

def timsonguyento(a):
    t = True
    for i in range(2,a):
        if a % i == 0:
            t = False
    return t
n = int(input("Nhập vào số nguyên dương bất kỳ: "))
while n < 0:
    n = int(input("Nhập lại vào số nguyên dương bất kỳ: "))
print("Số nguyên tố",n,"=",timsonguyento(n))
elif