# GUI
import networkx as nx
import tkinter as tk
from tkinter import filedialog, messagebox


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

