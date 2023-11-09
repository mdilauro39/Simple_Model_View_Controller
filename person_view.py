# -*- coding: utf-8 *-*

# from tkinter import *

# class Vista:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("")

#         self.etiqueta = tk.Label(self.root, text="etiqueta")
#         self.etiqueta.pack()

from tkinter import *
from tkinter import ttk

class PersonaView():

    
    


    def __init__(self):
        self.tab1 = "    "
        self.tab2 = "    " * 2
        self.tab3 = "    " * 3
        self.txt_opt = "%sElija una opción: " % self.tab2
        self.txt_nombre = "%sNombre: " % self.tab3
        self.txt_apellido = "%sApellido: " % self.tab3
        self.txt_idpersona = "%sID de Persona: " % self.tab3
        self.txt_dni = "%sD.N.I de la persona (sin puntos): " % self.tab3
        self.txt_genero = "%sGenero: " % self.tab3
        
       
        
        pass



    Persona = Tk()
    Persona.title = ("PersonaForm")
    Persona.geometry=('1000 x 1000')
    ttk.Label(Persona, text="Menú del Gestor de Personas").grid(column=0, row=0)
    ttk.Label(Persona, text=" (1) Crear una persona").grid(column=0, row=1)
    ttk.Label(Persona, text=" (2) Ver listado de perso").grid(column=0, row=2)
    ttk.Label(Persona, text=" (3) Editar una personas").grid(column=0, row=3)
    ttk.Label(Persona, text=" (4) Eliminar una person").grid(column=0, row=4)
    ttk.Label(Persona, text=" (0) Salir").grid(column=0, row=5)
    entry = ttk.Entry()
# Posicionarla en la ventana.
    entry.place(x=25, y=150)
    button = ttk.Button(Persona, 
                        text ="ENVIAR",
                        command="submit"
                        )
    
    button.place(x=195, y=145)
    Persona.mainloop()

    def mostrar_menu(self):
        """Vista del menú de opciones"""

        menu = """
        Menú del Gestor de Personas
            (1) Crear una persona
            (2) Ver listado de personas
            (3) Editar una personas
            (4) Eliminar una persona

            (0) Salir

        """
        print(menu)

        opcion = input(self.txt_opt)
        return opcion

    def crear_persona(self):
        """Vista del formulario para crear una nueva persona"""

        print("""
        CREAR UN NUEVA  PERSONA
        """)
        nombre = input(self.txt_nombre)
        apellido = input(self.txt_apellido)
        dni = int(input(self.txt_dni))
        genero = input(self.txt_genero)
        return (nombre, apellido, dni, genero)

    def confirmar_creacion(self):
        """Vista de confirmación de creación de nueva persona"""

        print ("""
        Persona creado con éxito!
        """)

    def listar_persona(self,listado):
        """Vista para el listado de persona"""

        print ("""
            LISTADO DE PERSONAS:
        """)
        for row in listado:
            idpersona = row[0]
            nombre = row[1]
            apellido = row[2]
            dni = row[3]
            genero = row[4]
            print("%s[%d] %s (%s) %s %s" % (self.tab3, idpersona, nombre, apellido, dni, genero))

    def editar_persona(self, listado):
        """Vista del formulario para editar un persona"""

        self.listar_persona(listado)
        print ("\n\n")
        idpersona = input(self.txt_idpersona)
        print ("\n")
        nombre = input(self.txt_nombre)
        apellido = input(self.txt_apellido)
        dni = input(self.txt_dni)
        genero = input(self.txt_genero)
        return (idpersona, nombre, apellido, dni, genero)

    def confirmar_editar_persona(self):
        """Vista de confirmación de edición"""

        print ("""
        Persona editada correctamente.
        """)

    def eliminar_persona(self, listado):
        """Vista de formulario para eliminar una persona"""

        self.listar_persona(listado)
        print ("\n\n")
        idpersona = input(self.txt_idpersona)
        print ("\n")
        return idpersona

    def confirmar_eliminar_persona(self):
        """Vista de cofirmación eliminar persona"""
        print( """
        Persona eliminada correctamente.
        """)
