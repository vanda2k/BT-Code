
# cu phap cua ham - def tenham():
"""
def say():
    print("Hello Python")
# Goi lai ham
say()"""
# Ham co tham so
"""
def tong(a, b):
    print("Tong cua hai so: ",a+b)
def tich(a, b):
    print("Tich cua hai so: ",a*b)

tong(30,20)

c = int(input("Nhap vao so thu 1: "))
d = int(input("Nhap vao so thu 2: "))
tong(c,d)
tich(c,d)"""

"""
def tong1(a, b):
    return a + b

c = tong1(1,1)
print("Tong cua 2 so la: ",c)
"""
# Viet ham tinh dien tich cua cac hinh sau: Hinh Chu Nhat, Hinh Vong, Hinh Tron
"""import math

def circle(r):
    return r*r*math.pi
print("Dien tich hinh tron: ",circle(r))"""

# Bien toan cuc global tenbien
"""def sotunhien():
    global a
    a = 10
    print(a)"""
# Viet ham tinh tong cua cac so tu nhien: S = 1, 2, 3, 4, 5, 6, 7...,n voi n la so nhap vao tu ban phim

def Sum(n):
    tong = 0
    for i in range(1, n+1):
        tong += i
    return tong
n = int(input("Nhap vao n: "))
print("Tong cua day so: ", Sum(n))

"""Bài 3: Viết chương trình tính kết quả biểu thức 
S= 1+ 1/2 + 1/3 +...+1/n (làm tròn 5 chữ số thập phân). 
Viet ham tinh tong S"""


