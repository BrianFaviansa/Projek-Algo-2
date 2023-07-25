from tkinter import *
from tkinter import messagebox 
from csv import *
import csv
import json

neon = "#54d477"
green = "#dbe4c6"
darkgreen ="#94af9f"
white = "#ffffff"
black = "#000000"

jendela_signup = Tk()
jendela_signup.title("Sign up POTRAY")
jendela_signup.geometry("1280x720")
jendela_signup.configure(bg='white')
jendela_signup.resizable(False, False)

header = Label(jendela_signup,text="POTRAY", fg='#54D477', bg='white', font=("Poppins", 30, "bold")).place(x=240, y=120)

img1 = PhotoImage(file='png\\gambardepan.png')
Label(jendela_signup,image=img1,bg='white',).place(x=170, y=220)

jendela_daftar = Frame(jendela_signup, width=450, height=450, bg='white')
jendela_daftar.place(x=680, y=150)

header = Label(jendela_daftar,text="Daftar", fg='#54D477', bg='white', font=("Poppins", 24))
header.place(x=180, y=0)

def ndaftar():
    username = usn.get()
    password = passw.get()
    isAdmin = False
    try:
        with open('database\\users.json', "r") as ndaftar_file:
            userData = json.load(ndaftar_file)
    except FileNotFoundError:
        userData = []

    masukin = {}
    masukin['nama'] = username

    for i in userData:
        if masukin['nama'] == i['nama']:
            messagebox.showerror('Invalid', 'Username telah terdaftar')
            break
    else:
        masukin["pw"] = password
        masukin["isAdmin"] = isAdmin
        userData.append(masukin)
        isAdmin = False
        try:
            with open('database\\users.json', "w") as ndaftarin_file:
                json.dump(userData, ndaftarin_file, indent=4)
            messagebox.showinfo("Info", "Sign up success! Silahkan login")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mendaftarkan user: {str(e)}")
    jendela_signup.destroy()
    import login_potray

def hoverNama(e):
    usn.delete(0, "end")

def unhoverNama(e):
    fill = usn.get()
    if fill == "":
        usn.insert(0, "buat username")

def hoverPW(e):
    passw.delete(0, "end")

def unhoverPW(e):
    fill = passw.get()
    if fill == "":
        passw.insert(0, "password")

def login():
    jendela_signup.destroy()
    import login_potray

usn = Entry(jendela_daftar, width=25, fg='black', border=0, font=("Poppins", 12))
usn.place(x=60, y=100)
usn.insert(0, "buat username")
usn.bind("<FocusIn>", hoverNama)
usn.bind("<FocusOut>", unhoverNama)
Frame(jendela_daftar, width=345, height=2, bg='black').place(x=60, y=130)

pasw = StringVar()
passw = Entry(jendela_daftar, width=25, textvariable=pasw, fg='black', border=0, font=("Poppins", 12))
passw.place(x=60, y=180)
passw.insert(0, "buat password")
passw.bind("<FocusIn>", hoverPW)
passw.bind("<FocusOut>", unhoverPW)
Frame(jendela_daftar, width=345, height=2, bg='black').place(x=60, y=210)

Button(jendela_daftar, width=35, pady=2, text="Daftar", font=("Poppins", 12, "bold"), bg='#54D477', fg='white', command=ndaftar, border=0).place(x=60, y=285)
adaAcc = Label(jendela_daftar, text="Memiliki akun?", bg='white', font=("Poppins", 11)).place(x=150, y=340)

Button(jendela_daftar, text="Login", font=("Poppins", 11, "underline"), bg='white', command=login, cursor="hand2", border=0).place(x=265, y=335)

jendela_signup.mainloop()