import networkx as nx
G_directed = nx.DiGraph()
G_directed.add_edges_from([(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9)])
is_dag = nx.is_directed_acyclic_graph(G_directed)
print("Is DAG:", is_dag)