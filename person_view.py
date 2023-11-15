import tkinter as tk
from tkinter import messagebox

class PersonaView:
    def __init__(self):
        self.tab1 = "    "
        self.tab2 = "    " * 2
        self.tab3 = "    " * 3

        self.opcion_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.idpersona_var = tk.StringVar()
        self.dni_var = tk.StringVar()

        self.txt_opt = "%sElija una opción: " % self.tab2
        self.txt_nombre = "%sNombre: " % self.tab3
        self.txt_apellido = "%sApellido: " % self.tab3
        self.txt_idpersona = "%sID de Persona: " % self.tab3
        self.txt_dni = "%sD.N.I: " % self.tab3

    def mostrar_menu(self):
        """Vista del menú de opciones"""
        menu = """
        Menú del Gestor de Personas
            (1) Crear una persona
            (2) Ver listado de personas
            (3) Editar una persona
            (4) Eliminar una persona

            (0) Salir
        """
        messagebox.showinfo("Menú", menu)

       
        window = tk.Toplevel()
        tk.Label(window, text=self.txt_opt).pack()
        tk.Entry(window, textvariable=self.opcion_var).pack()
        tk.Button(window, text="Confirmar", command=window.destroy).pack()

        window.wait_window(window)

        return self.opcion_var.get().strip()
    
    def crear_persona(self):
        """Vista del formulario para crear una nueva persona"""
        self.reset_variables()

        window = tk.Toplevel()
        tk.Label(window, text=self.txt_nombre).pack()
        tk.Entry(window, textvariable=self.nombre_var).pack()
        tk.Label(window, text=self.txt_apellido).pack()
        tk.Entry(window, textvariable=self.apellido_var).pack()
        tk.Label(window, text=self.txt_dni).pack()
        tk.Entry(window, textvariable=self.dni_var).pack()

        confirmar_button = tk.Button(window, text="Confirmar", command=lambda: self.confirmar_creacion(window))
        confirmar_button.pack()
        window.wait_window(window)

        return {
            'nombre': self.nombre_var.get(),
            'apellido': self.apellido_var.get(),
            'dni': self.dni_var.get()
        }

    

    def confirmar_creacion(self,window):
        """Vista de confirmación de creación de nueva persona"""
        messagebox.showinfo("Confirmación", "Persona creada con éxito!")
        window.destroy()

    def listar_persona(self, listado):
        """Vista para el listado de persona"""
        result = "LISTADO DE PERSONAS:\n"
        for row in listado:
            idpersona, nombre, apellido, dni = row
            result += "%s[%d] %s (%s) %s\n" % (self.tab3, idpersona, nombre, apellido, dni)
        messagebox.showinfo("Listado de Personas", result)

    def editar_persona(self, listado):
        """Vista del formulario para editar una persona"""
        self.reset_variables()

        window = tk.Toplevel()
        tk.Label(window, text=self.txt_idpersona).pack()
        tk.Entry(window, textvariable=self.idpersona_var).pack()
        tk.Label(window, text=self.txt_nombre).pack()
        tk.Entry(window, textvariable=self.nombre_var).pack()
        tk.Label(window, text=self.txt_apellido).pack()
        tk.Entry(window, textvariable=self.apellido_var).pack()
        tk.Label(window, text=self.txt_dni).pack()
        tk.Entry(window, textvariable=self.dni_var).pack()
        tk.Button(window, text="Confirmar", command=window.destroy).pack()

        window.wait_window(window)

        return {
            'idpersona': self.idpersona_var.get(),
            'nombre': self.nombre_var.get(),
            'apellido': self.apellido_var.get(),
            'dni': self.dni_var.get()
        }

    def confirmar_editar_persona(self):
        """Vista de confirmación de edición"""
        messagebox.showinfo("Confirmación", "Persona editada correctamente.")

    def eliminar_persona(self, listado):
        """Vista de formulario para eliminar una persona"""
        self.reset_variables()

        window = tk.Toplevel()
        tk.Label(window, text=self.txt_idpersona).pack()
        tk.Entry(window, textvariable=self.idpersona_var).pack()
        tk.Button(window, text="Confirmar", command=window.destroy).pack()

        window.wait_window(window)

        return self.idpersona_var.get()

    def confirmar_eliminar_persona(self):
        """Vista de confirmación eliminar persona"""
        messagebox.showinfo("Confirmación", "Persona eliminada correctamente.")

    def reset_variables(self):
        """Reiniciar variables de instancia"""
        self.nombre_var.set('')
        self.apellido_var.set('')
        self.idpersona_var.set('')
        self.dni_var.set('')
