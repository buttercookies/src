__author__ = 'lawrenberg'

class Node(object):
    def __init__(self, id):
        self.id = id
        self.metadata = {}
        self.neighbors = {}
        self.weight = 1

    def add_neighbor(self, neighbor):
        if neighbor.id not in self.neighbors:
            self.neighbors[neighbor.id] = neighbor

    def get_neighbors(self):
        return self.neighbors.keys()

    def find_neightbor(self, id):
        if self.neighbors.has_key(id):
            return self.neighbors
        return

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def get_metadata(self):
        return self.metadata

    def remove_neighbor(self, neighborId):
        del self.neighbors[neighborId]

    def has_neighbor(self):
        return self.neighbor_count() > 0

    def neighbor_count(self):
        return len(self.neighbors)

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return "id: " + self.id + " adjacent: [" + str(self.get_neighbors())