import tkinter as tk
from tkinter import PhotoImage, messagebox

class AnimeApp:
    def __init__(self, root, manager):
        self.root = root
        self.root.title("Gestor de Animes")
        self.manager = manager

        self.entry = tk.Entry(root, width=20, font=('Arial', 16))
        self.entry.grid(row=4, column=0,pady=10, columnspan=4)

        self.guardar_icon = tk.PhotoImage(file="save.png").subsample(15)
        self.limpiar_icon = tk.PhotoImage(file="clear.png").subsample(15)

        botones = [self.guardar_icon, self.limpiar_icon]
        row, col = 5, 0
        for boton_icon in botones:
            tk.Button(root, image=boton_icon, width=40, height=40, pady=10,
                      command=lambda b=boton_icon: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 1:
                col = 0
                row += 5

        app_name_label2 = tk.Label(root, text="Lista Animes", font=("Arial", 10), bg="black", fg="white")
        app_name_label2.grid(row=6, column=0, columnspan=4, pady=(10, 0))
        self.animes_listbox = tk.Listbox(root, width=40, height=8, font=('Arial', 12))
        self.animes_listbox.grid(row=7, column=0, columnspan=2,pady=10)
        app_name_label2 = tk.Label(root, text="By Dasgoxhu", font=("Arial", 10), bg="black", fg="white")
        app_name_label2.grid(row=8, column=0, columnspan=4, pady=(10, 0))


    def on_button_click(self, button):
        if button == self.guardar_icon:
            anime = self.entry.get()
            if not anime:
                messagebox.showwarning("Campo Vacío", "Debes ingresar un nombre de anime.")
            else:
                self.manager.save_anime(anime)
                self.entry.delete(0, tk.END)
                self.display_animes()
                messagebox.showinfo("Guardado", "Anime guardado con éxito.")
        elif button == self.limpiar_icon:
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Limpiado", "Se Limpio con exito La entrada.")

    def display_animes(self):
        self.animes_listbox.delete(0, tk.END)
        animes = self.manager.load_animes()
        for anime in animes:
            self.animes_listbox.insert(tk.END, anime)