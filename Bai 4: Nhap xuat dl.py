# # import os
# print("Tro choi ai la trieu phu")
# score = 0
# choose = input("Neu ban san sang tham gia, xin moi nhap ss: ")
# if choose == "ss":
#     print("""Cai 1: Con vit co may chan ?
#     A. 2    B. 3     C. 4    D. 5
#     """)
#     anser = input("Ban chon dap an: ")
#     if anser == "A":
#         print("Ban da tra loi dung!")
#         score += 1000
#     else:
#         print("Rat tiec! Ban phai dung cuoc choi tai day.")
#         exit()
#     print("""Cai 2: Co chuot nao di bang hai chan ?
#     A. Mickey  B. Donal   C, Jerry   D. Con nao cung di bang hai chan""")
#     anser = input("Ban chon dap an: ")
#     if anser == "D":
#         print("Ban da tra loi dung!")
#         score += 1000
#     else:
#         print("Rat tiec! Ban phai dung cuoc choi tai day.")
#         print("Ban se ra ve voi %s"%score)
#         exit()
"""Thiết kế một chương trình cỗ máy xử lý văn bản
Cho một đoạn thơ sau: Chao mung cac em den voi khoa hoc Python co ban -  cua trung tam coding for kid ha Noi
"""
"""print(""Chuong trinh xu ly van ban
1. Viet hoa chu cai dau tien
2. In hoa tat ca cac chu cai
3. In thuong tat ca cac chu cai
4. Tim kien vi tri cua tu trong chuoi
5. Tach chuoi thanh list
6. Dem so luong tu bat ki trong chuoi
7. Dem so ki tu co trong chuoi
8. Noi chuoi
9. Chuan hoa chuoi
10. ket thuc"")
print("-"*30)
str1 = input("Moi ban nhap vao mot chuoi: ")
choose = int(input("Ban chon: "))
while choose != 10:
    if choose == 1:
        print("Chuoi sau khi viet hoa chu cai dau: ",str1.capitalize())
    elif choose == 2:
        print("Chuoi sau khi in hoa toan bo: ",str1.upper())
    elif choose == 3:
        print("Chuoi sau khi in thuong toan bo: ",str1.lower())
    elif choose == 4:
        findx = input("Moi ban nhap vao tu can tim: ")
        print(f"vi tri xuat hien cua tu {findx} la: ", tr1.find(findx))
    elif choose == 5:
        print("Chuoi sau khi tach thanh List",str1.split())
    elif choose == 6:
        x = input("Nhap vao tu bat ky: ")
        if x in str1:
            print(f"Co tu {x} trong chuoi")
        else:
            print(f"Khong co tu {x} trong chuoi")
        count = 0
        for i in range(len(str1)):
            if str1[i] == x:
                count += 1
        print(f"Tu {x} xuat hien {count} lan")
    elif choose == 7:
        print(f"Tong so phan tu co trong chuoi la: ",len(str1))
    elif choose == 8:
        str2 = input("Nhap vao mot chuoi can noi: ")
        print("Chuoi sau khi noi la: ",str1+str2)
    elif choose == 9:
        print("Chuoi sau khi chuan hoa: ",str1.title())
    elif choose == 10:
        print("Cam on ban da su dung chuong trinh!")
        break
    else:
        print("Khong co lua chon nay!")
    choose = int(input("Moi ban chon lai: "))
print("Thoat chuong trinh")
"""