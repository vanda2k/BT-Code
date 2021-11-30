name = [] # name[0]
van = []
anh = []
toan = []
dtb = []
tonghs = 0
while True:
    print("Chuong trinh quan ly hoc sinh")
    print("1. Them hoc sinh")
    print("2. Xem tat ca")
    print("3. Xoa hoc sinh")
    choose = int(input("ban chon: "))
    if choose == 1:
        print("Them hoc sinh")
        n = int(input("Nhap so hoc sinh: "))
        tonghs = tonghs + n
        for i in range(tonghs):
            print("Hoc sinh thu ",i+1)
            ten = input("Nhap vao ten hoc sinh: ")
            name.append(ten)
            diem_van = float(input("Nhap vao diem van: "))
            van.append(diem_van)
            diem_anh = float(input("Nhap vao diem anh: "))
            anh.append(diem_anh)
            diem_toan = float(input("Nhap vao diem toan: "))
            toan.append(diem_toan)
            diemtb = (diem_anh + diem_toan + diem_van)/3
            dtb.append(diemtb)
    elif choose == 2:
        print("xem tat ca hoc sinh")
        for i in range(tonghs):
            print(i+1, name[i],toan[i], anh[i], van[i], dtb[i])
    elif choose == 3:
        print("Xoa hoc sinh")
        vitri = int(input("Nhap vao vi tri: "))
        if (0 < vitri < tonghs):
            del name[vitri-1]
            del van[vitri-1]
            del anh[vitri-1]
            del toan[vitri-1]
            del dtb[vitri-1]
            tonghs = tonghs - 1
            print("Danh sach hoc sinh")
            for i in range(tonghs):
                print(i + 1, name[i], toan[i], anh[i], van[i], dtb[i])
    elif choose < 0 or choose > 10:
        print("Xin moi nhap lai")