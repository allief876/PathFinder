import g
import n
import math
import networkx as nx
import matplotlib.pyplot as plt

# A* search
def astar(graph, heuristics, start, end):

    # Bikin variabel buat visualisasi
    G = GraphVisual()
    
    # Bikin list untuk node terbuka dan tertutup
    open = []
    closed = []

    # Membuat node awal & node akhir
    start_node = n.Node(start, None)
    goal_node = n.Node(end, None) # Parent dari goal ialah None karena belum diketahui
    
    # Tambahkan node pertama ke node terbuka
    open.append(start_node)
    
    # Looping sampai list terbuka kosong
    while len(open) > 0:
        # current_node ialah node yang mempunyai f terendah,
        # sehingga urutkan terlebih dahulu baru ambil kemudian
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)
        
        # Periksa apakah goal telah dicapai, jika ya kembalikan pathnya secara reversal & proses selesai
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ' ' + str(current_node.g))
                # Bentuk graf dari current_node dan "orang tua" dari current_node
                G.addEdge(current_node.name,current_node.parent.name)
                current_node = current_node.parent
            path.append(start_node.name + ' ' + str(start_node.g))
            # Visualisasikan graf
            G.visualize()
            # Kembalikan path secara terbalik (Karena kita menelusuri dari goal_node)
            return path[::-1]

        # Dapatkan tetangga
        neighbors = graph.get(current_node.name)

        # Untuk setiap tetangganya current...
        for key, value in neighbors.items():
            neighbor = n.Node(key, current_node)

            # Cek jika tetangga ada pada closed list
            if(neighbor in closed):
                continue

            # Hitung harga pathnya
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h

            # Cek jika tetangga ada di list terbuka dan punya nilai f (g + h) yang lebih tinggi
            if(add_to_open(open, neighbor)):

                # Tambahkan tetangga ke list terbuka
                open.append(neighbor)
                
    # Kembalikan none, tidak ada path yang ditemukan
    return None

# Fungsi untuk menambah tetangga ke list terbuka
# Pada dasarnya ini untuk mengecek apakah nilai f lebih rendah
def add_to_open(open, neighbor):
    # cek bila neighbor sama dengan open & nilai f neighbor lebih besar
    # daripada f nya node
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

# Kelas GraphVisual
class GraphVisual:
   
    def __init__(self):
        
        # self adalah list yang menyimpan semua
        # himpunan edge yang membentuk graf
        self.visual = []
          
    # meminta node asal dan node tujuan
    # serta memasukkan ke self
    def addEdge(self, a, b):
        edge = [a, b]
        self.visual.append(edge)
    
    # Objek dari kelas Graph dari modul networkx
    # nx.draw_networkx(G) - membentuk graf
    # plt.show() menampilkan graf
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

# Rumus menentukan jarak dua titik
def Jarak2Node(x1,x2,y1,y2):
    return (math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)))

# PROGRAM UTAMA

print("Halo, silahkan pilih nomor file yang ingin Anda periksa!")
print("Pilihan:")
print("1. tc1.txt (Kampus ITB)")
print("2. tc2.txt (Alun-alun Bandung)")
print("3. tc3.txt (Kecamatan Buahbatu, Bandung)")
print("4. tc4.txt (Kecamatan Tanjungpandan, Belitung)")
print("5. tc5.txt (Blitar)")
print("6. tc6.txt (Monas)")
print("")
print("> ",end='')

namafile = input()

namafile = "../test/tc" + namafile + ".txt"
f = open(namafile,"r")

# Baca file dan masukkan ke variabel
txtlines = f.readlines()
f.close()

# Cari dan masukkan seluruh node pada peta ke variabel node
# data_node berisi nama, koordinat x, dan koordinat y dari nama
# node berisi nama node

jmlNode = int(txtlines[0])

data_node_temp = []
data_node = []
node = []
i = 1

for i in range(1,jmlNode+1):
    data_node_temp = txtlines[i].split()
    data_node.append(data_node_temp)
    node.append(data_node[i-1][0])

# Buat weighted graph dalam representasi matrix

graf = []
graf_elemen = []
i = jmlNode + 1
for i in range(jmlNode+1,jmlNode+1+jmlNode):
    j = 0
    for eachchar in txtlines[i]:
        if eachchar != ' ':
            graf_elemen.append(0)
            if eachchar == '1':
                graf_elemen[j] = 1
            j += 1
    graf.append(graf_elemen)
    graf_elemen = []

# Telah dibentuk suatu matriks ketetanggaan
# Matriks ketetanggaan akan dikonversi ke graf

graph = g.Graph()
jarak = 0

print("\n\nList lokasi:")
for i in range(jmlNode):
    print(str(i+1) + ". " + node[i])
    
print("\n\nSilahkan pilih nomor lokasi start dari lokasi yang tersedia dalam list!")
print("> ",end='')
startNode = int(input()) - 1
print("\n\nSilahkan pilih nomor lokasi tujuan dari lokasi yang tersedia dalam list!")
print("> ",end='')
endNode = int(input()) - 1

for i in range(jmlNode):
    for j in range(jmlNode):
        if (graf[i][j] == 1):
            jarak = Jarak2Node(float(data_node[i][1]),float(data_node[j][1]),float(data_node[i][2]),float(data_node[j][2])) * 100000
            graph.connect(node[i],node[j],jarak)
 
heuristics = {}
for i in range(jmlNode):
    heuristics[node[i]] = Jarak2Node(float(data_node[i][1]),float(data_node[endNode][1]),float(data_node[i][2]),float(data_node[endNode][2]))
 
path = astar(graph, heuristics, node[startNode], node[endNode])
print("Ini adalah jalan dari ",end='')
print(node[startNode],end=' ')
print("ke ",end='')
print(node[endNode])
print(path)
print()