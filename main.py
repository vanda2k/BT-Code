# a = int(input("Nhap vao so a: "))
# b = int(input("Nhap vao so b: "))
# c = 1
# for i in range(1, b+1):
#     c = c * a
#     print(f"Lan thu {i} = ",c)
#
# print(f"Ket qua cua {a}^{b} = ",c)
#
# for i in range(a, b+1):
#     print(i ** 2, end="-")
#     c += i**2
# print()
# print(f"Tong binh phuong tu {a} den {b} la: ",c)

# money = float(input("Nhap vao so tien ban co: "))
# tong = money
# year = int(input("Nhap vao so nam ban muon gui: "))
# tongtien = 0
# rut = 0
# tongrut = 0
# for i in range(year):
#     money = money + money * 0.12
#     tongtien = money
#     rut = tongtien * 0.1
#     money = tongtien - rut
#     tongrut += rut
#     print("==============================")
#     print(f"Tong tien khi chua rut: ",tongtien)
#     print(f"Tien rut sau nam {i+1}: ",rut)
#     print(f"Tong tien sau khi rut con lai sau nam {i + 1}: ", money)
#
# for i in range(year):
#     tong = tong + tong * 0.12
# print("=====================================")
# print(f"Tong tien sau {year} nam gui la: ",tong)
# print(f"Tong tien sau moi nam rut mot lan la: ",tongrut)
# print(f"Tong tien sau moi nam rut mot lan la: ",tong - tongrut)
# nums = int(input("Nhập số tiền bạn muốn gửi:"))
# years = int(input("Nhập số năm bạn muốn gửi:"))
# if years == 1:
#     nums = nums+(nums*12/100)
#     print("Số tiền bạn có sau khi gửi là:",nums)
# elif years > 1:
#     nums = nums+((nums*12/100)*years)
#     print("Số tiền bạn có sau khi gửi là:",nums)
# for i in range(1,years+1,1):
#     nums =  nums - nums/10
# print("Nếu mỗi năm rút ra 1/10 số tiền thì khi hết hạn gửi thì có:",nums)

# S = 0
# i = 1
# while i < money +1:
#     S = 1 + 1/i**3
#     i += 1
# print(S)

#
# a = 1.12345678
#
# #Cach 1
# print("lam tron sau dau phay 3 chu so %0.3f"%a)
#
# #Cach 2
#
# print("Lam tron sau dau phay 4 chu so ",round(a, 4))
# str1 = "Nguyễn Trâm Anh, Đỗ Đức Hải, Vũ Tiến Hồng Đức"
#
# name = input("Nhap vao ten cua ban: ")
# if name in str1:
#     print("Co hoc sinh trong danh sach")
# else:
#     print("Khong co hoc sinh trong danh sach")

# name = "coding for kids Ha Noi"
# # ham viet hoa cac chu cai dau tien
# print(name.capitalize())
# sentences = input("Viết 1 câu văn ngắn: ")
# print(sentences.split(","))
# if "e" in sentences:
#     print("Co e")
# else:
#     print("Kho co")
# count = 0
# for i in range(len(sentences)):
#     if sentences[i] == "e":
#         count = count + 1
#     else:
#         print("khong")
#         break
# print("Số lượng kí tự e là:",count)

