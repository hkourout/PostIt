import tkinter as tk 
my_w = tk.Tk()
my_w.geometry("615x400")  # width and height 
def my_callback(event):
    global f_img1, f_img2
    l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    f_img1 = tk.PhotoImage(file="ball1.png") 
    my_c.create_image(event.x, event.y,  image=f_img1)
    #f_img2 = tk.PhotoImage(file="ball1.png") 
    #my_c.create_image(event.x, event.y,  image=f_img2)
l1=tk.Label(my_w,text='to Display',bg='yellow',font=30)
l1.pack(padx=10,pady=5)
f_img1 = tk.PhotoImage(file="ball1.png") # path of the image
#f_img2 = tk.PhotoImage(file="ball1.png") # path of the image
my_c = tk.Canvas(my_w,width=600,height=400) # canvas size 
my_c.pack() # place on pack 
my_c.create_image(160, 100,  image=f_img1) # add image to canvas
#my_c.create_image(80, 50,  image=f_img2) # add image to canvas
my_w.bind('<B1-Motion>',my_callback) # Mouse left button pressed move
my_w.mainloop()