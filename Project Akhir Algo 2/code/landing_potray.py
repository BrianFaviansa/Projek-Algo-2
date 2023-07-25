from tkinter import *
from tkinter import messagebox as mbox

neon = "#54d477"
green = "#dbe4c6"
darkgreen ="#94af9f"
white = "#ffffff"
black = "#000000"

jendela_landing = Tk()
jendela_landing.title('Landing page')
jendela_landing.geometry('1280x720')
jendela_landing.config(bg=white)

bg = PhotoImage(file='png\\bg_landing.png')
Label(jendela_landing,image=bg).place(x=0, y=0)

def register():
    jendela_landing.destroy()
    import signup_potray

def login():
    jendela_landing.destroy()
    import login_potray

# button register dan login

imgreg = PhotoImage(file='png\\landing_register.png')
frame1 = Frame(jendela_landing, width=318, height=70)
frame1.place(x=554, y=604)
Button(frame1, width=318, height=70, bg=white, border=0, image=imgreg, command=register, cursor='hand2').place(x=0, y=0)

imglog = PhotoImage(file='png\\landing_login.png')
frame1 = Frame(jendela_landing, width=318, height=70)
frame1.place(x=904, y=604)
Button(frame1, width=318, height=70, bg=white, border=0, image=imglog, command=login, cursor='hand2').place(x=0, y=0)

jendela_landing.mainloop()
