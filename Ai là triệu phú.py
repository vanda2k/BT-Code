# name = input("Xin moi ban nhap ten: ")
# print("""Chao mung %s da den voi chuong trinh ai la trieu phu!"""%name)
# money = 0
# realdy = input("Neu ban da san sang nhap \"ss\" de bat dau: ")
# if realdy == "ss":
#     # Cau 1
#     print("""Cau 1: Dat nuoc viet nam co bao nhieu thu do ?
#     A. 1    B. 2    C. 3    D. 4""")
#     anser = input("Dap an cua ban la: ")
#     if anser == "B":
#         money += 1000
#         print("Dap an chinh xac!")
#     else:
#         money = money
#         print("Rat tiec ban phai dung cuoc choi tai day voi so tien %s VND"%money)
#         print("Cam on ban da tham gia chuong trinh!")
#         exit()
#     # Cau 2
#     print("""Cau 2: Con vit co may chan ?
#         A. 1    B. 2    C. 3    D. 4""")
#     anser = input("Dap an cua ban la: ")
#     if anser == "B":
#         money += 1000
#         print("Dap an chinh xac!")
#     else:
#         money = money
#         print("Rat tiec ban phai dung cuoc choi tai day voi so tien %s VND"%money)
#         print("Cam on ban da tham gia chuong trinh!")
#         exit()
#     # Cau 3
#     print("""Cau 2: Mot de thi dai hoc mon toan gom co bao nhieu cau ?
#         A. 10    B. 20    C. 35    D. 50""")
#     anser = input("Dap an cua ban la: ")
#     if anser == "D":
#         money += 1000
#         print("Dap an chinh xac!")
#     else:
#         money = money
#         print("Rat tiec ban phai dung cuoc choi tai day voi so tien %s VND"%money)
#         print("Cam on ban da tham gia chuong trinh!")
#         exit()
# List = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
# for i in List:
#     if i[0] == i[-1] and len(i) > 3:
#         print(i)
# print(List.count(List[1]))
# cout = 0
# n = int(input("Nhap vao so nguyen n: "))
# Newlist = [1, 1, 0, 1, 1, 0, 0, 1, 1]
# print(Newlist.count(n))

# List = input("Nhap vao List: ")
# List = List.split(" ")
# print(List)
# sum = 0
# for i in List:
#     sum += int(i)
# print(sum)
#
# n = int(input("Nhap vao n: "))
# b = []
# while n > 0:
#     r = n % 2
#     b.append(r)
#     n = n // 2
# print(b)
# b.reverse()
# print(b)
# S = 0
# C = len(b)-1
# for i in b:
#     S += i * 2** C
#     C -= 1
# print(S)

# List1 = [1, 3, 5, 6, -1, -5, 8, 6, 7, -4, -5, 5]
# new_list = []
# for i in List1:
#      if i not in new_list:
#           new_list.append(i)
# print(List1)
# print(new_list)
# new_list.sort(reverse=False)
# print(new_list)
# n = input("Nhap vao list: ")
# List = n.split(",")
# print(List)
# Tich = 1
# for i in List:
#      i = int(i)
#      Tich *= i
# print(Tich)
# n = input("Nhap vao n: ")
# count = 0
# if n not in List:
#      print("Phan tu khong co trong danh sach")
# for i in List:
#      if n == i and n in List:
#           count += 1
# print(f"So lan xuat hien cua {n} trong danh sach la: {count}")
#y1
"""List1 = [1, 3, 5, 6, -1, -5, 8, 6, 7, -4, -5, 5] #Tao danh sach moi khong chua cac pt giong
new_list = []
print(List1)
for i in List1:
     if i not in new_list:
          new_list.append(i)
print(new_list)"""
#Bai 4:
n = input("Nhap vao cac phan tu: ")
List1 = n.split(",")
print(List1)
Sum = 0
Tich = 1
for i in List1:
     # Ep kieu du lieu tu str ve int
     Sum += int(i)
     Tich *= int(i)
print(Sum)
print(Tich)
# Y 3
print("Trung binh cong cua danh sach la: ",(Sum/len(List1)))

# Y 4
x = input("Nhap vao so bat ki: ") # 4
count = 0
if x not in List1:
     print("khong co phan tu ",x,"trong danh sach")
for k in List1:
     if x == k:
          count += 1
print("So ",x,"xuat hien ",count)

