# -*- coding: utf-8 *-*
from person import Persona 
from person_view import PersonaView
from db_connection import DBConn

#https://guia-tkinter.readthedocs.io/es/develop/chapters/5-basic/5.2-Clases.html

from tkinter import *
import tkinter as tk
from tkinter import scrolledtext

class MVC(tk.Tk):
    def __init__(self):
        super().__init__()

        self.controller = PersonaController()
        self.persona_view = PersonaView()
        self.output_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=10, width=50)
        self.output_text.pack()
        self.button = tk.Button(self, text="Mostrar Menú", command=self.mostrar_menu_en_tkinter)
        self.button.pack()
      

    def mostrar_menu_en_tkinter(self):
        self.output_text.delete('1.0', tk.END)
        menu_text = self.persona_view.mostrar_menu()
        self.output_text.insert(tk.END, menu_text)



#from six.moves import tkinter as tk

# class UI(tk.Frame):
#     """Docstring."""

#     def __init__(self, parent=None):
#         tk.Frame.__init__(self, parent)
#         self.parent = parent
#         self.init_ui()

#     def init_ui(self):
#         """Aqui colocariamos los widgets."""
#         self.parent.title("Un titulo para la ventana")

# if __name__ == "__main__":
#     ROOT = tk.Tk()
#     ROOT.geometry("800x600")
#     APP = UI(parent=ROOT)
#     APP.mainloop()
#     ROOT.destroy()

class PersonaController:

    def __init__(self):
        self.vista = PersonaView()
        self.persona_controller()
        
    def persona_controller(self):
        """Controlador general de persona"""
        peticion = self.vista.mostrar_menu()
        self.peticion = int(peticion)

        if self.peticion == 1:
            self.crear_persona_controller()
        elif self.peticion == 2:
            self.listar_persona_controller()
        elif self.peticion == 3:
            self.editar_persona_controller()
        elif self.peticion == 4:
            self.eliminar_persona_controller()

    def crear_persona_controller(self):
        """Controlador para creación de nueva persona"""
        datos_persona = self.vista.crear_persona()

    
        if datos_persona:
        
            persona_nombre = datos_persona['nombre']
            persona_apellido = datos_persona['apellido']
            persona_dni = int(datos_persona['dni'])
            persona = Persona()
            persona.nombre = persona_nombre
            persona.apellido = persona_apellido
            persona.dni = persona_dni
            persona.create()

       
            self.persona_controller()

    

    def traer_persona(self):
        """Trae una lista de todos las personas"""
        persona = Persona()
        listado = persona.read_all()
        return listado

    def listar_persona_controller(self):
        """Controlador del listado de persona"""
        listado = self.traer_persona()
        self.vista.listar_persona(listado)
        self.persona_controller()

    def editar_persona_controller(self):
        """Controlador para editar un persona"""
        listado = self.traer_persona()
        (idpersona, nombre, apellido, dni) = self.vista.editar_persona(listado)
        persona = Persona()
        persona.idpersona = int(idpersona)
        persona.nombre = nombre
        persona.apellido = apellido
        persona.dni =int(dni)
        persona.update()
        self.vista.confirmar_editar_persona()
        self.persona_controller()

    def eliminar_persona_controller(self):
        """Controlador para eliminar un persona"""
        listado = self.traer_persona()
        idpersona = self.vista.eliminar_persona(listado)
        idpersona = idpersona
        persona = Persona()
        persona.idpersona = idpersona
        persona.delete()
        self.vista.confirmar_eliminar_persona()
        self.persona_controller()


#controller = PersonaController()

if __name__ == "__main__":
     app = MVC()
     app.mainloop()


# mvc = Tk()
# mvc.title("Carga de productos")
# mvc.geometry("750x750")
# mvc.mainloop()