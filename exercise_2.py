import networkx as nx
from collections import deque
from data import graph

# DFS algotithm

def dfs(graph, start, visited=None, path=None):
    result = []
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    paths = []

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, visited, path)
            for p in new_path:
                paths.append(p)

    if not paths:
        paths.append(path)
    
    for i, path in enumerate(paths):
        for j, node in enumerate(path[:-1]):
            result.append((node, path[j+1]))

    return result

dfs_result = dfs(graph, "Kyiv")
print("DfS",dfs_result)



# BFS algotithm
def bfs(graph,start):
    visited = set()
    result = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return result

bfs_result = bfs(graph, "Kyiv")
print("BFS",bfs_result)

G = nx.DiGraph()

for src, neighbors in graph.items():
    for dest, weight in neighbors.items():
        G.add_edge(src, dest, weight=weight)


dfs_edges = list(nx.dfs_edges(G,source='Kyiv'))
print("DFS_embedded",dfs_edges)
bfs_edges = list(nx.bfs_edges(G,source='Kyiv'))
print("BFS_embedded",bfs_edges)
