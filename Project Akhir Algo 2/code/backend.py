import pandas as pd
import json
import os
import csv
import tkinter
from tkinter import *

os.system('cls')

def mainmenuAdmin() :
    os.system("cls")
    print("="*80)
    print("Selamat datang di Menu Admin program Potray".center(80))
    print("="*80)
    milihmenuAdmin = int(input("Silahkan pilih nomer fitur yang anda inginkan\n[1] Database kami\n[2] Ubah Data Penjadwalan\n[3] Hapus akun\n[4] Log Out\n[5] Kembali ke HomePage\n[6] Keluar dari program\nPilihan : "))
    if milihmenuAdmin == 1:
        databaseKami()
    elif milihmenuAdmin == 2:
        ubahdataPenjadwalan()
    elif milihmenuAdmin == 3:
        hapusakun()
    elif milihmenuAdmin == 4:
        masuk()
    elif milihmenuAdmin == 5:
        awal()
    elif milihmenuAdmin == 6:
        outro()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        mainMenu()

def intro():
    print("="*80 ) 
    print("Silahkan login".center(80))
    print("="*80 ) 

def outro(): 
    os.system("cls")
    print("="*80) 
    print("Terimakasih telah menggunakan program Potray".center(80))
    print("="*80)

def masuk():
    while True:
        os.system("cls")
        intro()
        name = input("Masukkan nama : ")
        pword = input("Masukkan password : ")
        if validasiLogin(name, pword):
            os.system("cls")
            if validasiLogin(name, pword)[1]:
                mainmenuAdmin()
            else:
                mainMenu()
            break
        else:
            input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
            continue

def daftar():
    os.system("cls")
    namadaftar = input("Masukkan nama : ")
    isAdmin = False
    with open ('database\\users.json','r') as ndaftar:
        userData = json.load(ndaftar)
    masukin = {}
    masukin["nama"] = namadaftar
    for i in userData:
        if masukin["nama"] == i["nama"]:
            print("Akun Sudah Tersedia")
            input("Untuk lanjut tekan enter")
            awal()
    pwdaftar = input("Masukkan password : ")
    masukin["pw"] = pwdaftar
    masukin["isAdmin"] = isAdmin
    userData.append(masukin)
    isAdmin = False
    with open ("database\\users.json",'w') as ndaftarin:
        json.dump(userData,ndaftarin,indent=4)
    masuk()

def awal():
    os.system("cls")
    print("="*80)
    print("Selamat Datang Di HomePage POTRAY".center(80))
    print("="*80)
    print("\n[1] Register\n[2] Login")
    awal1 = int(input("Pilihan : "))
    if awal1 == 1:
        os.system("cls")
        daftar()
    elif awal1 == 2:
        os.system("cls")
        masuk()
    else:
        input("Masukkan pilihan yang ada\nUntuk lanjut tekan enter")
        awal()

def validasiLogin(nama, password):
    dict = {}
    kondisi = False
    with open("database\\users.json", "r") as data:
        reader = json.load(data)

    for i in reader:     
        if nama == i["nama"]:
            dict["nama"] = i["nama"]
            dict["pw"] = i["pw"]
            dict["isAdmin"] = i["isAdmin"]
    if dict == {}:
        return kondisi
    else:
        if password != dict["pw"]:
            return kondisi
        else:
            kondisi = True
    return [kondisi, dict["isAdmin"]]

def mainMenu() :
    os.system("cls")
    print("="*80)
    print("Selamat datang di Program Potray".center(80))
    print("="*80)
    milihMenu = int(input("Silahkan pilih nomer fitur yang anda inginkan\n[1] Jual Hasil Panen dengan Truk\n[2] Rute ke Pasar Terdekat\n[3] Lahan saya\n[4] Konsultasi\n[5] Log Out\n[6] Kembali ke HomePage\n[7] Keluar dari program\nPilihan : "))
    if milihMenu == 1:
        menuknapsack()
    elif milihMenu == 2:
        shortpath()
    elif milihMenu == 3:
        menupenjadwalan()
    elif milihMenu == 4:
        rekomendasiPenanaman()
    elif milihMenu == 5:
        masuk()
    elif milihMenu == 6:
        awal()
    elif milihMenu == 7:
        outro()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        mainMenu()

