# Nhap vao cac so chia het co
# n = int(input("Nhap vao so n: "))
# count = 0
# while (count < n < 100):
#     if (count % 5 == 0) and (count % 7 ==0):
#         print(count)
#     count += 1
# n = int(input("Nhap vao so co 3 chu so: "))
# while (n<100 and n>1000):
#     n = int(input("Nhap vao so co 3 chu so: "))
#
# b = str(n)

# for i in range(100, 1000, 1):
#     b = str(i)
#     if (int(b[0])**3 + int(b[1])**3 + int(b[2])**3) == i:
#         print(b[0],b[1],b[2])
#         print(i)
print("Hello World")
print("Ham tinh tong hai so nguyen duong: ")


def Tong(a, b):
    return a + b

a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))
while a < 0:
    a = int(input("Nhap vao so nguyen a: "))
while b < 0:
    a = int(input("Nhap vao so nguyen b: "))


print(f"Tong cua hai so {a}+{n}={Tong(a,b)}")