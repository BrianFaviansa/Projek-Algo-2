from tkinter import *
from tkinter import messagebox as mbox

neon = "#54d477"
green = "#dbe4c6"
darkgreen ="#94af9f"
white = "#ffffff"
black = "#000000"

jendela_pilihMenu = Tk()
jendela_pilihMenu.title('Pilh menu')
jendela_pilihMenu.geometry("1280x720")
jendela_pilihMenu.config(bg=white)
jendela_pilihMenu.resizable(False, False)

def lahansaya():
    jendela_pilihMenu.destroy()
    import lahan_backend

def jualtruk():
    jendela_pilihMenu.destroy()
    import knapsack_potray

def rutedekat():
    jendela_pilihMenu.destroy()
    import shortest_tes

def landing():
    jendela_pilihMenu.destroy()
    import landing_potray

def konsultasii():
    jendela_pilihMenu.destroy()
    import konsultasi_potray

def logoutt():
    jendela_pilihMenu.destroy()
    import login_potray2

def akhir():
    jendela_pilihMenu.destroy()

img = PhotoImage(file="png/bg pilihmenu.png")
Label(jendela_pilihMenu,image=img).place(x=0,y=0)

# button pilih menu

lahan = PhotoImage(file='png\\pilih_lahansaya.png')
frame1 = Frame(jendela_pilihMenu, width=176.89, height=166.1, bg=white)
frame1.place(x=318, y=201)
Button(frame1, width=176.89, height=176.89, bg=white, border=0, image=lahan, command=lahansaya, cursor='hand2').place(x=0, y=0)

jual = PhotoImage(file='png\\pilih_jual.png')
frame2 = Frame(jendela_pilihMenu, width=176.89, height=166.1, bg=white)
frame2.place(x=552, y=201)
Button(frame2, width=176.89, height=166.1, bg=white, border=0, image=jual, command=jualtruk, cursor='hand2').place(x=0, y=0)

rute = PhotoImage(file='png\\pilih_pasar.png')
frame3 = Frame(jendela_pilihMenu, width=176.89, height=166.1, bg=white)
frame3.place(x=786, y=201)
Button(frame3, width=176.89, height=166.1, bg=white, border=0, image=rute, command=rutedekat, cursor='hand2').place(x=0, y=0)

konsultasi = PhotoImage(file='png\\pilih_konsultasi.png')
frame3 = Frame(jendela_pilihMenu, width=176.89, height=166.1, bg=white)
frame3.place(x=318, y=401)
Button(frame3, width=176.89, height=166.1, bg=white, border=0, image=konsultasi, command=konsultasii, cursor='hand2').place(x=0, y=0)

logout = PhotoImage(file='png\\pilih_logout.png')
frame3 = Frame(jendela_pilihMenu, width=176.89, height=166.1, bg=white)
frame3.place(x=544, y=401)
Button(frame3, width=176.89, height=166.1, bg=white, border=0, image=logout, command=logoutt, cursor='hand2').place(x=0, y=0)

pilihakhir = PhotoImage(file='png\\pilih_akhiri.png')
frame3 = Frame(jendela_pilihMenu, width=176.89, height=166.1, bg=white)
frame3.place(x=785, y=401)
Button(frame3, width=176.89, height=166.1, bg=white, border=0, image=pilihakhir, command=akhir, cursor='hand2').place(x=0, y=0)

jendela_pilihMenu.mainloop()

