import networkx as nx

G = nx.Graph()

edges = [
    ("Jakarta", "Cirebon", 327),
    ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 130),
    ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305),
    ("Cirebon", "Yogyakarta", 210),
    ("Yogyakarta", "Semarang", 109),
    ("Yogyakarta", "Surakarta", 97),
    ("Surakarta", "Semarang", 97),
    ("Surakarta", "Surabaya", 370),
    ("Semarang", "Surabaya", 369),
    ("Surabaya", "Malang", 94)
]

G.add_weighted_edges_from(edges)

print("Shortest Path Graf Indonesia")
for source in G.nodes:
    for target in G.nodes:
        if source != target:
            path = nx.shortest_path(G, source, target, weight='weight')
            distance = nx.shortest_path_length(G, source, target, weight='weight')
            print(f"{source} -> {target}: {path}, jarak = {distance}")