# dtb = int(input("Nhap vao dtb: "))
# if dtb > 0:
#     print("Day la so nguyen duong")
# else:
#     print("Day la so nguyen am")
# if dtb >9.5:
#     print("Xuat sac")
# if 8<dtb<9.5:
#     print("Goi")
# if 6.5<dtb<8:
#     print("Kha")
# if 5 < dtb < 6.5:
#     print("Trung binh")
# else:
#     print("yeu")
# Viết chương trình in ra dãy sau: -3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4
# def oscillate(start, end):
#     for i in range(start, end):
#         print(i, -i, end=" ")
#
# oscillate(-3, 5)
"""
def nhaphoso():
    global hoso
    hoso=[]
    t=1
    while (t==1):
 u=1
 while (u==1):
 x=input("masv :")
 d=0
 for i in range(0,len(hoso)):
     if (hoso[i][0]==x):
     d=d+1
     print("ban nhap lai ,masv da ton tai")
 if (d==0):
 u=0
 ds=[]
 ds.append(x)
 x=(input("ho ten: "))
 ds.append(x)
 x=(input("ngay sinh: "))
 ds.append(x)
 x=int(input("diem: "))
 ds.append(x)
 hoso.append(ds)
 m=input("ban co muon nhap nua khong ?")
 if m=='k':
      t=0
 for i in range(0, len(hoso)):
 print("masv :",hoso[i][0],"   ho ten :",hoso[i][1],"  n/s :",hoso[i][2],"   diem :",hoso[i][3])
def timkiem():
 global hoso
 u=1
 while (u==1):
 masv=input("nhap masv can tim")
 d=0
 for i in range(0,len(hoso)):
 if (hoso[i][0]==masv):
 d=d+1
 print("ho so sv dc tim thay la ")
 print("masv :",hoso[i][0],"   ho ten :",hoso[i][1],"  n/s :",hoso[i][2],"   diem :",hoso[i][3])
 if (d==0):
 print("khong tim thay sv co masv la",masv)
 a=input("ban co muon tim nua khong ? c/k ")
 if (a=="k"):
 u=0
def xoahoso():
 global hoso
 u=1
 while (u==1):
 masv=input("nhap masv can xoa")
 d=0
 t=0
 for i in range(0,len(hoso)):
 if (hoso[i][0]==masv):
     d=d+1
     print("ho so sv dc tim thay la ")
     print("masv :",hoso[i][0],"   ho ten :",hoso[i][1],"  n/s :",hoso[i][2],"   diem :",hoso[i][3])
     a=input("ban co muon xoa khong ? c/k ")
     if (a=="c"):
          hoso.pop(i)
          break
 if (d==0):
 print("khong tim thay sv co masv la",masv)
 a=input("ban co muon xoa nua  khong ? c/k ")
 if (a=="k"):
 u=0
def inhoso():
 global hoso
 for i in range(0, len(hoso)):
          print("masv :",hoso[i][0],"   ho ten :",hoso[i][1],"  n/s :",hoso[i][2],"   diem :",hoso[i][3])
def ktdo():
 global hoso
 kt=int(input("ban nhap vao diem dk"))
 print("danh sach sv do la")
 for i in range(0,len(hoso)):
 if (hoso[i][3]>=kt):
 print("masv :",hoso[i][0],"   ho ten :",hoso[i][1],"  n/s :",hoso[i][2],"   diem :",hoso[i][3])
def xeptt():
 global hoso
 print("danh sach sau khi sap tt la")
 for i in range(0,len(hoso)):
 for j in range(i+1,len(hoso)):
 if (hoso[j][3]>hoso[i][3]):
 m=hoso[i]
 hoso[i]=hoso[j]
 hoso[j]=m
def suahoso():
 global hoso
 u=1
 while (u==1):
           masv=input("nhap masv can sua ")
           d=0
           for i in range(0,len(hoso)):
            if (hoso[i][0]==masv):
            d=d+1
            print("ho so sv dc tim thay la ")
            print("masv :",hoso[i][0],"   ho ten :",hoso[i][1],"  n/s :",hoso[i][2],"   diem :",hoso[i][3])
            a=input("ban xem lai roi sua ")
            hoso[i][1]=input("ho ten : ")
            hoso[i][2]=input("ngay sinh :")
            hoso[i][3]=int(input("diem  :"))
            break
           if (d==0):
             print("khong tim thay sv co masv la",masv)
           a=input("ban co muon tim nua khong ? c/k ")
           if (a=="k"):
            u=0
nhaphoso()
timkiem()
xoahoso()
inhoso()
ktdo()
xeptt()
inhoso()
suahoso()
inhoso()
"""
print(max(2))






