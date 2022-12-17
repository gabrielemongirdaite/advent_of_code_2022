import networkx as nx
import matplotlib.pyplot as plt
import re
import dijkstar
from itertools import permutations


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            ln = []
            ln.append(int(re.findall(r'-?\d+', line)[0]))
            ln.extend(re.findall('([A-Z][A-Z])', line))
            lines.append(ln)
    return lines


data = read_file('input_day16.txt')


def add_edges(graph, data):
    dct = {}
    for i in data:
        node = i[1]
        for j in i[2:]:
            graph.add_edges_from([(node, j)])
        if i[0] != 0:
            dct[i[1]] = i[0]
    return graph, dct


def draw_graph(G, val_map):
    val_map['AA'] = -10
    values = [val_map.get(node, 0.25) for node in G.nodes()]
    # Specify the edges you want here
    red_edges = []
    edge_colours = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                           node_color=values, node_size=150)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.show()
    return


G = nx.DiGraph()
G, values_map = add_edges(G,data)
draw_graph(G, values_map)

