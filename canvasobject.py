import tkinter as tk
from editpostit import EditPostIt

IMAGE_PATH = "images/"

class CreateCanvasObj(object):
    def __init__(self, root, canvas, image_name, image_format, xpos, ypos, db):
        self.root = root
        self.canvas = canvas
        self.image_name = image_name
        self.image_format = image_format
        self.xpos, self.ypos = xpos, ypos
        self.db = db
 
        self.tk_image = tk.PhotoImage(file="{}{}".format(IMAGE_PATH, image_name+image_format))
        self.image_obj= canvas.create_image(xpos, ypos, image=self.tk_image)
         
        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        canvas.tag_bind(self.image_obj,'<Double-Button-1>', self.edit_post_it)

        self.move_flag = False
         
    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y
             
            self.canvas.move(self.image_obj,
                new_xpos-self.mouse_xpos ,new_ypos-self.mouse_ypos)
             
            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
            print("New canvas pos : ", self.mouse_xpos, self.mouse_ypos)
            self.db.update(self.image_name,"position", str(self.mouse_xpos)+" "+str(self.mouse_ypos))
        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y

    def release(self, event):
        self.move_flag = False

    def edit(self, event):
        print("Double clicked!! ", event.x, event.y)

    def edit_post_it(self, event):
        EditPostIt(self.root, self.canvas, self.db, self.image_name)