import tkinter as tk
from tkinter import PhotoImage, messagebox

class AnimeApp:
    def __init__(self, root, manager):
        self.root = root
        self.root.title("Gestor de Animes")
        self.manager = manager

        self.entry = tk.Entry(root, width=20, font=('Arial', 16))
        self.entry.grid(row=4, column=0, pady=10, columnspan=4)

        self.guardar_icon = tk.PhotoImage(file="save.png").subsample(15)
        self.limpiar_icon = tk.PhotoImage(file="clear.png").subsample(15)
        self.editar_icon = tk.PhotoImage(file="edit.png").subsample(15)
        self.borrar_icon = tk.PhotoImage(file="delete.png").subsample(15)

        tk.Button(root, image=self.guardar_icon, width=40, height=40, pady=10, padx=5,
                  command=lambda: self.on_button_click(self.guardar_icon)).grid(row=6, column=0)
        tk.Button(root, image=self.limpiar_icon, width=40, height=40, pady=10, padx=5,
                  command=lambda: self.on_button_click(self.limpiar_icon)).grid(row=6, column=1)
        tk.Button(root, image=self.editar_icon, width=40, height=40, pady=10, padx=5,
                  command=lambda: self.on_button_click(self.editar_icon)).grid(row=6, column=2)
        tk.Button(root, image=self.borrar_icon, width=40, height=40, pady=10, padx=5,
                  command=lambda: self.on_button_click(self.borrar_icon)).grid(row=6, column=3)

        app_name_label2 = tk.Label(root, text="Lista Animes", font=("Arial", 10), bg="black", fg="white")
        app_name_label2.grid(row=8, column=0, columnspan=4, pady=10)
        self.animes_listbox = tk.Listbox(root, width=40, height=8, font=('Arial', 12))
        self.animes_listbox.grid(row=9, column=0, columnspan=4, pady=10)
        app_name_label2 = tk.Label(root, text="By Dasgoxhu", font=("Arial", 10), bg="black", fg="white")
        app_name_label2.grid(row=10, column=0, columnspan=4, pady=(10, 0))

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
            messagebox.showinfo("Limpiado", "Se Limpio con éxito La entrada.")
        elif button == self.editar_icon:
            self.editar_anime()
        elif button == self.borrar_icon:
            self.borrar_anime()

    def editar_anime(self):
        selected_index = self.animes_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            new_name = self.entry.get()
            if new_name:
                self.manager.edit_anime(selected_index, new_name)
                self.display_animes()
                self.entry.delete(0, tk.END)
                messagebox.showinfo("Editado", "Anime editado con éxito.")
            else:
                messagebox.showwarning("Campo Vacío", "Debes ingresar un nuevo nombre para editar el anime.")

    def borrar_anime(self):
        selected_index = self.animes_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            self.manager.delete_anime(selected_index)
            self.display_animes()
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Borrado", "Anime borrado con éxito.")

    def display_animes(self):
        self.animes_listbox.delete(0, tk.END)
        animes = self.manager.load_animes()
        for anime in animes:
            self.animes_listbox.insert(tk.END, anime)