def shortpath():
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=1280, height=720)
    canvas.pack()
    
    img = PhotoImage(file='png\\indeksPasar.png')
    Label(window, image=img).place(x=820, y=640)

    def Initiate(pasar):
        # Kode inisialisasi region
        nedge = ''
        with open(f'database\\pasarjember.txt', "r") as txt:
            while True:
                nodedge = txt.readline()
                nedge+=nodedge
                if '\n' not in nodedge:
                    break
        nodes = nedge.split('\n')[0].split(',')
        before, after = nedge.split('\n')[1].split(','), {}
        for i in before:
            a = int(i.split('.')[0])
            b = int(i.split('.')[1])
            weight = int(i.split('.')[2])
            if a not in after:
                after[a] = {}
            after[a][b] = weight
            if b not in after:
                after[b] = {}
            after[b][a] = weight
        return after, nodes

    def Graph(edges, lead, last, graph=[]):
        # Kode fungsi Graph
        graph = graph + [lead]
        if lead == last:
            return [graph]
        if lead not in edges:
            return []
        graphs = []
        for node in edges[lead]:
            if node not in graph:
                newGraph = Graph(edges,node,last,graph)
                for newNode in newGraph:
                    graphs.append(newNode)
        return graphs

    def Weight(edges, lead, last):
        # Kode fungsi Weight
        table = Graph(edges,lead,last)
        for i in table:
            weight = 0
            for j in range(len(i)-1):
                weight += edges[i[j]][i[j+1]]
            i.insert(0,weight)    
        return sorted(table)

    def Minimum(Table):
        # Kode fungsi Minimum
        for i in Table:
            i.remove(i[0])
        return Table

    def NodeToCoordinate(nodes, edges, Table):
        # Kode fungsi NodeToCoordinate
        list = []
        coordinates = []
        for node in nodes:
            label = node.split('.')[0]
            xaxis = int(node.split('.')[1])
            yaxis = int(node.split('.')[2])
            list.append([xaxis,yaxis])
            canvas.create_oval(xaxis-5,yaxis-5,xaxis+5,yaxis+5,fill='black')
            canvas.create_text(xaxis-20,yaxis-20,text=str(label),fill='black',font=('Poppins 9'))
            
        for i in edges.keys():
            for j in edges[i].keys():
                coordinate = [i,j,edges[i][j]]
                coordinates.append(coordinate)
        for k in coordinates:
            for l in range(len(k)-1):
                k[l] = list[k[l]]
        for j in range(len(Table[0])):
            Table[0][j] = list[Table[0][j]]
        return coordinates, Table[0]

    def DrawPath(all_paths, shortest_path):
        # Kode fungsi DrawPath
        for i in range(len(all_paths)):
            xaxis1, yaxis1, xaxis2, yaxis2 = all_paths[i][0][0], all_paths[i][0][1], all_paths[i][1][0], all_paths[i][1][1]
            canvas.create_line(xaxis1, yaxis1, xaxis2, yaxis2, fill='black')
            canvas.create_text((xaxis1+xaxis2)/2,(yaxis1+yaxis2)/2,text=str(all_paths[i][2]),fill='black',font= ('Poppins 8'))
        for i in range(len(shortest_path)-1):
            canvas.create_line(shortest_path[i][0], shortest_path[i][1], shortest_path[i+1][0], shortest_path[i+1][1], fill='red')

    def Dijkstra(lead, last, edges, nodes):
        # Kode fungsi Dijkstra
        Table = Weight(edges, lead, last)
        Table = Minimum(Table)
        all_paths, shortest_path = NodeToCoordinate(nodes, edges, Table)
        DrawPath(all_paths, shortest_path)
        window.mainloop()

    def handle_button_click():
        PasarAwal = int(entry_awal.get())
        PasarAkhir = int(entry_akhir.get())
        AFTER, NODES = Initiate('PASAR')
        Dijkstra(PasarAwal, PasarAkhir, AFTER, NODES)

    label_awal = tkinter.Label(window, text="Index Pasar Awal :")
    label_awal.pack()

    entry_awal = tkinter.Entry(window)
    entry_awal.pack()

    label_akhir = tkinter.Label(window, text="Index Pasar Akhir :")
    label_akhir.pack()

    entry_akhir = tkinter.Entry(window)
    entry_akhir.pack()

    button = tkinter.Button(window, text="Cari Jalur", command=handle_button_click)
    button.pack()

    window.mainloop()

