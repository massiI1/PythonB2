import tkinter as tk
from tkinter import ttk

fenetre = tk.Tk()
fenetre.title("ma premiere fenetre")
fenetre.geometry("400x300")

fenetre.mainloop()

label = ttk.Label(fenetre, texte="bonjour Tkinter")
label.pack(pady=20)
