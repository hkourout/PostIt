import tkinter as tk
import constants
import canvasobject
import uuid
import random

from tkinter import messagebox, Text, ttk, N, S, E, W
from tkinter.colorchooser import askcolor
from tkfontchooser import askfont
from tkcalendar import Calendar
from PIL import ImageGrab, Image, ImageTk
from loadpostit import LoadPostIt

TODAY_DATE = constants.TODAY_DATE
SIZES = [300, 325, 350, 375, 400]

class NewPostIt:
    def __init__(self, root, canvas, db):
        #def open_self.new():
        # Create secondary (or popup) window.
        self.root = root
        self.new = tk.Toplevel(self.root)
        self.new.wm_transient(root)

        self.canvas = canvas
        self.db = db
        self.color = constants.WHITE_COLOR
        self.font = constants.BRUSH_FONT
        self.width = random.choice(SIZES)
        self.height = random.choice(SIZES)
        self.image = str(uuid.uuid4())

        self.new.title("New Post It")
        self.new.geometry("400x300+0+0")
        #self.new.config(width=300, height=200)

        self.new.f1_style = ttk.Style()
        self.new.f1_style.configure('My.TFrame', background='#e0e0e0')
        self.new.f1 = ttk.Frame(self.new, style='My.TFrame', padding=(3, 3, 12, 12))  # added padding
        #self.new.f1 = Text(self.new, background='#334353')  # added padding

        self.new.f1.grid(column=0, row=0, sticky=(N, S, E, W))  # added sticky
        #self.new.message = ttk.Frame(self.new.f1, borderwidth=5, relief="sunken", width=200, height=100)
        self.new.message = Text(self.new.f1, foreground=constants.BLACK_COLOR, background=self.color, borderwidth=5, relief="sunken", width=30, height=15)
        self.new.author_label = ttk.Label(self.new.f1, text="Author")
        self.new.author_entry = ttk.Entry(self.new.f1)

        self.new.color = ttk.Button(self.new.f1, text="Color", command=self.change_color)
        self.new.style = ttk.Button(self.new.f1, text="Style", command=self.change_font)
        self.new.date = ttk.Button(self.new.f1, text=f"{TODAY_DATE}", command=self.change_date)
        self.new.ok = ttk.Button(self.new.f1, text="Ok", command=self.create_postit)
        self.new.cancel = ttk.Button(self.new.f1, text="Cancel", command=self.new.destroy)

        self.new.f1.grid(column=0, row=0, sticky=(N, S, E, W))  # added sticky
        self.new.message.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))  # added sticky
        self.new.author_label.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)  # added sticky, padx
        self.new.author_entry.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)  # added sticky, pady, padx
        self.new.color.grid(column=0, row=3)
        self.new.style.grid(column=1, row=3)
        self.new.date.grid(column=2, row=3)
        self.new.ok.grid(column=3, row=3)
        self.new.cancel.grid(column=3, row=4)

        # added resizing configs
        self.new.columnconfigure(0, weight=1)
        self.new.rowconfigure(0, weight=1)
        self.new.f1.columnconfigure(0, weight=3)
        self.new.f1.columnconfigure(1, weight=3)
        self.new.f1.columnconfigure(2, weight=3)
        self.new.f1.columnconfigure(3, weight=1)
        self.new.f1.columnconfigure(4, weight=1)
        self.new.f1.rowconfigure(1, weight=1)

    def change_color(self):
        colors = askcolor(title="Color Chooser")
        print(colors)
        if colors[1]:
            self.color = colors[1]
        else:
            self.color = constants.WHITE_COLOR
        self.new.message.config(bg=self.color)
        self.new.message.update_idletasks()
        print(self.color)

    def change_font(self):
        # open the font chooser and get the font selected by the user
        font = askfont()
        # font is "" if the user has cancelled
        if font:
            # spaces in the family name need to be escaped
            font['family'] = font['family'].replace(' ', '\\ ')
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
            if font['underline']:
                font_str += ' underline'
            if font['overstrike']:
                font_str += ' overstrike'
            self.font = font_str
        else:
            self.font=constants.BRUSH_FONT
        print(self.font)
        self.new.message.config(font=self.font)
        self.new.message.update_idletasks()


    def change_date(self):
        top = tk.Toplevel(self.new)
        cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", 
                       year=int(constants.TODAY_YEAR), month=int(constants.TODAY_MONTH), day=int(constants.TODAY_DAY))
        cal.pack(pady = 5)
        cal.pack(fill="both", expand=True)

        def cal_done():
            top.withdraw()
            date = cal.selection_get()
            self.new.date.config(text=date)
            print(date)
            
        ttk.Button(top, text="Ok", command=cal_done).pack(pady = 5)

    def create_postit(self):
        author = self.new.author_entry.get()
        message = self.new.message.get("1.0",tk.END).strip()
        date = self.new.date.cget("text")
        image = self.image
        font = self.font
        color = self.color
        width = self.width
        height = self.height
        x_pos = self.new.message.winfo_width()
        y_pos = self.new.message.winfo_height()
        print("author: ", "~"+author+"~")
        print("message: ", "~"+message+"~")
        print("font: ", "~"+font+"~")
        print("date: ", "~"+date+"~")
        print("color: ", "~"+color+"~")
        print("image: ", image)
        print("width: ", width)
        print("height: ", height)
        print("x_pos: ", x_pos)
        print("y_pos: ", y_pos)

        if not author:
            messagebox.showerror("Invalid Input", "Please enter Author name.")

        if not message:
            messagebox.showerror("Invalid Input", "Please write a message, a posit it can't be empty")

        if author and message:
            self.new.message.delete('1.0', 'end')
            self.new.message.insert('1.0', f'{author} ({date})\n\n{message}')
            self.new.message.update_idletasks()
            #message = self.new.message.get("1.0",tk.END).strip()
            self.capture(self.new.message, self.image, "png", width, height)
            self.db.insert((author, message, font, date, color, image, str(x_pos)+" "+str(y_pos), str(width)+" "+str(height), ""))
            #canvasobject.CreateCanvasObj(self.root, self.canvas, image, ".png", x_pos, y_pos, self.db)
            self.load_post_it()
            self.new.destroy()
                
    def load_post_it(self):
        self.canvas.delete("all")
        LoadPostIt(self.root, self.canvas, self.db)

    def capture(self, widget, file_name, file_format, width, height):
        """Take screenshot of the passed widget"""
        
        self.root.update_idletasks()
        self.new.update_idletasks()
        widget.update_idletasks()

        x0 = widget.winfo_rootx() #+ 10
        y0 = widget.winfo_rooty() #+ 15
        x1 = x0 + widget.winfo_width()
        y1 = y0 + widget.winfo_height()
        
        print("self.root.winfo_rootx() :", self.root.winfo_rootx() )
        print("self.root.winfo_rooty() :", self.root.winfo_rooty() )
        
        print("self.canvas.winfo_rootx() :", self.canvas.winfo_rootx() )
        print("self.canvas.winfo_rooty() :", self.canvas.winfo_rooty() )
        
        print("self.new.winfo_rootx() :", self.new.winfo_rootx() )
        print("self.new.winfo_rooty() :", self.new.winfo_rooty() )
        
        print("widget.winfo_rootx() :", widget.winfo_rootx() )
        print("widget.winfo_rooty() :", widget.winfo_rooty() )
        
        print("widget.winfo_width() :", widget.winfo_width() )
        print("widget.winfo_height() :", widget.winfo_height() )
        
        
        #x0 = self.new.winfo_rootx() + widget.winfo_rootx() + 15
        #y0 = self.new.winfo_rooty() + widget.winfo_rooty() + 15
        #x1 = x0 + self.new.winfo_width() + widget.winfo_width() - 170
        #y1 = y0 + self.new.winfo_height() + widget.winfo_height() - 90
        
        print("x1-x0: ",x1-x0)
        print("y1-y0: ",y1-y0)
        img = ImageGrab.grab(bbox=(x0, y0, x1, y1)) # bbox means boundingbox, which is shown in the image below
        img.save(f'images/{file_name}_tmp.{file_format}')  # Can also say im.show() to display it
        img = Image.open(f'images/{file_name}_tmp.{file_format}')
        new_img = img.resize((width, height))
        new_img.save(f'images/{file_name}.{file_format}')
