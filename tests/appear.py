import tkinter as tk
from PIL import Image, ImageTk

class TransparentImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transparent Image Animation")
        
        # Load the image
        self.image = Image.open("./tests/ball1.png").convert("RGBA")
        self.alpha = 0  # Start with fully transparent
        self.image_with_alpha = self.image.copy()
        
        # Create a label to display the image
        self.label = tk.Label(root)
        self.label.pack()
        
        # Start the animation
        #self.fade_in()
        
        self.alpha = 255  # Start with fully transparent
        self.image_with_alpha = self.image.copy()
        self.fade_out()

    def fade_in(self):
        if self.alpha < 255:
            self.alpha += 5  # Increase opacity
            self.image_with_alpha.putalpha(self.alpha)
            self.tk_image = ImageTk.PhotoImage(self.image_with_alpha)
            self.label.config(image=self.tk_image)
            self.root.after(50, self.fade_in)  # Repeat after 50ms


    def fade_out(self):
        if self.alpha > 0:
            self.alpha -= 5
            self.image_with_alpha.putalpha(self.alpha)
            self.tk_image = ImageTk.PhotoImage(self.image_with_alpha)
            self.label.config(image=self.tk_image)
            self.root.after(50, self.fade_out)

if __name__ == "__main__":
    root = tk.Tk()
    app = TransparentImageApp(root)
    root.mainloop()
