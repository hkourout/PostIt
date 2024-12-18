import tkinter as tk
import random
from editpostit import EditPostIt
from PIL import Image, ImageTk

IMAGES_PATH = "images/"
ANGLES_IMG = [-2, -1, 0, 1, 2]
class CreateCanvasObj(object):
    def __init__(self, root, canvas, image_name, image_format, xpos, ypos, db):
        self.root = root
        self.canvas = canvas
        self.image_name = image_name
        self.image_format = image_format
        self.xpos, self.ypos = xpos, ypos
        self.db = db

        self.alpha = 0  # Start with fully transparent
        self.image_with_alpha = Image.open("{}{}".format(IMAGES_PATH, image_name+image_format)).convert("RGBA")
        #self.image_with_alpha = self.tk_image.copy()
        self.angle = random.choice(ANGLES_IMG)
        self.fade_in()
        self.move_flag = False


    def fade_in(self):
        if self.alpha < 255:
            self.alpha += 10  # Increase opacity
            self.image_with_alpha.putalpha(self.alpha)
            self.tk_image = ImageTk.PhotoImage(self.image_with_alpha.rotate(self.angle))
            #self.canvas.config(image=self.tk_image)
            self.image_obj = self.canvas.create_image(self.xpos, self.ypos, image=self.tk_image, tags=self.image_name)
            #self.image_obj= canvas.create_image(xpos, ypos, image=self.tk_image)
            self.canvas.after(50, self.fade_in)  # Repeat after 50ms
        else:
            #self.tk_image = tk.PhotoImage(file="{}{}".format(IMAGES_PATH, self.image_name+self.image_format))
            #self.image_obj = self.canvas.create_image(self.xpos, self.ypos, image=self.tk_image)
            self.canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
            self.canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
            self.canvas.tag_bind(self.image_obj, '<Double-Button-1>', self.edit_post_it)
                

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