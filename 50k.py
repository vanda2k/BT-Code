# Max - Tim max cua mot danh sach
"""n = int(input("Nhap vao so phan tu: "))
a = [0] * n
for i in range(n):
    a[i] = int(input(f"PT thu {i+1}: "))
print(a)
def Max(a):
    M = a[0]
    for i in range(len(a)):
        if a[i] > a[0]:
            M = a[i]
        else:
            M = a[i]
    return M
print(f"{Max(a)} la gia tri lon nhat")"""

# Prime - Tim so nguyen  to

"""n = -1
while n < 0:
    n = int(input("Nhap vao n: "))
def Prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(f"{n} la so nguyen to!")
    else:
        print(f"{n} khong la so nguyen to!")
Prime(n)"""

#Bubble Sort - Sap xep noi bot
"""n = int(input("Nhap vao so phan tu: "))
a = [0] * n
for i in range(n):
    a[i] = int(input(f"PT thu {i+1}: "))

def Bubble_sort(a):
    for i in range(n):
        for j in range(1, n - i):
            if a[j] < a[j - 1]:
                tg = a[j]
                a[j] = a[j - 1]
                a[j - 1] = tg
    return a
print("mang chua sap xep: ",a)
print("mang sau khi sap xep: ",Bubble_sort(a))"""

#Selection Sort -  Sap xep chon
"""n = int(input("Nhap vao so phan tu: "))
a = [0] * n
for i in range(n):
    a[i] = int(input(f"PT thu {i+1}: "))
def Selection_sort(a):
    for i in range(0,n-1):
        for j in range(i+1, n):
            if a[j] < a[i]:
                tg = a[j]
                a[j] = a[i]
                a[i] = tg
    return a
print("mang chua sap xep: ",a)
print("mang sau khi sap xep: ",Selection_sort(a))"""

#Direction Selection Sort - Sap xep chen truc tiep
"""n = int(input("Nhap vao so phan tu: "))
a = [0] * n
for i in range(n):
    a[i] = int(input(f"PT thu {i+1}: "))
def Dir_selection_sort(a):
    for i in range(0, n-1):
        k = i
        for j in range(i+1, n):
            if a[j] < a[k]:
                k = j
        if k != i:
            tg = a[k]
            a[k] = a[i]
            a[i] = tg
    return a
print("mang chua sap xep: ",a)
print("mang sau khi sap xep: ",Dir_selection_sort(a))"""

# Insertion Sort - Sap xep chonj truc tiep
"""n = int(input("Nhap vao so phan tu: "))
a = [0] * n
for i in range(n):
    a[i] = int(input(f"PT thu {i+1}: "))
def Insertion_sort(a):
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and x < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = x
    return a
print("mang chua sap xep: ",a)
print("mang sau khi sap xep: ",Insertion_sort(a))"""

# Binary Search - Tim kiem nhi phan

# def Binary_search(a, x):
#     start = 0
#     end = len(a) - 1
#     mid = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if a[mid] < x:
#             start = mid + 1
#         elif a[mid] > x:
#             end = mid - 1
#         else:
#             return mid
#     return -1
# a = [1, 2, 3, 40, 10, 7, 8, 9 ,12]
# x = int(input("Nhap vao so can tim: "))
#
# result = Binary_search(a, x)
# if result != -1:
#     print(f"{x} nam o vi tri {result} trong danh sach")
# else:
#     print(f"{x} khong co trong danh sach")
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

# from PIL import ImageTk,Image

win = Tk()
win.geometry('500x500')
win.title('TỶ GIÁ')

L1 = Label(win, text="TỶ GIÁ TIỀN", font=('Times New Roman', 15))
L1.place(x=50, y=50)

L2 = Label(win, text="NGOẠI TỆ ", font=('Times New Roman', 15))
L2.place(x=220, y=150)

listngoaite = [['KOREAN WON', 'KRW', 18127.19], ['YEN', 'JPY', 218.19], ['EURO', 'EUR', 28028.63],
               ['AUSTRALIAN DOLLAR', 'AUD', 18127.19], ['CANADIAN DOLLAR', 'CAD', 18742.18],
               ['US DOLLAR', 'USD', 23160.00], ['RUSSIAN RUBLE', 'RUB', 344.76], ['SINGAPORE DOLLAR', 'SGD', 17413.40],
               ['HONGKONG DOLLAR', 'HKD', 3017.38], ['INDIAN RUPEE', 'INR', 329.03],
               ['MALAYSIAN RINGGIT', 'MYR', 5658.53], ['VIETNAM', 'VN', 1]]

listtien = []
for i in listngoaite:
    listtien.append(i[0])

listma = []
for i in listngoaite:
    listma.append(i[1])


def sk1(event):
    for i in listngoaite:
        if c1.get() == i[0]:
            c2.set(i[1])
            break


def sk2(event):
    for i in listngoaite:
        if c3.get() == i[0]:
            c4.set(i[1])
            break


def ketqua():
    hesovao = 1
    hesora = 1
    if c1.get() == 'Tên ngoại tệ':
        return messagebox.showwarning('Notice', 'Please choose input currency')
    if c3.get() == 'Tên ngoại tệ':
        return messagebox.showwarning('Notice', 'Please choose ouput currency')
    try:
        if txt.get() == "":
            return messagebox.showwarning('Notice', 'Change value')
        for i in listngoaite:
            if c2.get() == i[1]:
                hesovao = i[2]
        for j in listngoaite:
            if c4.get() == j[1]:
                hesora = j[2]
        kq = float(txt.get()) * hesovao / hesora
        txt1.set(round(kq, 2))
    except:
        return messagebox.showerror('Notice', 'Value must be int')


# photo=ImageTk.PhotoImage(Image.open("currency-exchange.png"))

def reset():
    c1.set('Tên ngoại tệ')
    c3.set('Tên ngoại tệ')
    txt.set('')


# anh=Label(win,image=photo)
# anh.place(x=83,y=100)

a = Menu(win)

menucon = Menu(tearoff=0)
a.add_cascade(label='File', menu=menucon)
menucon.add_command(label='Clear', command=reset)
menucon.add_command(label='Quit', command=win.destroy)
win.config(menu=a)

c1 = Combobox(win)
c1['values'] = listtien
c1.place(x=100, y=200)
c1.set('Tên ngoại tệ')
c1.bind("<<ComboboxSelected>>", sk1)

c2 = Combobox(win, state='disable')
c2['values'] = listma
c2.place(x=300, y=200)
c2.set('Mã NT')

txt = StringVar()
E1 = Entry(win, show='', font=('Times New Roman', 10), textvariable=txt)
E1.place(x=200, y=250)

L3 = Label(win, text='ĐỔI NGOẠI TỆ ', font=('Times New Roman', 15))
L3.place(x=200, y=280)

c3 = Combobox(win)
c3['values'] = listtien
c3.place(x=100, y=330)
c3.set('Tên ngoại tệ')
c3.bind("<<ComboboxSelected>>", sk2)

c4 = Combobox(win, state='disable')
c4['values'] = listma
c4.place(x=300, y=330)
c4.set('Mã NT')

B1 = Button(win, text='Kết quả', width=20, command=ketqua)
B1.place(x=200, y=380)

txt1 = StringVar()
E2 = Entry(win, font=('Times New Roman', 10), textvariable=txt1, state='disable')
E2.place(x=280, y=420)

B3 = Button(win, text='XOA', width=20, command=reset)
B3.place(x=100, y=420)
win.mainloop()

