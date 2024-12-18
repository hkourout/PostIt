import canvasobject
from tkinter import Menu
#from new import open_new_window
from newpostit import NewPostIt
from loadpostit import LoadPostIt

class MainMenu:
    def __init__(self, root, canvas, db, search):
        self.root = root
        self.canvas = canvas
        self.db = db
        self.search = search
        self.loaded = False

        # create a menubar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )

        def new_post_it():
            disable_entry(self.search)
            NewPostIt(self.root, self.canvas, self.db)

        def load_post_it():
            if not self.loaded:
                self.canvas.delete("all")
                LoadPostIt(self.root, self.canvas, self.db)
                self.loaded = True
            disable_entry(self.search)
                
        def clear_post_it():
            self.canvas.delete("all")
            self.loaded = False
            disable_entry(self.search)
                
        def find_post_it():
            enable_entry(self.search)

        def sort_by_key(key):
            clear_post_it()
            x_pos = 400
            y_pos = 120
            for d in self.db.get_sorted_row(key):
                x_pos += 100
                y_pos += 60
                canvasobject.CreateCanvasObj(root, canvas, d["image"], ".png", x_pos, y_pos, db)

    
        # add menu items to the File menu
        file_menu.add_command(label='New', underline=0, command=new_post_it)
        file_menu.add_command(label='Load', underline=0, command=load_post_it)
        file_menu.add_command(label='Clear', underline=0, command=clear_post_it)
        file_menu.add_separator()
        file_menu.add_command(label='Find', underline=0, command=find_post_it)

        # add a submenu
        sub_menu = Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Author', command=lambda: sort_by_key("author"))
        sub_menu.add_command(label='Date', command=lambda: sort_by_key("date"))
        sub_menu.add_command(label='Color', command=lambda: sort_by_key("color"))
        sub_menu.add_command(label='Style', command=lambda: sort_by_key("style"))
        sub_menu.add_command(label='Creation', command=lambda: sort_by_key("id"))
        
        # add the File menu to the menubar
        file_menu.add_cascade(
            label="Sort",
            underline=0,
            menu=sub_menu
        )

        # add Exit menu item
        file_menu.add_separator()
        file_menu.add_command(
            label='Exit',
            underline=0,
            command=root.destroy
        )


        menubar.add_cascade(
            label="File",
            underline=0,
            menu=file_menu
        )
        # create the Help menu
        help_menu = Menu(
            menubar,
            tearoff=0
        )

        help_menu.add_command(label='Welcome', underline=0)
        help_menu.add_command(label='About', underline=0)

        # add the Help menu to the menubar
        menubar.add_cascade(
            label="Help",
            menu=help_menu,
            underline=0
        )

# def validate_combo(combo, db, root, canvas):
#     select = combo.get()
#     print("Vous avez sélectionné : '", select,"'")
    
def validate_entry(entry, db, root, canvas):
    print("Search in progress...: "+entry.get())
    canvas.delete("all")
    print(db.retrieve(entry.get()))
    for d in db.retrieve(entry.get()):
        print(d)
        x_pos = d["position"].split()[0]
        y_pos = d["position"].split()[1]
        print(d, x_pos, y_pos)
        canvasobject.CreateCanvasObj(root, canvas, d["image"], ".png", x_pos, y_pos, db)

def disable_entry(entry):
    entry.configure(state="disabled", disabledbackground="steelblue")
    
def enable_entry(entry):
    entry.configure(state="normal", disabledbackground="white")
    