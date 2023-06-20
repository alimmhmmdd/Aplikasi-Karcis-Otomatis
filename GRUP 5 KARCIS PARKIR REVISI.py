#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import ttk
from tkinter import *
import time
from time import strftime
import datetime
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
import datetime as dt
from barcode import EAN13
from barcode.writer import ImageWriter
import numpy as np


root=Tk()
root.geometry("500x500")
root.configure(bg="#fff")
root.resizable(False,False)

global data
data = {
    'plat': ['W 6296 UK', 'L 2334 PL', 'AG 2901 KK', 'W 7334 AA'],
    'jenis': ['motor', 'mobil', 'motor','mobil'],
    'tgl_masuk_detail':['Mon, Dec 24 2022', 'Tue, Nov 29 2022','Sun, Nov 27 2022', 'Mon, Dec 26 2022'],
    'tgl_masuk': ['2022-12-24', '2022-11-29', '2022-11-27', '2022-12-26'],
    'jam_masuk_detail': ['12:22:41','10:22:40', '23:57:41', '14:25:34'],
    'bln_masuk':['12', '11', '11', '12'],
    'hari_masuk':['24', '29', '27', '26'],
    'jam_masuk':['12', '10', '23', '14'],
    'jam_keluar_detail':[],
    'tarif':['3000.0', '10000.0']
}
def masuk():
    screen = Toplevel(root)
    screen.title("Parkir Masuk")
    screen.geometry("925x500+300+200")
    screen.config(bg="#fff")
    screen.resizable(False,False)

    username=user.get()

    title=Label(screen,text = "Selamat Datang, "+username, font = ("Times", 27, "bold"),bg="white")
    title.pack(pady = 50)
    
    frame1=Frame(screen,width=500,height=300,bg="white")
    frame1.place(x=210,y=140)

    def open():
        label1=Label(screen,text=clicked.get(),font=('Times', "12","bold"),bg="white")
        label1.place(x=345,y=245)

    options=["Motor","Mobil"]
        
    clicked=StringVar()
    clicked.set(options[0])

    pilih_kendaraan=Label(screen,text="Kendaraan : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=245)
    plat_nomor=Label(screen,text="Plat Nomor : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=280)
    tanggal= Label(screen,text="Tanggal : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=315)
    jam_masuk=Label(screen,text="Jam Masuk : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=350)

    drop=OptionMenu(screen,clicked,*options)
    drop.place(x=243,y=205)
    bttn=Button(screen, text="Ok",command=open)
    bttn.place(x=340,y=205)

    def plat_no(event):
        e5.config(state=NORMAL)
        e5.delete(0,END)
            
    e5=Entry(screen,font=("Times",'12',"bold"))
    e5.insert(0," ")
    e5.config(state=DISABLED)
    e5.bind("<Button-1>",plat_no)
    e5.place(x=345,y=280)
    
    date = dt.datetime.now()
    format_date = f"{date:%a, %b %d %Y}"
    e6 = Entry(screen, font=("Times", 12))
    e6.insert(END, format_date)
    e6.place(x=345, y=315)
        
    format_date = f"{date:%X}"
    e8 = Entry(screen, font=("Times", 12))
    e8.insert(END, format_date)
    e8.place(x=345, y=350)

    def cetak_msk():
        global countMasuk, data
        msk=Toplevel(screen)
        msk.geometry("450x400")
        msk.config(bg='white')
        msk.resizable(False,False)
            
        jenis=clicked.get()
        platt=e5.get()
        jam_msk=e8.get()
        tgl=e6.get()

        Label(msk,text="TIKET PARKIR",font = ("Times",15, "bold"),fg="black",bg='white').place(x=165,y=30)
        Label(msk,text="Mall of Unesa",font = ("Times",12),fg="black",bg='white').place(x=20,y=90)
        Label(msk,text="Nomor Tiket : 152",font = ("Times",12),fg="black",bg='white').place(x=20,y=110)
        Label(msk,text="Tanggal : "+tgl,font = ("Times",12),fg="black",bg='white').place(x=20,y=130)
        Label(msk,text="Jam Masuk : "+jam_msk,font = ("Times",12),fg="black",bg='white').place(x=20,y=150)
        Label(msk,text="Jenis Kendaraan : "+jenis,font = ("Times",12),fg="black",bg='white').place(x=20,y=170)
        Label(msk,text="JANGAN MENINGGALKAN TIKET & \n BARANG BERHARGA DI DALAM \n KENDARAAN ANDA",font = ("Times",15),fg="black",bg='white').place(x=60,y=290)
        randomBarcode()

        name_barcode = f'barcode{countMasuk}.png'
        img = Image.open(name_barcode)
        img.resize((87, 42))
        img = ImageTk.PhotoImage(img)
        l1=Label(msk, image=img, height=50)
        l1.place(x=-35,y=220)
        countMasuk+=1

        tanggal= strftime("%Y-%m-%d")

        # Memasukkan data
        data['plat'].append(platt.upper())
        data['jenis'].append(jenis.lower())
        data['tgl_masuk'].append(tanggal)
        print(data['tgl_masuk'])
        data['tgl_masuk_detail'].append(tgl)
        data['bln_masuk'].append(strftime("%m"))
        data['hari_masuk'].append(strftime("%d"))
        data['jam_masuk_detail'].append(jam_msk)
        data['jam_masuk'].append(strftime("%H"))


        msk.mainloop()
                
    Button(screen,width=9,pady=5,text='Cetak',font=('Times','12'),command=cetak_msk).place(x=240,y=390)
    Button(screen,width=9,pady=5,text='Batal',font=('Times','12'),command=login).place(x=400,y=390)

    screen.mainloop()

def keluar():
    global data, klr
    klr=Toplevel(root)
    klr.title("Parkir Keluar")
    klr.geometry("925x600+300+200")
    klr.config(bg="white")
    klr.resizable(False,False)

    username=user.get()

    title = Label(klr,text = "Selamat Jalan, "+username, font = ("Times", 27, "bold"),bg="white")
    title.pack(pady = 50)

    frame2=Frame(klr,width=500,height=300,bg="white")
    frame2.place(x=210,y=140)
    

    def open():
        label1=Label(klr,text=clicked.get(),font=('Times', "12","bold"),bg="white")
        label1.place(x=345,y=245)
    
    options=["Motor","Mobil"]
    
    clicked=StringVar()
    clicked.set(options[0])

    pilih_kendaraan=Label(klr,text = "Pilih kendaraan", font = ("Times", 12, "bold"),bg="white").place(x=240,y=170)
    kendaraan=Label(klr,text ="Kendaraan : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=245)
    plat_nomor=Label(klr,text="Plat Nomor : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=280)
    tanggal= Label(klr,text="Tanggal : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=315)
    jam_keluar=Label(klr,text="Jam Keluar : ", font = ("Times", 12, "bold"),bg="white").place(x=240,y=350)


    drop=OptionMenu(klr,clicked,*options)
    drop.place(x=243,y=205)
    bttn=Button(klr, text="Ok",command=open)
    bttn.place(x=340,y=205)

    def plat_no(event):
        e4.config(state=NORMAL)
        e4.delete(0,END)     
        
    e4=Entry(klr,font=("Times",'12',"bold"))
    e4.insert(0," ")
    e4.config(state=DISABLED)
    e4.bind("<Button-1>",plat_no)
    e4.place(x=345,y=280)
    
    date = dt.datetime.now()
    format_date = f"{date:%a, %b %d %Y}"
    e7 = Entry(klr, font=("Times", 12))
    e7.insert(END, format_date)
    e7.place(x=345, y=315)
    
    format_date = "00:00:00"
    e9 = Entry(klr, font=("Times", 12))
    e9.insert(END, format_date)
    # e9['text']=format_date
    e9.place(x=345, y=350)
    
    e11=ttk.Combobox(klr,font=("Times",12,"bold"))
    e11['values'] = data['plat']
    e11.place(x=345,y=280)
    
    def cetak_keluar():
        global platt, waktu_tarif
        ctk_keluar=Toplevel(root)
        ctk_keluar.title("Resi Parkir")
        ctk_keluar.geometry("450x520")
        ctk_keluar.config(bg='white')
        ctk_keluar.resizable(False,False)

        username=user.get()
        plat=e11.get()
        tgl=e7.get()
        jam_klr=e9.get()
        # jam_klr=e9['text']
        jenis=clicked.get()

        index_plat= e11.get()
        index_plat=data['plat'].index(index_plat)
        jam_klr=str(jam_klr)
        def lama_parkir():
            date = dt.datetime.now()
            fmat="%Y-%m-%d %H:%M:%S"
            tgl_now = date.strftime('%Y-%m-%d')
            tanggal_msk = f"2022-12-27 {data['jam_masuk_detail'][index_plat]}"
            tanggal_klr = f"{tgl_now} {jam_klr}"
            hasil = dt.datetime.strptime(tanggal_klr, fmat) -dt.datetime.strptime(tanggal_msk, fmat)

            str_hasil=str(hasil)
            len_hasil = len(str_hasil)
            if len_hasil > 8:
                hari, days, jamDetail = str_hasil.split(" ")
                jam, menit, detik = jamDetail.split(":")
                hasil = f'{jam} Jam {menit} Menit'
            else:
                jam, menit, detik = str_hasil.split(":")
                hasil = f'{jam} Jam {menit} Menit'
            return hasil
        lama = lama_parkir()
        
        jmk, mmk, dtkk= jam_klr.split(":")
        hari, bulan, tgl_, tahun=tgl.split(" ")
        tarif = tarifHarga(data['bln_masuk'][index_plat], strftime("%m"), data['hari_masuk'][index_plat], tgl_, data['jam_masuk'][index_plat], jmk, jenis.lower())
        # print(data['bln_masuk'][index_plat], strftime("%m"), data['hari_masuk'][index_plat], strftime("%d"), data['jam_masuk'][index_plat], strftime("%H"), jenis.lower())
        Label(ctk_keluar,text="MATH UNESA PARKSYS",font = ("Times",15, "bold"),fg="black",bg='white').place(x=120,y=50)
        Label(ctk_keluar,text="Tanggal : "+tgl,font = ("Times",12),fg="black",bg='white').place(x=20,y=120)
        Label(ctk_keluar,text="Plat Nomor : "+plat ,font = ("Times",12),fg="black",bg='white').place(x=20,y=140)
        Label(ctk_keluar,text="Nomor Tiket : 152",font = ("Times",12),fg="black",bg='white').place(x=20,y=160)
        Label(ctk_keluar,text="Tanggal Masuk : "+data['tgl_masuk_detail'][index_plat],font = ("Times",12),fg="black",bg='white').place(x=20,y=180)
        Label(ctk_keluar,text="Jam Masuk : "+data['jam_masuk_detail'][index_plat],font = ("Times",12),fg="black",bg='white').place(x=20,y=200)
        Label(ctk_keluar,text="Jam Keluar : "+jam_klr,font = ("Times",12),fg="black",bg='white').place(x=20,y=220)
        Label(ctk_keluar,text="Durasi Parkir : "+lama,font = ("Times",12),fg="black",bg='white').place(x=20,y=240)
        Label(ctk_keluar,text="Petugas : "+username,font = ("Times",12),fg="black",bg='white').place(x=20,y=260)
        Label(ctk_keluar,text="Tarif : "+tarif,font = ("Times",12),fg="black",bg='white').place(x=20,y=280)
        Label(ctk_keluar,text="TERIMA KASIH DAN \n SELAMAT JALAN",font = ("Times",15,),fg="black",bg='white').place(x=135,y=430)

        name_barcode = f"barcode{index_plat}.png"
        img = Image.open(name_barcode)
        img.resize((87, 42))
        img = ImageTk.PhotoImage(img)
        Label(ctk_keluar, image=img, height=50).place(x=-35,y=330)

        ctk_keluar.mainloop()
    
    Button(klr,width=9,pady=5,text='Cetak',font=('Times','12'),command=cetak_keluar).place(x=240,y=400)
    Button(klr,width=9,pady=5,text='Batal',font=('Times','12'),command=login).place(x=400,y=400)

    klr.mainloop()

def login():
    username=user.get()
    password=code.get()

    if password=="123":
        screen=Toplevel(root)
        screen.title("Parkir UNESA")
        screen.geometry("500x500")
        screen.config(bg="white")
        
        Label(screen,text='MATH UNESA PARKYS',bg="white",font=('Times','18', 'bold')).place(x=120,y=80) 
        Button(screen,width=25,pady=12,text='Parkir Masuk',font=('Times','14', 'bold'),command=masuk).place(x=100,y=180)    
        Button(screen,width=25,pady=12,text='Parkir Keluar',font=('Times','14', 'bold'),command=keluar).place(x=100,y=300) 
        
        screen.mainloop()
    else:
        messagebox.showerror("Invalid","Invalid Password!!!")

# Method Barcode
global countMasuk
countMasuk=4
def randomBarcode():
    global countMasuk
    hasil=""
    num = np.random.randint(0,9,12)
    for i in range(len(num)):
        hasil+=str(num[i])
    
    bar_code = EAN13(hasil, writer=ImageWriter())
    bar_code.save(f'barcode{countMasuk}')

# Method Tarif
def tarifHarga(bulanAwal, bulanAkhir, hariAwal, hariAkhir, jamAwal, jamAkhir, model):
    bulanAwal=int(bulanAwal)
    bulanAkhir=int(bulanAkhir)
    hariAkhir=int(hariAkhir)
    hariAwal=int(hariAwal)
    jamAkhir=int(jamAkhir)
    jamAwal=int(jamAwal)
    bulan_list =[
        ['01', '31'], ['02', '28'], ['03', '31'], ['04', '30'],
        ['05', '31'], ['06', '30'], ['07', '31'], ['08', '31'],
        ['09', '30'], ['10', '31'], ['11', '30'], ['12', '31']
        ]
    if model == "motor":
        tarif=float(data['tarif'][0])
        if bulanAwal == bulanAkhir:
            if hariAwal == hariAkhir:
                if jamAwal == jamAkhir:
                    tarif=tarif
                else:
                    hasil_jam=jamAkhir-jamAwal
                    tarif=hasil_jam*tarif
            else:
                hasil_hari= hariAkhir - hariAwal
                hasil_hari = 24*hasil_hari
                if jamAwal == jamAkhir:
                    tarif=hasil_hari*tarif
                else:
                    if jamAkhir < jamAwal:
                        jamAwal = 24-jamAwal
                        hasil_jam=jamAwal+jamAkhir
                        tarif=(hasil_hari + hasil_jam)*tarif
                    else:
                        hasil_jam=jamAkhir-jamAwal
                        tarif=(hasil_hari + hasil_jam)*tarif
        else:
            # Mencari jumlah tanggal pada bulan menghasilkan banyak hari
            bulanAwal= int(tanggalBulan(str(bulanAwal), bulan_list))
            bulanAkhir= int(tanggalBulan(str(bulanAkhir), bulan_list))
            hasil_bulan = bulanAkhir - bulanAwal # mengahsilkan hitungan hari
            if hariAwal == hariAkhir:
                if jamAwal == jamAkhir:
                    hasil_bulan = hasil_bulan * 24
                    tarif=hasil_bulan*tarif
                else:
                    if jamAkhir < jamAwal:
                        jamAwal = 24-jamAwal
                        hasil_jam=jamAwal+jamAkhir
                        tarif=(hasil_hari + hasil_jam)*tarif
                    else:
                        hasil_jam=jamAkhir-jamAwal
                        tarif=(hasil_hari + hasil_jam)*tarif
            else:
                hariAwal=bulanAwal-hariAwal
                hasil_hari=(hariAwal+hariAkhir)*24
                if jamAwal == jamAkhir:
                    tarif=hasil_hari*tarif
                else:
                    if jamAkhir < jamAwal:
                        jamAwal = 24-jamAwal
                        hasil_jam=jamAwal+jamAkhir
                        tarif=(hasil_hari + hasil_jam)*tarif
                    else:
                        hasil_jam=jamAkhir-jamAwal
                        tarif=(hasil_hari + hasil_jam)*tarif
    elif model== "mobil":
        tarif=float(data['tarif'][1])
        if bulanAwal == bulanAkhir:
            if hariAwal == hariAkhir:
                if jamAwal == jamAkhir:
                    tarif=tarif
                else:
                    hasil_jam=jamAkhir-jamAwal
                    tarif=hasil_jam*tarif
            else:
                hasil_hari= hariAkhir - hariAwal
                hasil_hari = 24*hasil_hari
                if jamAwal == jamAkhir:
                    tarif=hasil_hari*tarif
                else:
                    if jamAkhir < jamAwal:
                        jamAwal = 24-jamAwal
                        hasil_jam=jamAwal+jamAkhir
                        tarif=(hasil_hari + hasil_jam)*tarif
                    else:
                        hasil_jam=jamAkhir-jamAwal
                        tarif=(hasil_hari + hasil_jam)*tarif
        else:
            # Mencari jumlah tanggal pada bulan menghasilkan banyak hari
            bulanAwal= int(tanggalBulan(str(bulanAwal), bulan_list))
            bulanAkhir= int(tanggalBulan(str(bulanAkhir), bulan_list))
            hasil_bulan = bulanAkhir - bulanAwal # mengahsilkan hitungan hari
            hasil_bulan = hasil_bulan * 24
            if hariAwal == hariAkhir:
                if jamAwal == jamAkhir:
                    tarif=hasil_bulan*tarif
                else:
                    if jamAkhir < jamAwal:
                        jamAwal = 24-jamAwal
                        hasil_jam=jamAwal+jamAkhir
                        tarif=(hasil_hari + hasil_jam)*tarif
                    else:
                        hasil_jam=jamAkhir-jamAwal
                        tarif=(hasil_hari + hasil_jam)*tarif
            else:
                hariAwal=bulanAwal-hariAwal
                hasil_hari=(hariAwal+hariAkhir)*24
                if jamAwal == jamAkhir:
                    tarif=hasil_hari*tarif
                else:
                    if jamAkhir < jamAwal:
                        jamAwal = 24-jamAwal
                        hasil_jam=jamAwal+jamAkhir
                        tarif=(hasil_hari + hasil_jam)*tarif
                    else:
                        hasil_jam=jamAkhir-jamAwal
                        tarif=(hasil_hari + hasil_jam)*tarif
    return format_rupiah(tarif)

# Method Format Penulisan Rupiah
def format_rupiah(value):
    str_value = str(value)
    separate_decimal=str_value.split(".")
    after_decimal= separate_decimal[0]
    before_decimal = separate_decimal[1]
    
    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value += val + "."
        else:
            temp_reverse_value += val
    
    temp_result= temp_reverse_value[::-1]
    return "Rp " + temp_result + "," + before_decimal

def find_all(matrix, element):
    yield from ((row_no, col_no)
        for row_no, row in enumerate(matrix)
        for col_no, matrix_element in enumerate(row)
        if matrix_element == element)

def tanggalBulan(index, list):
    for x, y in find_all(list, index):
        return list[x][1]
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=90,y=70)

heading=Label(frame,text='MATH UNESA PARKYS',bg='white',font=('Times','18', 'bold'))
heading.place(x=35,y=5)

def enter(e):
    user.delete(0,'end')

def leave(e):
    name=user.get()
    if name=="":
        user.insert(0,'Username')
        
user= Entry(frame,width=25,fg='black',border=0,bg="white",font=('Times','12'))
user.place(x=55,y=90)
user.insert(0,'Username')
user.bind('<FocusIn>',enter)
user.bind('<FocusOut>', leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=120)

def enter(e):
    code.delete(0,'end')

def leave(e):
    name=code.get()
    if name=="":
        code.insert(0,'Password')

code= Entry(frame,width=25,fg='black',border=0,bg="white",font=('Times', "12"))
code.place(x=55,y=170)
code.insert(0,'Password')
code.bind('<FocusIn>', enter)
code.bind('<FocusOut>', leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=200)

Button(frame,width=15,pady=7,text='Login',command=login).place(x=35,y=245)
Button(frame,width=15,pady=7,text='Cancel',command=root.destroy).place(x=200,y=245)

root.mainloop()


# In[ ]:




