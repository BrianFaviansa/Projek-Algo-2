from tkinter import *
from tkinter import messagebox as mbox

neon = "#54d477"
green = "#dbe4c6"
darkgreen ="#94af9f"
white = "#ffffff"
black = "#000000"



import tkinter as tk
from tkinter import messagebox

def cariBulan(month, target_list):
    left = 0
    right = len(target_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if target_list[mid] == month:
            return True
        elif target_list[mid] < month:
            left = mid + 1
        else:
            right = mid - 1

    return False

def cekBulan():
    jenis_tanaman = jenis_tanaman_var.get()
    bulan = bulan_entry.get().capitalize()

    if jenis_tanaman == 1:
        target_list = ["Januari", "Februari", "Maret", "November", "Desember"]
        tanaman = "Padi"
    elif jenis_tanaman == 2:
        target_list = ["Mei", "Juni", "Juli"]
        tanaman = "Jagung"
    elif jenis_tanaman == 3:
        target_list = ["April", "Mei", "Juni", "Juli"]
        tanaman = "Kedelai"
    elif jenis_tanaman == 4:
        target_list = ["Desember", "Januari"]
        tanaman = "Tebu"
    elif jenis_tanaman == 5:
        target_list = ["Maret", "April", "Mei", "Juni"]
        tanaman = "Cabai"
    elif jenis_tanaman == 6:
        target_list = ["Maret", "April"]
        tanaman = "Tomat"
    else:
        messagebox.showinfo("Kesalahan", "Pilih jenis tanaman yang valid.")
        return

    if cariBulan(bulan, target_list):
        messagebox.showinfo("Rekomendasi", f"Cocok Menanam {tanaman}")
    else:
        messagebox.showinfo("Rekomendasi", f"Tidak Cocok Menanam {tanaman}")

window = tk.Tk()
window.title("Rekomendasi Penanaman")
window.geometry("1280x720")
window.resizable(False,False)

img = PhotoImage(file="png/bg pilihmenu.png")
Label(window,image=img).place(x=0,y=0)

header_label = tk.Label(window, text="Rekomendasi Penanaman", font=("Poppins", 24, "bold"))
header_label.pack(pady=20)

jenis_tanaman_var = tk.IntVar()
jenis_tanaman_label = tk.Label(window, text="Pilih jenis tanaman yang anda cari :", font=("Poppins", 16))
jenis_tanaman_label.pack()

jenis_tanaman_frame = tk.Frame(window)
jenis_tanaman_frame.pack(pady=10)

radio_button1 = tk.Radiobutton(jenis_tanaman_frame, text="Padi", variable=jenis_tanaman_var, value=1, font=("Poppins", 12))
radio_button1.pack(side="left", padx=10)
radio_button2 = tk.Radiobutton(jenis_tanaman_frame, text="Jagung", variable=jenis_tanaman_var, value=2, font=("Poppins", 12))
radio_button2.pack(side="left", padx=10)
radio_button3 = tk.Radiobutton(jenis_tanaman_frame, text="Kedelai", variable=jenis_tanaman_var, value=3, font=("Poppins", 12))
radio_button3.pack(side="left", padx=10)
radio_button4 = tk.Radiobutton(jenis_tanaman_frame, text="Tebu", variable=jenis_tanaman_var, value=4, font=("Poppins", 12))
radio_button4.pack(side="left", padx=10)
radio_button5 = tk.Radiobutton(jenis_tanaman_frame, text="Cabai", variable=jenis_tanaman_var, value=5, font=("Poppins", 12))
radio_button5.pack(side="left", padx=10)
radio_button6 = tk.Radiobutton(jenis_tanaman_frame, text="Tomat", variable=jenis_tanaman_var, value=6, font=("Poppins", 12))
radio_button6.pack(side="left", padx=10)

bulan_label = tk.Label(window, text="Masukkan bulan yang anda inginkan :", font=("Poppins", 14))
bulan_label.pack(pady=10)

bulan_entry = tk.Entry(window, font=("Poppins", 14))
bulan_entry.pack()

submit_button = tk.Button(window, text="Cek Bulan", command=cekBulan, font=("Poppins", 16), bg="white", fg="black")
submit_button.pack(pady=10)

window.mainloop()

