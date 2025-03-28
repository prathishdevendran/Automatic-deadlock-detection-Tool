import tkinter as tk
from tkinter import filedialog, messagebox

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lightblue")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set window width and height
    window_width = 400
    window_height = 300

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    app = DeadlockGUI(root)
    root.mainloop()
