import tkinter as tk
import constants
import canvasobject
from tkinter import messagebox, Text, ttk, N, S, E, W
from tkinter.colorchooser import askcolor
from tkfontchooser import askfont
from tkcalendar import Calendar

COLOR = constants.WHITE_COLOR
FONT = constants.BRUSH_FONT
TODAY_DATE = constants.TODAY_DATE

class NewPostIt:
    def __init__(self, root, canvas):
        #def open_self.new():
        # Create secondary (or popup) window.
        self.new = tk.Toplevel(root)
        self.canvas = canvas

        self.new.title("New Post It")
        self.new.geometry("400x300+300+200")
        self.new.config(width=300, height=200)

        self.new.f1_style = ttk.Style()
        self.new.f1_style.configure('My.TFrame', background='#e0e0e0')
        self.new.f1 = ttk.Frame(self.new, style='My.TFrame', padding=(3, 3, 12, 12))  # added padding
        #self.new.f1 = Text(self.new, background='#334353')  # added padding

        self.new.f1.grid(column=0, row=0, sticky=(N, S, E, W))  # added sticky
        #self.new.message = ttk.Frame(self.new.f1, borderwidth=5, relief="sunken", width=200, height=100)
        self.new.message = Text(self.new.f1, foreground=constants.BLACK_COLOR, background=COLOR, borderwidth=5, relief="sunken", width=30, height=15)
        self.new.author_label = ttk.Label(self.new.f1, text="Author")
        self.new.author_entry = ttk.Entry(self.new.f1)

        self.new.color = ttk.Button(self.new.f1, text="Color", command=self.change_color)
        self.new.style = ttk.Button(self.new.f1, text="Style", command=self.change_font)
        self.new.date = ttk.Button(self.new.f1, text="Date", command=self.change_date)
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
        COLOR = colors[1]
        self.new.message.config(bg=COLOR)
        print(COLOR)

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
            FONT = font_str
        print(FONT)
        self.new.message.config(font=FONT)

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
        print("author: ", "~"+author+"~")
        print("message: ", "~"+message+"~")
        print("date: ", "~"+date+"~")
        if not author:
            messagebox.showerror("Invalid Input", "Please enter Author name.")

        if not message:
            messagebox.showerror("Invalid Input", "Please write a message, a posit it can't be empty")

        if not date:
            date = constants.TODAY_DATE

        if author and message:
            self.new.message.insert(tk.END, f"\n\n{author}\n({date})\n")
            canvasobject.CreateCanvasObj(self.canvas, "ball1.png", 100, 100)
            self.new.destroy()
