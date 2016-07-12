__author__ = 'Geetika'


class Graph(object):
    nodes = {}
    no_of_vertices = 0
    no_of_edges = 0

    def __init__(self):
        pass

    def add_node(self, node):
        if node.id not in self.nodes:
            self.update_vertices_count()
            self.nodes[node.id] = node

    def add_edge(self, fromNode, toNode):
        if fromNode.id not in self.nodes:
            self.update_vertices_count()
            self.nodes[fromNode.id] = fromNode
        if toNode.id not in self.nodes:
            self.update_vertices_count()
            self.nodes[toNode.id] = toNode
        self.nodes[toNode.id].add_neighbor(self.nodes[fromNode.id])
        self.nodes[fromNode.id].add_neighbor(self.nodes[toNode.id])

    def update_vertices_count(self, incr=1):
        self.no_of_vertices += incr

    def update_edge_count(self):
        self.no_of_edges += 1

    def get_node(self, id):
        if id in self.nodes:
            return self.nodes[id]
        return

    def get_vertices(self):
        return self.nodes

    def set_node(self, node):
        self.nodes[node.id] = node

    def remove_edge(self, frm, to):
        if frm.id in self.nodes:
            result = self.nodes[frm.id].find_neighbor(to.id)
            if(result):
                self.nodes[frm.id].remove_neighbor(to.id)
                self.nodes[to.id].remove_neighbor(frm.id)
            
            if not self.nodes[frm.id].has_neighbors():
                self.remove_node(frm.id)

            if not self.nodes[to.id].has_neighbors():
                self.remove_node(to.id)

    def __str__(self):
        output = ""
        for node in self.nodes:
            output += str(self.nodes[node]) + "\n"
        return "[graph]: {" + output + "}"

    def remove_node(self, id):
        del self.nodes[id]