def buatjadwal() :
    os.system("cls")
    Lahanbaru = input("Masukkan Nama Lahan Baru : ")
    pilihjenis = int(input("Pilih Jenis Tanaman\n[1] Padi\n[2] Jagung\n[3] Kedelai\n[4] Tebu\n[5] Cabai\n[6] Tomat\nSilahkan Pilih Jenis Tanaman : "))
    datatanaman = pd.read_csv('database\\datatanaman.csv')
    listdatatanaman = pd.read_csv('data.csv')
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
    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainMenu()
    elif inputan3 == 2:
        outro()

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
        inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
        if inputan3 == 1:
            os.system("cls")
            mainMenu()
        elif inputan3 == 2:
            outro()

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

def search_month(month, target_list):
    """
    Fungsi untuk melakukan pencarian biner pada list bulan-bulan yang cocok
    dengan bulan yang diinputkan pengguna.
    """
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

def rekomendasiPenanaman():
    os.system("cls")
    print("Rekomendasi Penanaman".center(80, "="))
    print("""Pilih jenis tanaman yang anda cari
    1. Padi
    2. Jagung
    3. Kedelai
    4. Tebu
    5. Cabai
    6. Tomat
    """)
    cekBulan()

def cekBulan():
    jenis_tanaman = int(input("Silahkan pilih : "))
    bulan = input('Masukkan bulan : ').capitalize()

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
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        rekomendasiPenanaman()

    if search_month(bulan, target_list):
        print("Bulan {} cocok untuk menanam {}".format(bulan, tanaman))
    else:
        print("Bulan {} tidak cocok untuk menanam {}".format(bulan, tanaman))

    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainMenu()
    elif inputan3 == 2:
        outro()

def pemupukan():
    os.system("cls")
    print("Melalui Akar Tanaman".center(80,"="),"\n")
    print("1. Pemupukan dengan cara disebar (broadcasting)\n2. Pemupukan dengan cara ditempatkan di antara larikan/barisan\n3. Pemupukan dengan cara ditempatkan dalam lubang")
    akar = int(input("Pilih metode pemupukan : "))
    if akar == 1:
        os.system("cls")
        print("Pemupukan dengan cara disebar (broadcasting)\n")
        print("Pemupukan dilakukan dengan cara meyebar pupuk secara merata pada tanah\n-tanah di sekitar pertanaman atau pada waktu pembajakan/penggaruan\nterakhir. Dilakakuna sehari sebelum tanam, kemudian diinjak-injak\nagar pupuk masuk ke dalam tanah. Beberapa pertimbangan untuk menggunakan\ncara ini adalah:\n\n1. Tanaman ditanam pada jarak tanam yang rapat, baik teratur dalam\nbarisan maupun tidak teratur dalam barisan,\n2. Tanaman mempunyai akar yang dangkal atau berada dekat dengan permukaan\ntanah,\n3. Tanah mempunyai kesuburan yang relatif baik,\n4. Pupuk yang dipakai cukup banyak atau dosis permukaan tinggi,\n5. Daya larut pupuk besar, karena bila daya larutnya rendah maka\nyang terserap tanaman sedikit,\n6. Cara pemupukan ini biasanya digunakan untuk memupuk tanaman padi,\nkacang-kacangan, dan lain-lain yang mempunyai jarak tanam rapat. Kerugian\ncara ini ialah merangsang pertumbuhan rumput pengganggu/gulma dan\nkemungkinan pengikatan unsur hara tertentu oleh tanah lebih tinggi.\n")
    elif akar == 2:
        os.system("cls")
        print("Pemupukan dengan cara ditempatkan di antara larikan/barisan\n")
        print("Pemupukan dilakukan dengan cara menaburkan pupuk di antara larikan\ntanaman dan kemudian ditutup kembali dengan tanah. Untuk tanaman tahunan,\nditaburkan melingkari tanaman dengan jarak tegak lurus dengan daun terjauh\n(tajuk daun) dan kemudian ditutup kembali dengan tanah.\nCara ini dilakukan dengan pertimbangan-pertimbangan sebagai berikut:\n\n1. Pupuk yang digunakan relatif sedikit,\n2. Jarak tanam antar tanaman yang dipupuk cukup jarang dan jarak antara\nbarisan pertanaman cukup jarang,\n3. Kesuburan tanah rendah,\n4. Tanaman dengan perkembangan akar yang sedikit,\n5. Untuk tanah tegalan atau darat.\n")
    elif akar == 3:
        os.system("cls")
        print("Pemupukan dengan cara ditempatkan dalam lubang\n")
        print("Pemupukan dilakukan dengan cara pupuk dibenamkan ke dalam lubang di\nsamping batang sedalam kurang lebih 10 cm dan ditutup dengan tanah.\nUntuk tanaman tahunan, pupuk dibenamkan ke dalam lubang pupuk yang\nmelingkari tanaman dengan jarak tegak lurus dengan daun terjauh (tajuk\ndaun) dan ditutup kembali dengan tanah. Cara ini dilakukan dengan\npertimbangan sama dengan pemupukan cara larikan/barisan.\n")
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        TipsTrick()

