import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Rute')
canvas = tkinter.Canvas(window, width=1280, height=720)
canvas.pack()

img = PhotoImage(file='png\\indeksPasar.png')
Label(window, image=img).place(x=820, y=640)

def inisiasi():
    pemisah = ''
    with open(f'database\\pasarjember.txt', "r") as txt:
        while True:
            nodedge = txt.readline()
            pemisah+=nodedge
            if '\n' not in nodedge:
                break
    vertex = pemisah.split('\n')[0].split(',')
    before, after = pemisah.split('\n')[1].split(','), {}
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
    return after, vertex

def Grafik(edges, awal, akhir, graph=[]):
    graph = graph + [awal]
    if awal == akhir:
        return [graph]
    if awal not in edges:
        return []
    graphs = []
    for node in edges[awal]:
        if node not in graph:
            newGraph = Grafik(edges,node,akhir,graph)
            for newNode in newGraph:
                graphs.append(newNode)
    return graphs

def Weight(edges, awal, akhir):
    table = Grafik(edges,awal,akhir)
    for i in table:
        weight = 0
        for j in range(len(i)-1):
            weight += edges[i[j]][i[j+1]]
        i.insert(0,weight)    
    return sorted(table)

def Minimum(Table):
    for i in Table:
        i.remove(i[0])
    return Table

def NodeToCoordinate(vertex, edges, Table):
    list = []
    coordinates = []
    for node in vertex:
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
    for i in range(len(all_paths)):
        xaxis1, yaxis1, xaxis2, yaxis2 = all_paths[i][0][0], all_paths[i][0][1], all_paths[i][1][0], all_paths[i][1][1]
        canvas.create_line(xaxis1, yaxis1, xaxis2, yaxis2, fill='black')
        canvas.create_text((xaxis1+xaxis2)/2,(yaxis1+yaxis2)/2,text=str(all_paths[i][2]),fill='black',font= ('Poppins 8'))
    for i in range(len(shortest_path)-1):
        canvas.create_line(shortest_path[i][0], shortest_path[i][1], shortest_path[i+1][0], shortest_path[i+1][1], fill='red')

def Rute(awal, akhir, edges, vertex):
    Table = Weight(edges, awal, akhir)
    Table = Minimum(Table)
    all_paths, shortest_path = NodeToCoordinate(vertex, edges, Table)
    DrawPath(all_paths, shortest_path)
    window.mainloop()

def handle_button_click():
    PasarAwal = int(entry_awal.get())
    PasarAkhir = int(entry_akhir.get())
    after, before = inisiasi()
    Rute(PasarAwal, PasarAkhir, after, before)

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
