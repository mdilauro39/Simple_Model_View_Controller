import tkinter as tk
from tkinter import ttk
from person_view import PersonaView

class InterfazPersona(tk.Tk):
    def __init__(self):
        super().__init__()

        self.persona_view = PersonaView()

        self.title("Gestor de Personas")
        self.geometry("500x500")

        welcome_label = ttk.Label(self, text = "Bienvenido al sistema MVC")
        welcome_label.pack()
        
    
        option_label = ttk.Label(self, text = "Por favor ingrese una opción")
        option_label.pack()
        
    

        button = ttk.Button(self, text="Crear Persona", command=lambda: self.handle_menu_option("1"))
        button.pack()
        
        button = ttk.Button(self, text="Listar Personas", command=lambda: self.handle_menu_option("2"))
        button.pack()
        
        button = ttk.Button(self, text="Editar Persona", command=lambda: self.handle_menu_option("3"))
        button.pack()
        
        button = ttk.Button(self, text="Eliminar Persona", command=lambda: self.handle_menu_option("4"))
        button.pack()
        
        button = ttk.Button(self, text="Salir", command=lambda: self.handle_menu_option("0"))
        button.pack()
        
    def handle_menu_option(self, option):
        if option == "1":
            self.crear_persona()
        elif option == "2":
            self.listar_personas()
        elif option == "3":
            self.editar_persona()
        elif option == "4":
            self.eliminar_persona()
        elif option == "0":
            self.destroy()
        else:
            print("Opción no válida. Inténtelo de nuevo.")


    def crear_persona(self):
        """Mostrar formulario para crear una nueva persona"""
        nombre_label = ttk.Label(self, text="Nombre")
        nombre_label.pack()
        nombre_var = tk.StringVar()
        nombre_entry = ttk.Entry(self, textvariable=nombre_var, width=30)
        nombre_entry.pack()

        apellido_label = ttk.Label(self, text="Apellido")
        apellido_label.pack()
        apellido_var = tk.StringVar()
        apellido_entry = ttk.Entry(self, textvariable=apellido_var, width=30)
        apellido_entry.pack()

        dni_label = ttk.Label(self, text="DNI")
        dni_label.pack()
        dni_var = tk.StringVar()
        dni_entry = ttk.Entry(self, textvariable=dni_var, width=30)
        dni_entry.pack()


        genero_var = tk.StringVar()
        genero_label = ttk.Label(self, text="Género")
        genero_label.pack()
        genero_entry = ttk.Entry(self, textvariable=genero_var, width=30)
        genero_entry.pack()
        

        button = ttk.Button(self, text="ENVIAR", command=lambda: self.handle_crear_persona(nombre_var.get(), apellido_var.get(), dni_var.get(), genero_var.get()))
        button.pack()
        
    def handle_crear_persona(self, nombre, apellido, dni, genero):
        form_data = (nombre, apellido, dni, genero)
        print("Datos ingresados:", form_data)
        
        self.persona_view.confirmar_creacion()
        exito_label = ttk.Label(self, text="Persona creada con éxito!")
        exito_label.pack()
        
        self.after(500, self.refrescar_ventana)


    def listar_personas(self):
        """Mostrar listado de personas"""
        listado = [("1", "Nombre1", "Apellido1", "12345678", "F"),
                   ("2", "Nombre2", "Apellido2", "87654321", "M")]
        
        
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido", "DNI", "Género", "Acciones"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Apellido", text="Apellido")
        tree.heading("DNI", text="DNI")
        tree.heading("Género", text="Género")

        # Insertar datos en la tabla
        for persona in listado:
            tree.insert("", "end", values=persona)

        # Ajustar el tamaño de las columnas
        for col in ("ID", "Nombre", "Apellido", "DNI", "Género",):
            tree.column(col, width=100)

        tree.pack()
        
        volver_button = ttk.Button(self, text="Volver al Inicio", command=self.refrescar_ventana)
        volver_button.pack(side="bottom")
        
        self.persona_view.listar_persona(listado)
        
    def refrescar_ventana(self):
        """Destruye la ventana actual y crea una nueva instancia de la clase"""
        self.destroy()
        app = InterfazPersona()
        app.mainloop()
    

        
    def editar_persona(self):
        """Mostrar formulario para editar una persona"""
        listado = [("1", "Nombre1", "Apellido1", "12345678", "F"),
                   ("2", "Nombre2", "Apellido2", "87654321", "M")]
        
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido", "DNI", "Género", "Acciones"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Apellido", text="Apellido")
        tree.heading("DNI", text="DNI")
        tree.heading("Género", text="Género")

        # Insertar datos en la tabla
        for persona in listado:
            tree.insert("", "end", values=persona)

        # Ajustar el tamaño de las columnas
        for col in ("ID", "Nombre", "Apellido", "DNI", "Género",):
            tree.column(col, width=100)

        tree.pack()
        
        id_label = ttk.Label(self, text="Id persona")
        id_label.pack()
        id_entry = ttk.Entry(self, textvariable=id, width=30)
        id_entry.pack()
        id_button = ttk.Button(self, text="Enviar", command=self.listado(id))
        id_button.pack()
        
        volver_button = ttk.Button(self, text="Volver al Inicio", command=self.refrescar_ventana)
        volver_button.pack(side="bottom")
        
        form_data = self.persona_view.editar_persona(listado)
        print("Datos editados:", form_data)
        # Puedes agregar aquí la lógica para trabajar con los datos editados

        # Confirmar edición
        self.persona_view.confirmar_editar_persona()

    def eliminar_persona(self):
        """Mostrar formulario para eliminar una persona"""
        listado = [("1", "Nombre1", "Apellido1", "12345678", "F"),
                   ("2", "Nombre2", "Apellido2", "87654321", "M")]

        id_persona = self.persona_view.eliminar_persona(listado)
        print("ID de la persona a eliminar:", id_persona)
        # Puedes agregar aquí la lógica para trabajar con el ID de la persona a eliminar

        # Confirmar eliminación
        self.persona_view.confirmar_eliminar_persona()


if __name__ == "__main__":
    app = InterfazPersona()
    app.mainloop()