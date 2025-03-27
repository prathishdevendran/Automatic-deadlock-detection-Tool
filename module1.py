# deadlock_detection
import networkx as nx

class DeadlockDetector:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, process, resource):
        self.graph.add_edge(process, resource)
        
    def detect_deadlock(self):
        # print("Graph edges:", list(self.graph.edges()))
        try:
            cycles = list(nx.find_cycle(self.graph, orientation='original'))
            return cycles if cycles else None
        except nx.NetworkXNoCycle:
            return None
