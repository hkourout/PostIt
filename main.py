import tkinter as tk
import constants
import database
from mainmenu import MainMenu, disable_entry, validate_entry #, validate_combo
from tkinter import ttk

# Configure root window
root = tk.Tk()
#root.geometry('800x700+200+200')
#getting screen width and height of display
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
#setting tkinter root size
root.geometry("%dx%d" % (width, height))
root.title('Post It')

db = database.Database(filename = constants.DATABASE_NAME, table = constants.TABLE_NAME)
db.sql_do(constants.CREATE_TABLE)

# Create root menu
#canvas = tk.Canvas(root, width=800, height=700, bg='steelblue', highlightthickness=0)
canvas = tk.Canvas(root, width=width, height=height, bg='steelblue', highlightthickness=0)
canvas.pack(fill="both", expand=True)
search = tk.Entry(canvas)

# # 2) - créer la liste Python contenant les éléments de la liste Combobox
# listeProduits=["Select", "Laptop", "Imprimante","Tablette","SmartPhone"]

# # 3) - Création de la Combobox via la méthode ttk.Combobox()
# combo = ttk.Combobox(root, values=listeProduits)

def onclick_entry(event):
    validate_entry(search, db, root, canvas)

# def onclick_combo(event):
#     validate_combo(combo, db, root, canvas)
    
search.pack(side='top', anchor='nw') #, fill="x")
search.bind('<Return>', onclick_entry)
disable_entry(search)

# combo.current(0)

# combo.pack(side='bottom', anchor='ne')
# combo.bind("<<ComboboxSelected>>", onclick_combo)

# Create root menu
MainMenu(root, canvas, db, search)
root.mainloop()
