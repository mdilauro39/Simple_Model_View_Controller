# -*- coding: utf-8 *-*


class PersonaView:

    def __init__(self):
        self.tab1 = "    "
        self.tab2 = "    " * 2
        self.tab3 = "    " * 3
        self.txt_opt = "%sElija una opción: " % self.tab2
        self.txt_nombre = "%sNombre: " % self.tab3
        self.txt_apellido = "%sApellido: " % self.tab3
        self.txt_idpersona = "%sID de Persona: " % self.tab3
        self.txt_dni = "%sD.N.I de la persona: " % self.tab3
        pass

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
        return (nombre, apellido, dni)

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
            print("%s[%d] %s (%s) %s" % (self.tab3, idpersona, nombre, apellido, dni))

    def editar_persona(self, listado):
        """Vista del formulario para editar un persona"""

        self.listar_persona(listado)
        print ("\n\n")
        idpersona = input(self.txt_idpersona)
        print ("\n")
        nombre = input(self.txt_nombre)
        apellido = input(self.txt_apellido)
        dni = input(self.txt_dni)
        return (idpersona, nombre, apellido, dni)

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
