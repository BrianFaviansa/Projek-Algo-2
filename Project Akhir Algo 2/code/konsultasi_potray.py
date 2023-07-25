from tkinter import *
from tkinter import messagebox as mbox

neon = "#54d477"
green = "#dbe4c6"
darkgreen ="#94af9f"
white = "#ffffff"
black = "#000000"

jendela_konsultasi = Tk()
jendela_konsultasi.title('Menu Konsultasi')
jendela_konsultasi.geometry("1280x720")
jendela_konsultasi.config(bg=white)
jendela_konsultasi.resizable(False, False)

def mulaii():
    jendela_konsultasi.destroy()
    import konsultasi_potray1

img = PhotoImage(file="png/konsultasi_1.png")
Label(jendela_konsultasi,image=img).place(x=0,y=0)

mulai = PhotoImage(file='png\\konsul_tombolMulai.png')
frame1 = Frame(jendela_konsultasi, width=216, height=43, bg=white)
frame1.place(x=749, y=478)
Button(frame1, width=216, height=43, bg=white, border=0, image=mulai, command=mulaii, cursor='hand2').place(x=0, y=0)

jendela_konsultasi.mainloop()