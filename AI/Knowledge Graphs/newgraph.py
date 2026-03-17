"""
KNOWLEDGE GRAPH with Wikipedia Scraping
Improved India Example (Debug + Looser Filter)
"""
import requests
from bs4 import BeautifulSoup
import re
import spacy
import networkx as nx
import matplotlib.pyplot as plt

# ------------------ Node, Edge, KG ------------------
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
    def add_edge(self, edge):
        self.edges.append(edge)
    def __repr__(self):
        return f"Node({self.name})"

class Edge:
    def __init__(self, source, target, relation):
        self.source = source
        self.target = target
        self.relation = relation
    def __repr__(self):
        return f"({self.source.name}) -[{self.relation}]-> ({self.target.name})"

class KG:
    def __init__(self, name):
        self.name = name
        self.nodes = {}
    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
        return self.nodes[name]
    def add_relation(self, source_name, target_name, relation):
        source = self.add_node(source_name)
        target = self.add_node(target_name)
        edge = Edge(source, target, relation)
        source.add_edge(edge)
    def display(self):
        print(f"\n--- {self.name} ---")
        for node in self.nodes.values():
            for edge in node.edges:
                print(edge)

# ------------------ Scraping ------------------
def scrape_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = [p.get_text() for p in soup.select("p") if p.get_text().strip()]
    text = " ".join(paragraphs[:10])  # take first 10 paragraphs
    text = re.sub(r"\[\d+\]", "", text)  # remove references like [1]
    return text

# ------------------ NLP Entity + Relation Extraction ------------------
def extract_relations(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    print("\n🔎 Named Entities Found:", [(ent.text, ent.label_) for ent in doc.ents])

    relations = []
    india = "India"

    # Looser filter → take all entities (except "India")
    for ent in doc.ents:
        if ent.text.strip() and ent.text.lower() != "india":
            relations.append((india, ent.text, f"entity:{ent.label_}"))

    # Extract simple subject-verb-object triples
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "ROOT":  # main verb
                subj = [w.text for w in token.lefts if w.dep_ in ("nsubj","nsubjpass")]
                obj = [w.text for w in token.rights if w.dep_ in ("dobj","attr","pobj")]
                if subj and obj:
                    relations.append((subj[0], obj[0], token.lemma_))

    relations = list(set(relations))  # deduplicate
    return relations

# ------------------ Visualization ------------------
def visualize_kg(relations):
    G = nx.DiGraph()
    for s, t, r in relations:
        G.add_edge(s, t, label=r)

    pos = nx.spring_layout(G, k=0.5)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=9, arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("India Knowledge Graph", fontsize=14)
    plt.show()

# ------------------ Driver Code ------------------
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/India"

    print("Scraping Wikipedia page...")
    text = scrape_wikipedia(url)
    print("\n📄 Scraped text preview:\n", text[:500], "\n")

    print("Extracting relations...")
    relations = extract_relations(text)

    print(f"\n✅ Found {len(relations)} relations.\n")
    graph = KG("India Knowledge Graph")
    for s, t, r in relations:
        graph.add_relation(s, t, r)

    graph.display()
    visualize_kg(relations)
