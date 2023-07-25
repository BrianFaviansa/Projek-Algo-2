from tkinter import *
from tkinter import messagebox 
import json
import os

jendela_login = Tk()
jendela_login.title('Login POTRAY')
jendela_login.geometry("1280x720")
jendela_login.configure(bg='white')
jendela_login.resizable(False, False)

#--------------------------------------------------------------------------

header = Label(jendela_login,text="POTRAY", fg='#54D477', bg='white', font=("Poppins", 30, "bold")).place(x=240, y=120)

img1 = PhotoImage(file='png\gambardepan.png')
Label(jendela_login,image=img1,bg='white',).place(x=170, y=220)

log_frame = Frame(jendela_login, width=450, height=450, bg='white')
log_frame.place(x=680, y=150)

header = Label(log_frame,text="Masuk", fg='#54D477', bg='white', font=("Poppins", 24))
header.place(x=180, y=0)

def hoverNama(e):
    usn.delete(0, "end")

def unhoverNama(e):
    fill = usn.get()
    if fill == "":
        usn.insert(0, "username")

def hoverPW(e):
    passw.delete(0, "end")

def unhoverPW(e):
    fill = passw.get()
    if fill == "":
        passw.insert(0, "password")

def signup():
    jendela_login.destroy()
    import signup_potray

usn = Entry(log_frame, width=25, fg='black', border=0, font=("Poppins", 12))
usn.place(x=60, y=100)
usn.insert(0, "username")
usn.bind("<FocusIn>", hoverNama)
usn.bind("<FocusOut>", unhoverNama)
Frame(log_frame, width=345, height=2, bg='black').place(x=60, y=130)

pasw = StringVar()
passw = Entry(log_frame, width=25, textvariable=pasw, fg='black', border=0, font=("Poppins", 12))
passw.place(x=60, y=180)
passw.insert(0, "password")
passw.bind("<FocusIn>", hoverPW)
passw.bind("<FocusOut>", unhoverPW)
Frame(log_frame, width=345, height=2, bg='black').place(x=60, y=210)

def validasi_json():
    username = usn.get()
    password = passw.get()
    kondisi = False
    with open('database\\users.json', "r") as data:
        reader = json.load(data)
    dict = {}  

    for i in reader:
        if username == i["nama"]:
            dict["nama"] = i["nama"]
            dict["pw"] = i["pw"]
            dict["isAdmin"] = i["isAdmin"]

    if not dict:
        messagebox.showerror('Error', 'Username tidak ditemukan')
        return kondisi
    else:
        if password != dict["pw"]:
            messagebox.showerror('Error', 'Password salah')
            return kondisi
        else:
            kondisi = True
            if username == 'admin':
                messagebox.showinfo('Info', 'Halo admin')
                jendela_login.destroy()
                import mainmenuAdmin
            else:
                messagebox.showinfo('Info', 'Login sukses')
                jendela_login.destroy()
                import pilih_menu

    return [kondisi, dict["isAdmin"]]
        

Button(log_frame, width=35, pady=2, text="Login", font=("Poppins", 12, "bold"), bg='#54D477', fg='white', command=validasi_json, border=0).place(x=46, y=285)
gadaAcc = Label(log_frame, text="tidak punya akun?", bg='white', font=("Poppins", 11)).place(x=120, y=340)

Button(log_frame, text="daftar", font=("Poppins", 11, "underline"), bg='white', command=signup, cursor="hand2", border=0).place(x=265, y=335)

jendela_login.mainloop()