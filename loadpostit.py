import tkinter as tk
import constants
import canvasobject
import uuid
import random

from tkinter import messagebox, Text, ttk, N, S, E, W
from tkinter.colorchooser import askcolor
from tkfontchooser import askfont
from tkcalendar import Calendar
from PIL import ImageGrab, Image

COLOR = constants.WHITE_COLOR
FONT = constants.BRUSH_FONT
TODAY_DATE = constants.TODAY_DATE
SIZES = [300, 325, 350, 375, 400]

class LoadPostIt:
    def __init__(self, root, canvas, db):
        #def open_self.new():
        # Create secondary (or popup) window.
        self.root = root
        self.canvas = canvas
        self.db = db

        def dict_from_row(row):
            return dict(zip(row.keys(), row)) 
        
        for row in self.db.get_row():
            d = dict_from_row(row)
            x_pos = d["position"].split()[0]
            y_pos = d["position"].split()[1]
            print(d, x_pos, y_pos)
            canvasobject.CreateCanvasObj(self.root, self.canvas, d["image"], ".png", x_pos, y_pos, self.db)
