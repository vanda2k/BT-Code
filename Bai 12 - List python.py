# List trong python
l = [1, 2, 3, 4, 5, 6]
name = ["Ngoc","Anh","Duc","Triet","Phuong"]
list1 = ["Anh Ngoc", 10, 8.4]
print(name)
"""
#Truy cap den phan tu trong list - tends[chi so cua pt]
print("Ten toi la: ",list1[0])
print("Tuoi: ",list1[1])
print("Diem TB: ",list1[2])
print(name[0])
print(name[-2])
# Truy cập phần tử trong danh sách sử dụng lát cắt - tends[start : end-1]
name1 = name[0:4]
print(name1)
# Cap nhat danh sach theo chi so
name[1] = "Hong"
print(name)
"""
# Cap nhat theo lat cat - tends[start:end-1]
name[0:2] = ["Nga","Ngan"]
print(name)
# Truy cap toi tung phan tu trong mot danh sach
for i in name:
    print(i)
# Thêm một phần tử vào cuối danh sách - append(new_element)
name.append("Van")
print(name)
# Them một phần tử vào vị trí bất kì trong danh sách - insert(vị trí, new_element)
name.insert(1,"Hung")
print(name)
# Xoa phan tu theo chi so trong danh sach del tends[vi tri can xoa]
del name[0]
print(name)
# Xoá trực tiếp phần tử
name.remove("Van")
print(name)
# Dem tong so phan tu co trong danh sach
print(len(name))
print("Gia tri max = ",max(l))
print("Gia tri max = ",min(l))
tup = ("Van", 10, 2.4)
print(list(tup))
# Các phép toán với danh sách +, *
l1 = [2,3,4,5]
l2 = [3,4,5,"Van"]
print(l1+l2)
print(l1*2)
# Bài 1: Viết chương trình tính tổng các phần tử trong một danh sách sau: L = [1,2,3,4,5,6,7,8]
List = [1,2,3,4,5,6,7,8]
tong = 0
for i in List:
    tong += i
print("Tong cua danh sach la: ",tong)
# Bai 2: Viết chương trình python tính tích của các phần tử trong một list sau: _list= [1,2,4,5,6,7,8,9]
_list= [1,2,3,4,5,6,7,8,9]
tich = 1
for k in _list:
    tich *= k
print(tich)

# Tao danh sach nhap vao tu ban phim
num = input("Nhap vao cac phan tu (cach nhau boi dau phay): ")
List1 = num.split(" ")
print(List1)