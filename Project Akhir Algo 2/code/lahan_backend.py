import os, csv
import pandas as pd

def outro(): 
    os.system("cls")
    print("="*80) 
    print("Terimakasih telah menggunakan program Potray".center(80))
    print("="*80)

def macamlahan():
    print("Lahan yang ada :")
    listlahan = pd.read_csv('database\\data.csv')
    nilaikosong = 0
    for x in range(len(listlahan)):
        if nilaikosong < len(listlahan) :
            print(f"[{listlahan.iloc[nilaikosong,0]}]" , f"{listlahan.iloc[nilaikosong,1]}")
            nilaikosong += 1
        else :
            break
    banyaklahan()

def banyaklahan() :
    lanjut = int(input("[0] Kembali\nMasukkan Pilihan anda : "))
    listlahan2 = pd.read_csv('database\\data.csv')
    listkosong = []
    listkosongcolumn = []
    for y in listlahan2.iloc[lanjut - 1 , :] :
        listkosong.append([f"{y}"])

    for z in listlahan2 :
        listkosongcolumn.append(f"{z}")

    dictkosong = {}
    arraykosong = 0
    for r in range(len(listkosong)) :
        dictkosong[f'{listkosongcolumn[arraykosong]}'] = listkosong[arraykosong]
        arraykosong += 1
    df = pd.DataFrame(dictkosong)
    os.system("cls")
    if lanjut == 0 :
        menupenjadwalan()
    else :
        df.iloc[0,3] = f"{df.iloc[0,3]} Hari"
        if df.iloc[0,4] != 'nan' :
            df.iloc[0,4] = f"Hari ke-{df.iloc[0,4]}"
        if df.iloc[0,5] != 'nan' :      
            df.iloc[0,5] = f"Hari ke-{df.iloc[0,5]}"
        if df.iloc[0,6] != 'nan' :      
            df.iloc[0,6] = f"Hari ke-{df.iloc[0,6]}"
        if df.iloc[0,7] != 'nan' :      
            df.iloc[0,7] = f"Hari ke-{df.iloc[0,7]}"

        if df.iloc[0,4] == 'nan' :
            df.iloc[0,4] = "-"
        if df.iloc[0,5] == 'nan' :      
            df.iloc[0,5] = "-"
        if df.iloc[0,6] == 'nan' :      
            df.iloc[0,6] = "-"
        if df.iloc[0,7] == 'nan' :      
            df.iloc[0,7] = "-"
        
        print(df.iloc[0,1],"\n")
        print(df)
    # inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    # if inputan3 == 1:
    #     os.system("cls")
    #     import pilih_menu
    # elif inputan3 == 2:
    #     outro()

def hapuslahan() :
    buka = pd.read_csv('database\\data.csv')
    print("Pilih Lahan Yang Ingin Anda Hapus")
    nilaikosong = 0
    for x in range(len(buka)):
        if nilaikosong < len(buka) :
            print(f"[{buka.iloc[nilaikosong,0]}]" , f"{buka.iloc[nilaikosong,1]}")
            nilaikosong += 1
        else :
            break   
    pilihan = int(input("[0] Kembali \nMasukkan Pilihan Anda : "))
    if pilihan == 0 :
        menupenjadwalan()
    else :

        columnskosong = []
        row = []
        for i in buka :
            columnskosong.append(i)  

        for j in range (len(buka)) :
            
            row.append([buka.iloc[j,0],buka.iloc[j,1],buka.iloc[j,2],buka.iloc[j,3],buka.iloc[j,4],buka.iloc[j,5],buka.iloc[j,6],buka.iloc[j,7]])
        df = pd.DataFrame(row , columns=columnskosong)
        indexkosong = []
        for k in range(len(df)-1) :
            indexkosong.append(k)

        df = df.drop(pilihan-1)
        df.index = [indexkosong]

        for x in range(len(df)) :
            df.iloc[x,0] = x + 1

        df.to_csv('database\\data.csv',index=False)
        # inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
        # if inputan3 == 1:
        #     os.system("cls")
        #     import pilih_menu
        # elif inputan3 == 2:
        #     outro()

def menupenjadwalan():   
    os.system("cls") 
    pilihan = int(input("Menu Penjadwalan\n[1] Jadwal Yang Sudah Ada\n[2] Buat Jadwal Baru\n[3] Hapus Lahan\nSilahkan Pilih Menu : "))
    if pilihan == 1 :
        os.system("cls")
        macamlahan()
                
    elif pilihan == 2 :
        os.system("cls")
        print("Buat Jadwal Baru")
        buatjadwal()
    elif pilihan == 3 :
        os.system("cls")
        print("Hapus Lahan")
        hapuslahan()

    else :
        os.system("cls")
        print("Maaf jawaban anda tidak ada di pilihan")
        menupenjadwalan()

