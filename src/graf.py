# Kelas graf
class Graph:
    # Konstruktor kelas
    def __init__(self, graph_dict=None):
        self.graph_dict = graph_dict or {}
    
    # Menghubungkan A dan B dengan suatu jarak
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance

    # Mendapatkan tetangga dari suatu node
    def get(self, a, b=None):
        tetangga = self.graph_dict.setdefault(a, {})
        if b is None:
            return tetangga
        else:
            return tetangga.get(b)