def penyemprotan():
            os.system("cls")
            print("PEMUPUKAN MELALUI PENYEMPROTAN DAUN TANAMAN (Spraying)\n")
            print("Pemupukan dengan cara pemyemprotan menggunakan pupuk yang dilarutkan\ndalam air dengan konsentrasi sangat rendah kemudian disemprotkan langsung\nkepada daun dengan alat penyemprot biasa (hand sprayer). Pada lahan\nyang luas dapat menggunakan pesawat terbang.\nSebelum melakukan penyemprotan, ada beberapa hal yang harus diketahui\ndulu, yaitu:\n\n1. Konsentrasi larutan pupuk yang dibuat harus sangat rendah atau mengikuti\npetunjuk dalam kemasan pupuk. Jangan berlebihan! Lebih baik kurang\ndaripada berlebihan. Kalau konsentrasinya lebih rendah dari anjuran maka\nuntuk mengimbanginya frekuensi pemupukan bisa diperbanyak, misalnya\ndianjurkan 10 hari bisa dipercepat jadi seminggu sekali.\n2. Pupuk daun disemprotkan ke bagian daun yang menghadap ke bawah karena\nmulut daun (stomata) umumnya menghadap ke bawah atau bagain punggung daun.\n3. Pupuk hendaknya disemprotkan ketika matahari tidak sedang terik-teriknya.\nPaling ideal dilakukan sore atau pagi hari persis ketika matahari belum\nbegitu menyengat. Kalau dipaksakan juga menyemprot ketika panas, pupuk\ndaun itu banyak menguap daripada diserap oleh daun.\n4. Penyemprotan pupuk daun jangan dilaksanakan menjelang musim hujan.\nKarena beresiko pupuk daun akan habis tercuci oleh air hujan. Terlebih\nlagi pada saat hujan seperti itu stomata sedang menutup.\n5. Biasakanlah untuk membaca keterangan yang ada pada kemasan pupuk.\n")

def TipsTrick():
    os.system("cls")
    print("Menu Tips & Trick".center(80,"="))
    print("[1] Metode Pemupukan\n[2] Rekomendasi Penanaman Sesuai Bulan")
    pilihan = int(input("Pilihlah :"))
    if pilihan == 1:
        os.system("cls")
        print("METODE PEMUPUKAN YANG BAIK\n")
        print("Pemupukan merupakan salah satu proses penting dalam budidaya tanaman.\nKenapa menjadi prosesi penting? Karena proses pemupukan akan sangat\nmenentukan keberhasilan produksi tanaman tersebut. Selain harus mengetahui\njenis-jenis pupuk dan proses penyerapan pupuk, kita juga harus tahu\nbagaimana cara mengaplikasikan pupuk pada tanaman yang dibudidayakan\nsehingga proses tersebut menjadi lebih efektif dan efisien.")
        print("\nCara Pemupukan")
        print("1. Melalui Akar Tanaman\n2. Penyemprotan Daun Tanaman (Spraying)\n")
        metode = int(input("Pilihlah : "))
        if metode == 1:
            pemupukan()
        elif metode == 2:
            penyemprotan()
        else:
            input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
            TipsTrick()
        inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
        if inputan3 == 1:
            os.system("cls")
            mainMenu()
        elif inputan3 == 2:
            outro()
    elif pilihan == 2:
        rekomendasiPenanaman()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        TipsTrick()
    
    os.system("cls")
    print("="*80)
    print("Selamat datang di Program Potray".center(80))
    print("="*80)
    milihMenu = int(input("Silahkan pilih nomer fitur yang anda inginkan\n[1] Truk knapsack\n[2] Rute ke toko terdekat\n[3] Perhitungan\n[4] Tips & Trick\n[5] Log Out\n[6] Kembali ke HomePage\n[7] Keluar dari program\nPilihan : "))
    if milihMenu == 1:
        menuknapsack()
    elif milihMenu == 2:
        menupenjadwalan()
    elif milihMenu == 3:
        shortpath()
    elif milihMenu == 4:
        TipsTrick()
    elif milihMenu == 5:
        masuk()
    elif milihMenu == 6:
        awal()
    elif milihMenu == 7:
        outro()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        mainMenu()

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


    os.system("cls")
    print("="*80)
    print("Selamat Datang Di HomePage POTRAY".center(80))
    print("="*80)
    print("\n[1] Register\n[2] Login")
    awal1 = int(input("Pilihan : "))
    if awal1 == 1:
        os.system("cls")
        daftar()
    elif awal1 == 2:
        os.system("cls")
        masuk()
    else:
        input("Masukkan pilihan yang ada\nUntuk lanjut tekan enter")
        awal()

