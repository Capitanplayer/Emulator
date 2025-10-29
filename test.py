import tkinter as tk

class ScrollableTextBoxes:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrollable List of Text Boxes")

        # Create a Frame for the Canvas and Scrollbar
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create a Canvas
        self.canvas = tk.Canvas(frame)
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure Canvas and Scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create a Frame inside the Canvas
        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Add multiple Text boxes to the inner frame
        for i in range(20):
            text_box = tk.Text(self.inner_frame, height=5, width=40)
            text_box.pack(pady=5)

# Create the main application window
root = tk.Tk()
app = ScrollableTextBoxes(root)
root.geometry("300x400")  # Set initial window size
root.mainloop()