import tkinter as tk
from mainmenu import MainMenu

# Configure root window
root = tk.Tk()
root.geometry('800x700')
root.title('Post It')

# Create root menu
canvas = tk.Canvas(root, width=800, height=700, bg='steelblue', highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Create root menu
MainMenu(root, canvas)
root.mainloop()
