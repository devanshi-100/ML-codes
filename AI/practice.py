class Node:
    def  __init__(self,name):
        self.name=name
        self.edges=[]
    def add_edge(self,edge):
        self.edges.append(edge)
    def __repr__(self):
        return f"Nodes({self.name})"

class Edge:
    def __init__(self,source,target,relation):
        


