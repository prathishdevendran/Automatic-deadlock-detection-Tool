# GUI
import networkx as nx
import tkinter as tk
from tkinter import filedialog, messagebox

from module1 import DeadlockDetector
from module2 import DeadlockVisualizer

class DeadlockGUI:
    def __init__(self, root):
        self.detector = DeadlockDetector()
        self.root = root
        self.root.title("Deadlock Detection Tool")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Deadlock Detection Tool",bg="lightblue", font=("Arial Bold", 14)).pack(pady=20)
        tk.Label(self.root, text="Add a log file and check for deadlocks",bg="lightblue", font=("Arial", 10)).pack(pady=20)
        tk.Button(self.root, text="Upload Process Log",bg="#afdfcf" ,width=20, height=1,command=self.load_log).pack(pady=10)
        tk.Button(self.root, text="Detect Deadlock",bg="#afdfcf", width=20, height=2,command=self.detect_deadlock).pack(pady=10)

    def load_log(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # reseting the graph and add edge
            self.detector.graph = nx.DiGraph()
            count = 0
            with open(file_path, 'r') as file:
                for line in file:
                    process, resource = line.strip().split(" -> ")
                    self.detector.add_edge(process, resource)
                    count += 1
            messagebox.showinfo("Success", f"Process log loaded successfully! {count} edges added.")

    def detect_deadlock(self):
        cycles = self.detector.detect_deadlock()
        if cycles:
            DeadlockVisualizer.display_graph(self.detector.graph, cycles)
        else:
            messagebox.showinfo("No Deadlock", "No deadlocks detected!")
