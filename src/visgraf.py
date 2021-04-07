import networkx as nx
import matplotlib.pyplot as plt

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