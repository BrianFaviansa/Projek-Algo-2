from tkinter import *
from tkinter import messagebox as mbox

neon = "#54d477"
green = "#dbe4c6"
darkgreen ="#94af9f"
white = "#ffffff"
black = "#000000"

jendelaPupuk = Tk()
jendelaPupuk.title('Pemupukan')
jendelaPupuk.geometry("1280x720")
jendelaPupuk.config(bg=white)
jendelaPupuk.resizable(False, False)

img = PhotoImage(file="png/PemupukanBaik.png")
Label(jendelaPupuk,image=img).place(x=0,y=0)

jendelaPupuk.mainloop()
