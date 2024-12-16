import tkinter as tk
import constants
import database
from mainmenu import MainMenu, disable_entry, validate_entry

# Configure root window
root = tk.Tk()
root.geometry('800x700')
root.title('Post It')

# Create root menu
canvas = tk.Canvas(root, width=800, height=700, bg='steelblue', highlightthickness=0)
search = tk.Entry(canvas)

def onclick_entry(event):
    validate_entry(search)
    
search.pack(side='top', fill="x")
search.bind('<Return>', onclick_entry)
disable_entry(search)

canvas.pack(fill="both", expand=True)

db = database.Database(filename = constants.DATABASE_NAME, table = constants.TABLE_NAME)
db.sql_do(constants.CREATE_TABLE)

# Create root menu
MainMenu(root, canvas, db, search)
root.mainloop()
