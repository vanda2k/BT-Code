
n = int(input("Nhap vao so nguoi can thue: "))

b_start = []
b_end = []
b_price = []
for i in range(n):
    print(f"May thu {i+1}: ")
    s = int(input(f"Nhap vao gio bat dau {i+1}: "))
    e = int(input(f"Nhap vao gio ket thuc {i+1}: "))
    p = int(input(f"Nhap vao giat ien {i+1}: "))
    b_start.append(s)
    b_end.append(e)
    b_price.append(p)


print("Thoi gian chua xep sap")
print(b_start)
print(b_end)
print(b_price)

for i in range(n):
    print(f"May thu {i+1}: Thoi gian vao {b_start[i]}, thoi gian ra {b_end[i]}, gia {b_price[i]}")
start = b_start
end = b_end
price = b_price
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if end[j] < end[i]:
            tg = end[j]
            end[j] = end[i]
            end[i] = tg
# Sort start
            tgs = start[i]
            start[i] = start[j]
            start[j] = tgs
# Sort price
            tgp = price[i]
            price[i] = price[j]
            price[j] = tgp
print("Sau khi sap xep theo thoi gian ket thuc")
print(start)
print(end)
print(price)

L = [0]*n
cs = []
for i in range(n):
    L[i] = price[i]
    for j in range(i):
        # print(f"chi so price: ",price[i])
        if (end[j] <= start[i]) and (L[i] < L[j]+price[i]):
            L[i] = L[j] + price[i]
            c = i
            cs.append(c)
            print(f"{L[i]} = {L[j]} + {price[i]}")
            print(f"chi so max",cs)
print(cs)

# Truy vet

print(L)
print("Thoi gian lon nhat: ")
M = L[0]
# for i in range(n):
#     if M <= L[i]:
#         M = L[i]
#         cs = i
for i in range(n):
    if (L[i] > L[0]):
        M = L[i]
        cs = i
        print(start[cs], end[cs], price[cs])
        for j in range(n):
            if (start[cs] == b_start[j] and end[j]== b_end[j] and b_price[cs]==price[j]):
                print(b_start[j], end[j], price[j])
                print(j)

print(f"So tien loi lon nhat la: ",M)