import tkinter as tk
import constants
import canvasobject
import uuid
import random
import os
import glob

from tkinter import messagebox, Text, ttk, N, S, E, W
from tkinter.colorchooser import askcolor
from tkfontchooser import askfont
from tkcalendar import Calendar
from PIL import ImageGrab, Image, ImageTk
from loadpostit import LoadPostIt

TODAY_DATE = constants.TODAY_DATE
#SIZES = [300, 325, 350, 375, 400]

IMAGES_PATH = "images/"

class EditPostIt:
    def __init__(self, root, canvas, db, image):
        #def open_self.edit():
        # Create secondary (or popup) window.
        self.root = root
        self.edit = tk.Toplevel(self.root)
        self.edit.wm_transient(root)

        self.canvas = canvas
        self.db = db
        self.image = image
        
        self.edit.title("Update Post It")
        #self.edit.geometry("400x300+300+200")
        self.edit.geometry("400x300+0+0")
        #self.edit.config(width=300, height=200)

        row = self.db.retrieve_value_of_key("image", self.image)
        print("ROW", row)
        self.width = int(row[0]["angle"].split()[0])
        self.height = int(row[0]["angle"].split()[1])
        
        self.x_pos = int(row[0]["position"].split()[0])
        self.y_pos = int(row[0]["position"].split()[1])

        self.color = row[0]["color"]
        self.font = row[0]["style"]

        self.edit.f1_style = ttk.Style()
        self.edit.f1_style.configure('My.TFrame', background='#e0e0e0')
        self.edit.f1 = ttk.Frame(self.edit, style='My.TFrame', padding=(3, 3, 12, 12))  # added padding
        #self.edit.f1 = Text(self.edit, background='#334353')  # added padding

        self.edit.f1.grid(column=0, row=0, sticky=(N, S, E, W))  # added sticky
        #self.edit.message = ttk.Frame(self.edit.f1, borderwidth=5, relief="sunken", width=200, height=100)
        self.edit.message = Text(self.edit.f1, foreground=constants.BLACK_COLOR, background=self.color, borderwidth=5, relief="sunken", width=30, height=15)
        self.edit.author_label = ttk.Label(self.edit.f1, text="Author")
        self.edit.author_entry = ttk.Entry(self.edit.f1)

        self.edit.color = ttk.Button(self.edit.f1, text="Color", command=self.change_color)
        self.edit.style = ttk.Button(self.edit.f1, text="Style", command=self.change_font)
        self.edit.date = ttk.Button(self.edit.f1, text=f"{TODAY_DATE}", command=self.change_date)
        self.edit.ok = ttk.Button(self.edit.f1, text="Update", command=self.update_postit)
        self.edit.delete = ttk.Button(self.edit.f1, text="Delete", command=self.delete_postit)
        self.edit.cancel = ttk.Button(self.edit.f1, text="Cancel", command=self.edit.destroy)

        self.edit.f1.grid(column=0, row=0, sticky=(N, S, E, W))  # added sticky
        self.edit.message.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))  # added sticky
        self.edit.author_label.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)  # added sticky, padx
        self.edit.author_entry.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)  # added sticky, pady, padx
        self.edit.color.grid(column=0, row=3)
        self.edit.style.grid(column=1, row=3)
        self.edit.date.grid(column=2, row=3)
        self.edit.ok.grid(column=3, row=2)
        self.edit.delete.grid(column=3, row=3)
        self.edit.cancel.grid(column=3, row=4)

        # added resizing configs
        self.edit.columnconfigure(0, weight=1)
        self.edit.rowconfigure(0, weight=1)
        self.edit.f1.columnconfigure(0, weight=3)
        self.edit.f1.columnconfigure(1, weight=3)
        self.edit.f1.columnconfigure(2, weight=3)
        self.edit.f1.columnconfigure(3, weight=1)
        self.edit.f1.columnconfigure(4, weight=1)
        self.edit.f1.rowconfigure(1, weight=1)

        self.edit.message.insert('1.0', row[0]["message"])
        self.edit.message.update_idletasks()
        
        self.edit.author_entry.insert(0, row[0]["author"])
        self.edit.author_entry.update_idletasks()

        self.edit.message.config(bg=row[0]["color"])
        self.edit.message.config(font=row[0]["style"])
        self.edit.message.update_idletasks()

        self.edit.date.config(text=row[0]["date"])
        self.edit.date.update_idletasks()



    def change_color(self):
        colors = askcolor(title="Color Chooser")
        print(colors)
        if colors[1]:
            self.color = colors[1]
        else:
            self.color = constants.WHITE_COLOR
        self.edit.message.config(bg=self.color)
        self.edit.message.update_idletasks()
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
        self.edit.message.config(font=self.font)
        self.edit.message.update_idletasks()


    def change_date(self):
        top = tk.Toplevel(self.edit)
        cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", 
                       year=int(constants.TODAY_YEAR), month=int(constants.TODAY_MONTH), day=int(constants.TODAY_DAY))
        cal.pack(pady = 5)
        cal.pack(fill="both", expand=True)

        def cal_done():
            top.withdraw()
            date = cal.selection_get()
            self.edit.date.config(text=date)
            print(date)
            
        ttk.Button(top, text="Ok", command=cal_done).pack(pady = 5)

    def update_postit(self):
        author = self.edit.author_entry.get()
        message = self.edit.message.get("1.0",tk.END).strip()
        date = self.edit.date.cget("text")
        image = self.image
        font = self.font
        color = self.color
        width = self.width
        height = self.height
        x_pos = self.x_pos
        y_pos = self.y_pos
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
            self.edit.message.delete('1.0', 'end')
            self.edit.message.insert('1.0', f'{author} ({date})\n\n{message}')
            self.edit.message.update_idletasks()
            #message = self.edit.message.get("1.0",tk.END).strip()
            self.capture(self.edit.message, image, "png", width, height)
            
            self.db.update(image,"author", author)
            self.db.update(image,"message", message)
            self.db.update(image,"style", font)
            self.db.update(image,"date", date)
            self.db.update(image,"color", color)
            self.db.update(image,"position", str(x_pos)+" "+str(y_pos))
            self.db.update(image,"angle", str(width)+" "+str(height))
            self.canvas.delete(self.image)
            self.edit.destroy()
            canvasobject.CreateCanvasObj(self.root, self.canvas, image, ".png", x_pos, y_pos, self.db)
            #self.load_post_it()
            
    
    def load_post_it(self):
        self.canvas.delete(self.image)
        LoadPostIt(self.root, self.canvas, self.db)
        self.edit.destroy()
        
    def delete_postit(self):
        MsgBox = messagebox.askquestion ('Delete?', 'Are you sure you want to delete this post it?',icon = 'warning')
        if MsgBox == 'yes':
            # Your code
            self.canvas.delete(self.image)
            self.alpha = 255  # Start with fully transparent
            self.image_with_alpha = Image.open("{}{}".format(IMAGES_PATH, self.image+".png")).convert("RGBA")
            #self.image_with_alpha = self.tk_image.copy()
            self.edit.destroy()
            self.fade_out()


    def fade_out(self):
        if self.alpha > 0:
            self.alpha -= 10
            self.image_with_alpha.putalpha(self.alpha)
            self.tk_image = ImageTk.PhotoImage(self.image_with_alpha)
            self.canvas.create_image(self.x_pos, self.y_pos, image=self.tk_image, tags=self.image)
            self.canvas.after(50, self.fade_out)
        else:
            for f in glob.glob(f"{IMAGES_PATH}/{self.image}*"):
                os.remove(f)
            print(f"Posit it {self.image} deleted!")
            #self.load_post_it()
            self.db.delete(self.image)

            
    def capture(self, widget, file_name, file_format, width, height):
        """Take screenshot of the passed widget"""

        x0 = widget.winfo_rootx() #+ 10
        y0 = widget.winfo_rooty() #+ 15
        x1 = x0 + widget.winfo_width()
        y1 = y0 + widget.winfo_height()

        #x0 = self.edit.winfo_rootx() + widget.winfo_rootx() + 15
        #y0 = self.edit.winfo_rooty() + widget.winfo_rooty() + 15
        #x1 = x0 + self.edit.winfo_width() + widget.winfo_width() - 170
        #y1 = y0 + self.edit.winfo_height() + widget.winfo_height() - 90
        
        print("x1-x0: ",x1-x0)
        print("y1-y0: ",y1-y0)
        img = ImageGrab.grab(bbox=(x0, y0, x1, y1)) # bbox means boundingbox, which is shown in the image below
        img.save(f'images/{file_name}_tmp.{file_format}')  # Can also say im.show() to display it
        img = Image.open(f'images/{file_name}_tmp.{file_format}')
        new_img = img.resize((width, height))
        new_img.save(f'images/{file_name}.{file_format}')