def menuknapsack():
    os.system('cls')

    # wadah untuk menampung data barang
    array = []

    while True:
        # urutkan barang 
        print('='*120)
        print('No.\tNama Barang\tBerat Barang(Kg)\tHarga Barang(Rp)\t\t\tValue')
        for i in array:
            print('{}.\t{}\t\t{}\t\t\t{}\t\t\t\t{}'.format(array.index(i)+1, i['nama barang'], i['berat'], i['harga'], i['value']))
        print('='*120)
        array.sort(key = lambda x : x['value'], reverse=True)
        ngangkut = int(input('\npilih jenis tanaman yang akan diangkut untuk dijual :\n[1] padi\n[2] jagung\n[3] kedelai\n[4] tebu\n[5] cabai\n[6] tomat\n: '))
        if ngangkut == 1:
            nama = 'padi'
            berat = float(input('berat padi (kg) : '))
            harga = float(input('harga padi per kg (Rp) : '))
            harga_awal = harga * berat
            value = harga_awal // berat
        elif ngangkut == 2:
            nama = 'jagung'
            berat = float(input('berat jagung (kg) : '))
            harga = float(input('harga jagung per kg (Rp) : '))
            harga_awal = harga * berat
            value = harga_awal // berat
        elif ngangkut == 3:
            nama = 'kedelai'
            berat = float(input('berat kedelai (kg) : '))
            harga = float(input('harga kedelai per kg (Rp) : '))
            harga_awal = harga * berat
            value = harga_awal // berat
        elif ngangkut == 4:
            nama = 'tebu'
            berat = float(input('berat tebu (kg) : '))
            harga = float(input('harga tebu per kg (Rp) : '))
            harga_awal = harga * berat
            value = harga_awal // berat
        elif ngangkut == 5:
            nama = 'cabai'
            berat = float(input('berat cabai (kg) : '))
            harga = float(input('harga cabai per kg (Rp) : '))
            harga_awal = harga * berat
            value = harga_awal // berat
        elif ngangkut == 6:
            nama = 'tomat'
            berat = float(input('berat tomat (kg) : '))
            harga = float(input('harga tomat per kg (Rp) : ')) 
            harga_awal = harga * berat
            value = harga_awal // berat

        # tampung barang sebagai dictionary
        array.append(
            {
                'nama barang' : nama,
                'berat' : berat,
                'harga' : harga_awal,
                'value' : value
            }
        )
        
        lanjutkah = input('apakah anda ingin menambah barang? [y] / [n] : ')
        if lanjutkah == 'y':
            os.system('cls')
            continue
        elif lanjutkah == 'n':
            os.system('cls')
            print('='*120)
            print('No.\tNama Barang\tBerat Barang(Kg)\tHarga Barang(Rp)\t\t\tValue')
            for i in array:
                print('{}.\t{}\t\t{}\t\t\t{}\t\t\t\t{}'.format(array.index(i)+1, i['nama barang'], i['berat'], i['harga'], i['value']))
            print('='*120)
            array.sort(key = lambda x : x['value'], reverse=True)
            break

    # operasi knapsack 
    knapsack = []
    harga_masuk = 0
    berat_masuk = 0
    kapasitas = int(input('kapasitas truk (kg) : '))    
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

    # hasil knapsack 
    print('\nHasil Fractional Knapsack Greedy')
    print('='*90)
    print('No.\tNama Barang\tBerat Barang(Kg)\tHarga Barang(Rp)\t\t\tValue')
    for i in knapsack:
        print('{}.\t{}\t\t{}\t\t\t{}\t\t\t\t{}'.format(knapsack.index(i)+1, i['nama barang'], i['berat'], i['harga'], i['value']))
    print('='*90)
    print(f'berat barang yg masuk : {berat_masuk} kg')
    print(f'sisa kapasitas knapsack : {kapasitas}')
    print(f'total harga : Rp{harga_masuk}')
    
    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainMenu()
    elif inputan3 == 2:
        outro()
awal()

































