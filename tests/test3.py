import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

# Initializing Tkinter
root = TkinterDnD.Tk()
root.title("Multiple Widget Drag and Drop")
root.geometry("600x400")

# Label to drag 1
drag_label1 = tk.Label(root, text="Drag this label 1", bg="lightblue", width=20)
drag_label1.pack(pady=20)

# Label to drag 2
drag_label2 = tk.Label(root, text="Drag this label 2", bg="lightpink", width=20)
drag_label2.pack(pady=20)

# Drop area frame
drop_frame = tk.Frame(root, bg="lightgreen", width=400, height=200)
drop_frame.pack(pady=20)

# Drop label
drop_label = tk.Label(drop_frame, text="Drop here", bg="lightgreen", width=20)
drop_label.pack(pady=20)

# Drag start event
def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    dx = event.x - widget._drag_start_x
    dy = event.y - widget._drag_start_y
    widget.move(widget._drag_data['item'], dx, dy)

# Drop event
def on_drop(event):
    drop_label.config(text=f"{event.data} has been dropped", bg="lightcoral")

# Binding events
drag_label1.bind("<ButtonPress>", on_drag_start)
drag_label2.bind("<ButtonPress>", on_drag_start)
drop_frame.drop_target_register(DND_FILES)
drop_frame.dnd_bind('<ButtonRelease>', on_drop)

# Start the main loop
root.mainloop()