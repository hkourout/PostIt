from tkinter import *
from PIL import ImageGrab # If on Linux, use `import pyscreenshot as ImageGrab` after installing it

root = Tk()

def capture(wid,file_name='img',file_format='png'):
    """Take screenshot of the passed widget"""

    x0 = root.winfo_rootx() + wid.winfo_rootx()
    y0 = root.winfo_rooty() + wid.winfo_rooty()
    x1 = x0 + root.winfo_width() + wid.winfo_width()
    y1 = y0 + root.winfo_height() + wid.winfo_height()

    im = ImageGrab.grab((x0, y0, x1, y1))
    im.save(f'{file_name}.{file_format}')  # Can also say im.show() to display it

frame = Frame(root,bg='red',width=100,height=185)
frame.pack()
frame.pack_propagate(0) # Make it not auto-resize according to widgets

for i in range(5):
    Button(frame,text=f'Button {i}').pack()

Button(root,text='Take screenshot',command=lambda: capture(frame,file_name='frame',file_format='png')).pack()

root.mainloop()