# explore Tkinter transparency (simplified)
import time
try:
    # Python2
    import tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()

# use opacity alpha values from 0.0 to 1.0
# opacity/tranparency applies to image and frame
def appear(event):
    alpha = 0
    for _ in range(10):
        root.wm_attributes('-alpha', alpha)
        time.sleep(0.1)
        alpha += 0.1
    # use a GIF image you have in the working directory
    # or give full path

photo = tk.PhotoImage(file=r"C:\Users\hkour\Documents\Projects\PostIt\tests\ball1.png")

label = tk.Label(root, image=photo).pack()
label.bind("<Button-1>", appear)



root.mainloop()