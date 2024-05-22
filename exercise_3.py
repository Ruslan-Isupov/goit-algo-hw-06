import networkx as nx
import matplotlib.pyplot as plt
from data import graph


def dijkstra(graph, start):    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:     
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])    
    
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
      
            if distance < distances[neighbor]:
                distances[neighbor] = distance
   
        unvisited.remove(current_vertex)

    return distances


shortest_paths = dijkstra(graph, 'Kyiv')
print("Dijkstra", shortest_paths)

G = nx.Graph()

for node in graph:
    G.add_node(node)


for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Застосування вбудованих ф-й алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='Kyiv',weight='weight')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Kyiv', weight="weight")

print("Dijkstra_path_emb",shortest_paths) 
print("Dijkstra_path_lenght_emb",shortest_path_lengths)

