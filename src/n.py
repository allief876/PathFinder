# Kelas Node
class Node:
    # Konstruktor kelas
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost

    # Pengecekan node yang sama
    def __eq__(self, other):
        return self.name == other.name

    # Sorting node
    def __lt__(self, other):
         return self.f < other.f

    # Cetak node ke layar
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))