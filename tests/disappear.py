import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance

class TransparentImageApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Image Transparency Animation")
        
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        
        self.label = tk.Label(root, image=self.tk_image)
        self.label.pack()
        
        self.alpha = 1.0
        self.fade_out()

    def fade_out(self):
        if self.alpha > 0:
            self.alpha -= 0.01
            self.update_image()
            self.root.after(50, self.fade_out)
        else:
            self.label.config(image='')

    def update_image(self):
        enhancer = ImageEnhance.Brightness(self.image)
        faded_image = enhancer.enhance(self.alpha)
        self.tk_image = ImageTk.PhotoImage(faded_image)
        self.label.config(image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = TransparentImageApp(root, "./tests/ball1.png")
    root.mainloop()