import tkinter as tk

def drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=400)
canvas1.pack()

canvas2 = tk.Canvas(root, width=400, height=400)
canvas2.pack()

rect1 = canvas1.create_rectangle(10, 10, 50, 50, fill="blue")

canvas1.tag_bind(rect1, "<Button-1>", drag_start)
canvas1.tag_bind(rect1, "<B1-Motion>", drag_motion)

rect2 = canvas2.create_rectangle(10, 10, 50, 50, fill="red")

canvas2.tag_bind(rect2, "<Button-1>", drag_start)
canvas2.tag_bind(rect2, "<B1-Motion>", drag_motion)

root.mainloop()