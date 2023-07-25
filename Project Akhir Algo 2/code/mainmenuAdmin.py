import os
import pandas as pd
import json

def mainmenuAdmin() :
    os.system("cls")
    print("="*80)
    print("Selamat datang di Menu Admin program Potray".center(80))
    print("="*80)
    milihmenuAdmin = int(input("Silahkan pilih nomer fitur yang anda inginkan\n[1] Database kami\n[2] Ubah Data Penjadwalan\n[3] Hapus akun\n[4] Log Out\n: "))
    if milihmenuAdmin == 1:
        databaseKami()
    elif milihmenuAdmin == 2:
        ubahdataPenjadwalan()
    elif milihmenuAdmin == 3:
        hapusakun()


def databaseKami():
    os.system("cls")
    print("Pilih Database yang anda inginkan\n[1] data.csv\n[2] datatanaman.csv")
    milihDb = int(input("\nPilihan anda : "))
    if milihDb == 1:
        os.system("cls")    
        db1 = pd.read_csv("data.csv")
        print(db1)
    elif milihDb == 2:
        os.system("cls")    
        db2 = pd.read_csv("datatanaman.csv")
        print(db2)
    inputan3 = int(input("[1] Kembali ke Main Menu Admin\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainmenuAdmin()
    elif inputan3 == 2:
        outro()

def ubahdataPenjadwalan():
    os.system("cls")
    print("Pilih Database yang ingin anda rubah\n[1] datatanaman.csv")
    ubahdb = int(input("\nPilihan anda :"))
    if ubahdb == 1 :
        os.system("cls")
        db1 = pd.read_csv('database\\datatanaman.csv',index_col=0)
        pilihubah1 = int(input("Pilih Data Yang Ingin Anda Rubah\n[1] Lama Panen\n[2] Pupuk 1\n[3] Pupuk 2\n[4] Pupuk 3\nMasukkan Pilihan Anda : "))
        os.system("cls")
        tanaman = int(input ("Pilih Jenis Tanaman \n[1] Padi\n[2] Jagung\n[3] Kedelai\n[4] Tebu\n[5] Cabai\n[6] Tomat\n Masukkan Pilihan Anda : "))
        os.system("cls")
        yangdiubah = input("Masukkan data terbaru : ")
        db1.iloc[tanaman-1 , pilihubah1-1] = yangdiubah
        db1.to_csv('database\\datatanaman.csv')
    else :
        print("Pilihan anda salah")
        ubahdataPenjadwalan() 

    print(db1)       
    inputan3 = int(input("[1] Kembali ke Main Menu Admin\n[2] Kembali ke menu sebelumnya \n[3] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainmenuAdmin()
    elif inputan3 == 2:
        ubahdataPenjadwalan()
    elif inputan3 == 3:
        outro() 

def hapusakun():
    os.system("cls")
    with open ("database\\users.json","r") as ndaftar:
        userData = json.load(ndaftar)
    print("Hapus Akun\n")
    for idx,i in enumerate(userData):
        print(f"[{idx+1}]",i["nama"])
    index = int(input("Masukkan index akun yang ingin anda hapus atau [99] untuk kembali : "))
    if index == 99:
        mainmenuAdmin()
    userData.pop(index-1)

    with open("database\\users.json", "w") as data:
        json.dump(userData, data, indent=4)

    inputan3 = int(input("[1] Kembali ke Main Menu Admin\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainmenuAdmin()
    elif inputan3 == 2:
        outro()
def outro(): 
    os.system("cls")
    print("="*80) 
    print("Terimakasih telah menggunakan program Potray".center(80))
    print("="*80)

mainmenuAdmin()