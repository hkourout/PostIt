import tkinter as tk
from PIL import Image, ImageTk
 
 
class MainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.bind("<Configure>", self.resize)
        self.img = ImageTk.PhotoImage(
            Image.open("ball1.png")
        )
        self.canvas_img = self.canvas.create_image(0, 0, anchor="nw", image=self.img)
 
    def resize(self, event):
        img = Image.open("ball1.png").resize(
            (event.width, event.height), Image.ANTIALIAS
        )
        self.img = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.canvas_img, image=self.img)
 
 
if __name__ == "__main__":
    main_frame = MainFrame()
    main_frame.mainloop()