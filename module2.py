#Visualize graph of processes
import networkx as nx
import matplotlib.pyplot as plt


class DeadlockVisualizer:
    @staticmethod
    def display_graph(graph, cycles):
        pos = nx.spring_layout(graph)
        plt.figure(figsize=(8, 6))

        # Mark nodes and edges involved in a deadlock
        cycle_nodes = set(node for edge in cycles for node in edge)
        cycle_edges = set(cycles)

        node_colors = ['red' if node in cycle_nodes else 'green' for node in graph.nodes()]
        edge_colors = ['red' if edge in cycle_edges else 'black' for edge in graph.edges()]

        nx.draw(graph, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=2000, font_size=10)
        plt.show()
