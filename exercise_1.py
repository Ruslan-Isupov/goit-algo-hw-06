import networkx as nx
import matplotlib.pyplot as plt
from data import graph


G = nx.DiGraph()

for src, neighbors in graph.items():
    for dest, weight in neighbors.items():
        G.add_edge(src, dest, weight=weight)

# Аналіз графа
avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()



print(f"Number_of_nodes: {G.number_of_nodes()}")
print(f"Number_of_edges : {G.number_of_edges()}")
print(f"Nodes_degree: {dict(G.degree())}")
print(f"Average_degree: {avg_degree}")

pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Graph")
plt.show()