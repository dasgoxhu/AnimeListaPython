import tkinter as tk
from tkinter import PhotoImage
from anime_app import AnimeApp
from anime_manager import AnimeManager
from tkinter import messagebox


class MainMenu:
    def __init__(self, root, manager, app):
        self.root = root
        self.manager = manager
        self.app = app

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opciones", menu=file_menu)
        file_menu.add_command(label="Borrar Todo", command=self.clear_all)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit_app)
        menubar.configure(bg="black", fg="white")
        file_menu.configure(bg="black", fg="white")

    def clear_all(self):
        result = messagebox.askquestion("Borrar Todo", "¿Estás seguro de que deseas borrar todos los datos?")
        if result == "yes":
            with open(self.manager.file_path, 'w') as file:
                file.truncate(0)
            self.app.display_animes()
            messagebox.showinfo("Borrado", "Todos los datos han sido eliminados.")

    def quit_app(self):
        self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    root.overrideredirect(True)
    window_width = 365
    window_height = 530
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(bg="black")

    manager = AnimeManager('animes.txt')
    app = AnimeApp(root, manager)
    menu = MainMenu(root, manager, app)
    app.display_animes()

    app_name_label = tk.Label(root, text="Gestor de Animes", font=("Arial", 16), bg="black", fg="white")
    app_name_label.grid(row=0, column=0, columnspan=4, pady=(10, 0))



    try:
        image = PhotoImage(file="icono.png")
        image_label = tk.Label(root, image=image, bg="black")
        image_label.image = image
        image_label.grid(row=1, column=0, columnspan=4, pady=10)
        app_name_label3 = tk.Label(root, text="Ingresa el anime:", font=("Arial", 10), bg="black", fg="white")
        app_name_label3.grid(row=3, column=0, columnspan=4, pady=(10, 0))
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

    app.entry.config(bg="black", fg="white")
    app.animes_listbox.config(bg="black", fg="white")
    app_name_label.config(bg="black", fg="white")

    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(bg="black", fg="white")

    root.mainloop()
