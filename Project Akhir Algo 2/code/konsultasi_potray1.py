from tkinter import *
from tkinter import messagebox as mbox

neon = "#54d477"
green = "#dbe4c6"
darkgreen ="#94af9f"
white = "#ffffff"
black = "#000000"

jendela_konsul1 = Tk()
jendela_konsul1.title('Menu Konsultasi')
jendela_konsul1.geometry("1280x720")
jendela_konsul1.config(bg=white)
jendela_konsul1.resizable(False, False)

def pupuki():
    jendela_konsul1.destroy()
    import pupukBaik

def rekomeni():
    jendela_konsul1.destroy()
    import rekomen_potray
img = PhotoImage(file="png/bg_pilihKonsul.png")
Label(jendela_konsul1,image=img).place(x=0,y=0)

pupuk = PhotoImage(file='png\\tombolPupuk.png')
frame1 = Frame(jendela_konsul1, width=420, height=420, bg=white)
frame1.place(x=180, y=170)
Button(frame1, width=420, height=420, bg=white, border=0, image=pupuk, command=pupuki, cursor='hand2').place(x=0, y=0)

rekomen = PhotoImage(file='png\\tombolRekomen.png')
frame1 = Frame(jendela_konsul1, width=420, height=420, bg=white)
frame1.place(x=680, y=170)
Button(frame1, width=420, height=420, bg=white, border=0, image=rekomen, command=rekomeni, cursor='hand2').place(x=0, y=0)

jendela_konsul1.mainloop()