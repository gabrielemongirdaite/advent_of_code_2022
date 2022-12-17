import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('AA', 'TU'), ('AA', 'BO'), ('AA', 'CA'), ('AA', 'DM'), ('AA', 'ZJ'),
     ('TU', 'BO'), ('TU', 'DM'), ('TU', 'UK'), ('BO', 'ZJ'),
     ('BO', 'DM'), ('UK', 'EK'), ('GW', 'JT'), ('EK', 'GW'),
     ('ZJ', 'DM'), ('ZJ', 'FP'), ('ZJ', 'CA'), ('DM', 'YH'),
     ('YH', 'UX'), ('YH', 'AR'), ('YH', 'FP'), ('AR', 'UX'),
     ('AR', 'FP'), ('FP', 'CA'), ('FP', 'LE'), ('CA', 'JF'),
     ('CA', 'LE'), ('JF', 'LE')])

val_map = {'AA': 0.0,
           'TU': 11,
           'BO': 4,
           'CA': 13,
           'DM': 3,
           'ZJ': 9,
           'UK': 18,
           'EK': 19,
           'GW': 16,
           'JT': 22,
           'YH': 21,
           'AR': 20,
           'UX': 23,
           'FP': 5,
           'JF': 15,
           'LE': 14}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = []
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spiral_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color=values, node_size=150)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()