def buatjadwal() :
    os.system("cls")
    Lahanbaru = input("Masukkan Nama Lahan Baru : ")
    pilihjenis = int(input("Pilih Jenis Tanaman\n[1] Padi\n[2] Jagung\n[3] Kedelai\n[4] Tebu\n[5] Cabai\n[6] Tomat\nSilahkan Pilih Jenis Tanaman : "))
    datatanaman = pd.read_csv('database\\datatanaman.csv')
    listdatatanaman = pd.read_csv('database\\data.csv')
    datasementara = [len(listdatatanaman)+1,f"{Lahanbaru}"]

    if pilihjenis == 1 :
        bacadata = datatanaman.iloc[0,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("database\\data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 2 :
        bacadata = datatanaman.iloc[1,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("database\\data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 3 :
        bacadata = datatanaman.iloc[2,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("database\\data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 4 :
        bacadata = datatanaman.iloc[3,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("database\\data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 5 :
        bacadata = datatanaman.iloc[4,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("database\\data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 6 :
        bacadata = datatanaman.iloc[5,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("database\\data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    else :
        os.system("cls")
        print("Pilihan Salah, Masukkan Jenis Tanaman yang Benar")
        buatjadwal()

def macamlahan():
    print("Lahan yang ada :")
    listlahan = pd.read_csv('database\\data.csv')
    nilaikosong = 0
    for x in range(len(listlahan)):
        if nilaikosong < len(listlahan) :
            print(f"[{listlahan.iloc[nilaikosong,0]}]" , f"{listlahan.iloc[nilaikosong,1]}")
            nilaikosong += 1
        else :
            break
    banyaklahan()

def banyaklahan() :
    lanjut = int(input("[0] Kembali\nMasukkan Pilihan anda : "))
    listlahan2 = pd.read_csv('database\\data.csv')
    listkosong = []
    listkosongcolumn = []
    for y in listlahan2.iloc[lanjut - 1 , :] :
        listkosong.append([f"{y}"])

    for z in listlahan2 :
        listkosongcolumn.append(f"{z}")

    dictkosong = {}
    arraykosong = 0
    for r in range(len(listkosong)) :
        dictkosong[f'{listkosongcolumn[arraykosong]}'] = listkosong[arraykosong]
        arraykosong += 1
    df = pd.DataFrame(dictkosong)
    os.system("cls")
    if lanjut == 0 :
        menupenjadwalan()
    else :
        df.iloc[0,3] = f"{df.iloc[0,3]} Hari"
        if df.iloc[0,4] != 'nan' :
            df.iloc[0,4] = f"Hari ke-{df.iloc[0,4]}"
        if df.iloc[0,5] != 'nan' :      
            df.iloc[0,5] = f"Hari ke-{df.iloc[0,5]}"
        if df.iloc[0,6] != 'nan' :      
            df.iloc[0,6] = f"Hari ke-{df.iloc[0,6]}"
        if df.iloc[0,7] != 'nan' :      
            df.iloc[0,7] = f"Hari ke-{df.iloc[0,7]}"

        if df.iloc[0,4] == 'nan' :
            df.iloc[0,4] = "-"
        if df.iloc[0,5] == 'nan' :      
            df.iloc[0,5] = "-"
        if df.iloc[0,6] == 'nan' :      
            df.iloc[0,6] = "-"
        if df.iloc[0,7] == 'nan' :      
            df.iloc[0,7] = "-"
        
        print(df.iloc[0,1],"\n")
        print(df)
    # inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    # if inputan3 == 1:
    #     os.system("cls")
    #     import pilih_menu
    # elif inputan3 == 2:
    #     outro()

def hapuslahan() :
    buka = pd.read_csv('database\\data.csv')
    print("Pilih Lahan Yang Ingin Anda Hapus")
    nilaikosong = 0
    for x in range(len(buka)):
        if nilaikosong < len(buka) :
            print(f"[{buka.iloc[nilaikosong,0]}]" , f"{buka.iloc[nilaikosong,1]}")
            nilaikosong += 1
        else :
            break   
    pilihan = int(input("[0] Kembali \nMasukkan Pilihan Anda : "))
    if pilihan == 0 :
        menupenjadwalan()
    else :

        columnskosong = []
        row = []
        for i in buka :
            columnskosong.append(i)  

        for j in range (len(buka)) :
            
            row.append([buka.iloc[j,0],buka.iloc[j,1],buka.iloc[j,2],buka.iloc[j,3],buka.iloc[j,4],buka.iloc[j,5],buka.iloc[j,6],buka.iloc[j,7]])
        df = pd.DataFrame(row , columns=columnskosong)
        indexkosong = []
        for k in range(len(df)-1) :
            indexkosong.append(k)

        df = df.drop(pilihan-1)
        df.index = [indexkosong]

        for x in range(len(df)) :
            df.iloc[x,0] = x + 1

        df.to_csv('database\\data.csv',index=False)
        # inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
        # if inputan3 == 1:
        #     os.system("cls")
        #     import pilih_menu
        # elif inputan3 == 2:
        #     outro()

    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        import pilih_menu
    elif inputan3 == 2:
        outro()

menupenjadwalan()