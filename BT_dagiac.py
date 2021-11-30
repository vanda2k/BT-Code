import math

def dodai(x1, y1, x2, y2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d

def dientich(x,y,z):
    P = (x+y+z)/2
    S = math.sqrt(P*(P-x)*(P-y)*(P-z))
    return S

def tamgiac(x, y, z):
    if ((x + y > z) and (y + z > x) and (x + z > y)):
        return True
    else:
        return False

x1, y1 = map(float, input("Nhap vao hai toa do (x1, y1): ").split(","))
x2, y2 = map(float, input("Nhap vao hai toa do (x2, y2): ").split(","))
x3, y3 = map(float, input("Nhap vao hai toa do (x3, y3): ").split(","))
x4, y4 = map(float, input("Nhap vao hai toa do: (x4, y4): ").split(","))

a1 = dodai(x1, y1, x2, y2)
a2 = dodai(x2, y2, x3, y3)
a3 = dodai(x3, y3, x4, y4)
a4 = dodai(x4, y4, x1, y1)
dc = dodai(x2, y2, x4, y4)

if tamgiac(a1, dc, a4) and tamgiac(a2, a3, dc):
    S1 = dientich(a1, dc, a4)
    S2 = dientich(a2, a3, dc)
else:
    print("Khong phai la tu giac")

print(a1,a2,a3, a4, dc)
print("Dien tich tu giac: ",(S1 + S2))

"""n = -1
while n < 0:
    n = int(input("Nhap vao so cong nhan: "))
ds_congnhan = [0] * n
for i in range(n):
    ds_congnhan[i] = int(input("NV: "))
ds_congnhan_moi = []
count = 0
for k in ds_congnhan:
    if k not in ds_congnhan_moi:
        ds_congnhan_moi.append(k)
        count += 1
print("Tong so nhan vien: ",n)
print("Nhan vien sau khi ma hoa: ",ds_congnhan)
print("Nhan vien trung ma: ", ds_congnhan_moi)
print("Tong so nhan vien sau ma hoa:",count)
print(set(ds_congnhan))"""





















