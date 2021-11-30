
"""#Chuong trinh A
A = float(input("Nhap vao so tien gui: "))
B = float(input("Nhap vao so tien sau gui: "))
K = 0.0075
T = 0
while A < B:
    A = A + A * K
    T = T + 1

print("Co",A,"trieu dong va phai gui",T,"thang")"""

n = int(input("Nhap vao so n: "))
t = n
if (n > 0):
    n = -n
else:
    t = -n
    n = -n
print(f"tri tuyet doi cua |{t}| = {t}")
print(f"nghich dao cua {t} = {n}")
