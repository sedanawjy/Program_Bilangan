from tkinter import *
main_window=Tk()
main_window.title("I Putu Sedana Wijaya")

# label judul
Label(main_window, text="Halo!").grid(row=0,column=0,columnspan=3)
Label(main_window, text="Program ini bertujuan untuk").grid(row=1,column=0,columnspan=3)
Label(main_window, text="mengetahui nilai mean, median, dan perkalian").grid(row=2,column=0,columnspan=3)
Label(main_window, text="dari sekumpulan bilangan.").grid(row=3,column=0,columnspan=3)
Label(main_window, text=" ").grid(row=4,column=0,columnspan=3)

# output program
Label(main_window, text="Hasil").grid(row=12,column=0)
Label(main_window, text="Input Anda: ").grid(row=13,column=0)
e_input = Entry(main_window, width=35, borderwidth=5)
e_input.grid(row=13,column=1,columnspan=2)
Label(main_window, text="Urutkan Bilangan: ").grid(row=14,column=0)
e_urut = Entry(main_window, width=35, borderwidth=5)
e_urut.grid(row=14,column=1,columnspan=2)
Label(main_window, text="Rata-rata Bilangan: ").grid(row=15,column=0)
e_rata = Entry(main_window, width=35, borderwidth=5)
e_rata.grid(row=15,column=1,columnspan=2)
Label(main_window, text="Nilai Tengah: ").grid(row=16,column=0)
e_median = Entry(main_window, width=35, borderwidth=5)
e_median.grid(row=16, column=1, columnspan=2)
Label(main_window, text="Perkalian Bilangan: ").grid(row=17,column=0)
e_kali = Entry(main_window, width=35, borderwidth=5)
e_kali.grid(row=17, column=1, columnspan=2)
Label(main_window, text=" ").grid(row=18,column=0)

# input user
teks = Entry(main_window, width=35, borderwidth=5)
teks.grid(row=5, column=0, columnspan=3, padx=30)

stack=[]
# fun hasil
def submit():
    bilangan = teks.get()
    stack.append(int(bilangan))
    teks.delete(0, END)
    # input user
    e_input.delete(0, END)
    e_input.insert(0, str(stack))
    # sorted bilangan
    e_urut.delete(0, END)
    e_urut.insert(0, str(urut_bil()))
    # rata-rata bilangan
    e_rata.delete(0, END)
    e_rata.insert(0, str(rata_bil()))
    # nilai tengah
    e_median.delete(0, END)
    e_median.insert(0, str(median_bil()))
    # perkalian
    e_kali.delete(0, END)
    e_kali.insert(0, str(kali_bil()))

# fun layar
def layar(bil):
    bil_sekarang = teks.get()
    teks.delete(0, END)
    teks.insert(0, str(bil_sekarang)+str(bil))

# fun cls
def hapus_layar():
    teks.delete(0, END)

# fun sorted    
def urut_bil():
    stack.sort()
    return stack

# fun rata2
def rata_bil():
    return sum(stack)/len(stack)

# fun median
def median_bil():
    index_t=len(stack)//2
    if len(stack)%2==1:
        return stack[index_t]
    else:
        return (stack[index_t-1]+stack[index_t])/2

# fun perkalian
def kali_bil():
    kali=1
    for i in stack:
        kali*=i
    return kali

# button user
btn_1 = Button(main_window, text="1", padx=40, pady=20, command=lambda:layar(1)).grid(row=6 , column=0 )
btn_2 = Button(main_window, text="2", padx=40, pady=20, command=lambda:layar(2)).grid(row=6 , column=1 )
btn_3 = Button(main_window, text="3", padx=40, pady=20, command=lambda:layar(3)).grid(row=6 , column=2 )
btn_4 = Button(main_window, text="4", padx=40, pady=20, command=lambda:layar(4)).grid(row=7 , column=0 )
btn_5 = Button(main_window, text="5", padx=40, pady=20, command=lambda:layar(5)).grid(row=7 , column=1 )
btn_6 = Button(main_window, text="6", padx=40, pady=20, command=lambda:layar(6)).grid(row=7 , column=2 )
btn_7 = Button(main_window, text="7", padx=40, pady=20, command=lambda:layar(7)).grid(row=8 , column=0 )
btn_8 = Button(main_window, text="8", padx=40, pady=20, command=lambda:layar(8)).grid(row=8 , column=1 )
btn_9 = Button(main_window, text="9", padx=40, pady=20, command=lambda:layar(9)).grid(row=8 , column=2 )
btn_0 = Button(main_window, text="0", padx=40, pady=20, command=lambda:layar(0)).grid(row=9 , column=1)
btn_reset = Button(main_window, text="C", padx=40, pady=20, command=hapus_layar).grid(row=9 , column=2)

# button submit
btn_submit = Button(main_window, text="Submit", padx=150, pady=20, command=submit).grid(row=10,column=0, columnspan=3)
Label(main_window, text=" ").grid(row=11,column=0)

# load windows
main_window.mainloop()