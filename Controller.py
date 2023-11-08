# -*- coding: utf-8 *-*
from person import Persona 
from person_view import PersonaView
from db_connection import DBConn




class PersonaController():



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
        (persona_nombre, persona_apellido, persona_dni, persona_genero) = self.vista.crear_persona()
        persona = Persona()
        persona.nombre = persona_nombre
        persona.apellido = persona_apellido
        persona.dni = persona_dni
        persona.genero = persona_genero
        persona.create()
        self.vista.confirmar_creacion()
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
        (idpersona, nombre, apellido, dni, genero) = self.vista.editar_persona(listado)
        persona = Persona()
        persona.idpersona = int(idpersona)
        persona.nombre = nombre
        persona.apellido = apellido
        persona.dni =int(dni)
        persona.genero = genero
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


controller = PersonaController()

