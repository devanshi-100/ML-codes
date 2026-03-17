'''
KNOWLEDGE GRAPH
'''
class Node:
    def __init__(self,name):
        self.name=name
        self.edges=[]
    def add_edge(self,edge):
        self.edges.append(edge)
    def __repr__(self):
        return f"Node({self.name})"   #///wrapper function


class Edge:
    def __init__(self,source,target,relation):
        self.source=source
        self.target=target
        self.relation=relation
    def __repr__(self):
        return f"({self.source.name}) -[{self.relation}]-> ({self.target.name})"   #///wrapper function

class KG:
    def __init__(self,name):
        self.name=name
        self.nodes={}
    def add_node(self,name):
        if name not in self.nodes:
            self.nodes[name]=Node(name)
        return self.nodes[name]
    def add_relation(self,source_name,target_name,relation):
        source=self.add_node(source_name)
        target=self.add_node(target_name)
        edge=Edge(source,target,relation)
        source.add_edge(edge)
    def display(self):
        print(f"--- {self.name} ---")
        for node in self.nodes.values():
            for edge in node.edges:
                print(edge)

# //this is a driver code
if __name__=="__main__":
    graph=KG('Family Tree')    #this will make an empty K graph
    graph.add_relation('A','B','father of')
    graph.add_relation('B','C','sibling of')
    graph.add_relation('D','C','mother of')

    graph.display()






        
    













