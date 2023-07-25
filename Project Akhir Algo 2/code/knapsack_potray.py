import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

array = []
knapsack = []
harga_masuk = 0
berat_masuk = 0
kapasitas = 0

# Fungsi untuk menampilkan hasil knapsack pada GUI
def show_knapsack_result():
    for row in result_tree.get_children():
        result_tree.delete(row)
    
    for i, item in enumerate(knapsack):
        result_tree.insert(parent='', index='end', iid=i, values=(
            i+1, item['nama barang'], item['berat'], item['harga'], item['value']
        ))

    berat_masuk_label.config(text="Berat barang yang masuk : {:.2f} kg".format(berat_masuk))
    sisa_kapasitas_label.config(text="Sisa kapasitas knapsack : {:.2f} kg".format(kapasitas))
    total_harga_label.config(text="Total harga : Rp{:.2f}".format(harga_masuk))

# Fungsi untuk menambahkan data barang ke knapsack
def add_item():
    nama = ngangkut_entry.get()
    berat = float(berat_entry.get())
    harga = float(harga_entry.get())
    harga_awal = harga * berat
    value = harga_awal / berat

    array.append({
        'nama barang': nama,
        'berat': berat,
        'harga': harga_awal,
        'value': value
    })

    show_knapsack_result()

    berat_entry.delete(0, tk.END)
    harga_entry.delete(0, tk.END)

# Fungsi untuk membersihkan knapsack dan menghapus semua data barang
def clear_knapsack():
    array.clear()
    knapsack.clear()
    show_knapsack_result()

# Fungsi untuk menghitung knapsack
def calculate_knapsack():
    global kapasitas, harga_masuk, berat_masuk
    knapsack.clear()
    harga_masuk = 0
    berat_masuk = 0
    kapasitas = float(kapasitas_entry.get())

    array.sort(key=lambda x: x['value'], reverse=True)

    for i in array:
        if kapasitas >= i['berat']:
            if i['value'] > 0:
                kapasitas -= i['berat']
                harga_masuk += i['harga']
                berat_masuk += i['berat']
                knapsack.append(i)
        elif kapasitas < i['berat']:
            i['berat'] = kapasitas
            i['harga'] = i['berat'] * i['value']
            kapasitas = 0
            harga_masuk += i['harga']
            berat_masuk += i['berat']
            knapsack.append(i)
            if kapasitas == 0:
                break

    show_knapsack_result()

# Fungsi untuk menampilkan pesan konfirmasi sebelum keluar dari program
def exit_program():
    result = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar dari program?")
    if result:
        window.destroy()

# Membuat window utama
window = tk.Tk()
window.title("Menu Knapsack")
window.geometry("1280x720")

# Membuat frame untuk input data barang
input_frame = tk.Frame(window)
input_frame.pack(pady=20)

ngangkut_label = tk.Label(input_frame, text="Nama Barang:")
ngangkut_label.grid(row=0, column=0, padx=10, pady=5)
ngangkut_entry = tk.Entry(input_frame)
ngangkut_entry.grid(row=0, column=1, padx=10, pady=5)

berat_label = tk.Label(input_frame, text="Berat (kg):")
berat_label.grid(row=1, column=0, padx=10, pady=5)
berat_entry = tk.Entry(input_frame)
berat_entry.grid(row=1, column=1, padx=10, pady=5)

harga_label = tk.Label(input_frame, text="Harga (Rp):")
harga_label.grid(row=2, column=0, padx=10, pady=5)
harga_entry = tk.Entry(input_frame)
harga_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(input_frame, text="Tambah Barang", command=add_item)
add_button.grid(row=0, column=2, padx=10, pady=5)

# Membuat frame untuk hasil knapsack
result_frame = tk.Frame(window)
result_frame.pack(pady=20)

result_tree = ttk.Treeview(result_frame, columns=('No.', 'Nama Barang', 'Berat Barang (Kg)', 'Harga Barang (Rp)', 'Value'))
result_tree.heading('#0', text='', anchor='center')
result_tree.heading('#1', text='No.')
result_tree.heading('#2', text='Nama Barang')
result_tree.heading('#3', text='Berat Barang (Kg)')
result_tree.heading('#4', text='Harga Barang (Rp)')
result_tree.heading('#5', text='Value')
result_tree.column('#0', width=0, stretch='no')
result_tree.column('#1', width=50, anchor='center')
result_tree.column('#2', width=150)
result_tree.column('#3', width=150, anchor='center')
result_tree.column('#4', width=150, anchor='center')
result_tree.column('#5', width=100, anchor='center')
result_tree.pack()

# Membuat frame untuk informasi knapsack
info_frame = tk.Frame(window)
info_frame.pack()

berat_masuk_label = tk.Label(info_frame, text="Berat barang yang masuk : ")
berat_masuk_label.pack(anchor='w')

sisa_kapasitas_label = tk.Label(info_frame, text="Sisa kapasitas knapsack : ")
sisa_kapasitas_label.pack(anchor='w')

total_harga_label = tk.Label(info_frame, text="Total harga : ")
total_harga_label.pack(anchor='w')

# Membuat frame untuk tombol-tombol
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

calculate_button = tk.Button(button_frame, text="Hitung Knapsack", command=calculate_knapsack)
calculate_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Hapus Semua Barang", command=clear_knapsack)
clear_button.grid(row=0, column=1, padx=5)

# Membuat frame untuk kapasitas knapsack
kapasitas_frame = tk.Frame(window)
kapasitas_frame.pack(pady=20)

kapasitas_label = tk.Label(kapasitas_frame, text="Kapasitas Truk (kg):")
kapasitas_label.pack()

kapasitas_entry = tk.Entry(kapasitas_frame)
kapasitas_entry.pack()

# Tombol untuk keluar dari program
exit_button = tk.Button(window, text="Keluar", command=exit_program)
exit_button.pack(pady=20)

# Menjalankan main loop
window.mainloop()
