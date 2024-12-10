#!/usr/bin/env python3
import tkinter as tk

class Fenetre(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill='both', expand=1)        
        self.canvas = tk.Canvas(self, width=500, height=500, background="#383")
        self.canvas.pack(padx=8, pady=8) 
        self.create_drawing()

    def move(self, event):
        def node_center(tag):
            """ Renvoie le centre du noeud étant donné
                son rectangle englobant
            """
            x1, y1, x2, y2 = self.canvas.coords(tag)
            return (x1 + x2) // 2, (y1 + y2) // 2
        # ---------------------------------------------------------------------
        x, y = event.x, event.y # Coordonnées cliquées
        tags = self.canvas.gettags(tk.CURRENT) # tags contient le tag "node-B" et "current"

        for tag in tags:
            if not tag.startswith("node"):
                continue
            # Ceci est normalement effectué pour un seul tag (par ex "node-B").
            # Comme deux objets ont ce tag, les deux sont déplacés simultanément
            # par self.canvas.move...
            x1, y1 = node_center(tag)
            self.canvas.move(tag, x-x1, y-y1) 

    def create_drawing(self):
        # Affichage des noeuds et du texte
        nodes = [("A", 100, 200), ("B", 50, 100), ("C", 400, 20)]
        for nodename, nodex, nodey in nodes:
            tmpnode = self.canvas.create_oval(nodex - 10, nodey - 10, 
                                              nodex + 10, nodey + 10, 
                                              fill="#000066", outline="#0000ff")
            tmptxt = self.canvas.create_text(nodex, nodey, fill="#ffffff", text=nodename)
            tag = "node-{}".format(nodename)
            self.canvas.addtag_withtag(tag, tmpnode) # On tague les objets avec : "node-A", "node-B"...
            self.canvas.addtag_withtag(tag, tmptxt)
            #Association callbacks au rond ET au texte
            self.canvas.tag_bind(tmpnode, '<B1-Motion>', self.move)
            self.canvas.tag_bind(tmptxt, '<B1-Motion>', self.move)

root, gui = None, None
# Création de l'application
root = tk.Tk()
# Ajout des éléments graphiques 
gui = Fenetre(root)
# Boucle des événements
root.mainloop()