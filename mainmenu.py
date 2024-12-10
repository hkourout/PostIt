from tkinter import Menu
#from new import open_new_window
from newpostit import NewPostIt

class MainMenu:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas

        # create a menubar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )

        def new_post_it():
            NewPostIt(self.root, self.canvas)

        # add menu items to the File menu
        file_menu.add_command(label='New', underline=0, command=new_post_it)
        file_menu.add_command(label='Open', underline=0)
        file_menu.add_command(label='Find', underline=0)
        file_menu.add_separator()

        # add a submenu
        sub_menu = Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Author')
        sub_menu.add_command(label='Date')
        sub_menu.add_command(label='Categorie')

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
