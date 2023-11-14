# -*- coding: utf-8 *-*
# mi_modulo_ttk.py

from tkinter import Tk, Label, Entry, Button, Listbox, messagebox
from tkinter import ttk  # Importa el módulo ttk de tkinter

class MiApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("CRUD con ttk")

        # Etiqueta
        self.etiqueta = ttk.Label(ventana, text="Elementos:")
        self.etiqueta.pack(pady=10)

        # Lista para mostrar elementos
        self.lista_elementos = Listbox(ventana, height=5)
        self.lista_elementos.pack(padx=10, pady=10)

        # Entrada de texto para ingresar elementos
        self.entrada_elemento = ttk.Entry(ventana)
        self.entrada_elemento.pack(padx=10, pady=5)

        # Botones para CRUD
        self.boton_crear = ttk.Button(ventana, text="Crear", command=self.crear_elemento)
        self.boton_crear.pack(side="left", padx=5)
        
        self.boton_actualizar = ttk.Button(ventana, text="Actualizar", command=self.actualizar_elemento)
        self.boton_actualizar.pack(side="left", padx=5)
        
        self.boton_eliminar = ttk.Button(ventana, text="Eliminar", command=self.eliminar_elemento)
        self.boton_eliminar.pack(side="left", padx=5)

        # Llena la lista con algunos elementos de ejemplo
        self.lista_elementos.insert("end", "Elemento 1")
        self.lista_elementos.insert("end", "Elemento 2")

    def crear_elemento(self):
        nuevo_elemento = self.entrada_elemento.get()
        if nuevo_elemento:
            self.lista_elementos.insert("end", nuevo_elemento)
            self.entrada_elemento.delete(0, "end")  # Borra el texto después de agregar

    def actualizar_elemento(self):
        seleccionado = self.lista_elementos.curselection()
        if seleccionado:
            nuevo_texto = self.entrada_elemento.get()
            if nuevo_texto:
                self.lista_elementos.delete(seleccionado)
                self.lista_elementos.insert(seleccionado, nuevo_texto)
                self.entrada_elemento.delete(0, "end")  # Borra el texto después de actualizar
        else:
            messagebox.showwarning("Error", "Selecciona un elemento para actualizar")

    def eliminar_elemento(self):
        seleccionado = self.lista_elementos.curselection()
        if seleccionado:
            self.lista_elementos.delete(seleccionado)
            self.entrada_elemento.delete(0, "end")  # Borra el texto después de eliminar
        else:
            messagebox.showwarning("Error", "Selecciona un elemento para eliminar")

if __name__ == "__main__":
    ventana = Tk()
    app = MiApp(ventana)
    ventana.mainloop()

class Persona:

    def __init__(self):
        self.idpersona =''
        self.nombre = ''
        self.apellido = ''
        self.dni = 0
        self.fecha_nacimiento = ''
        self.db = DBConn()

    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO persona VALUES (null,?,?,?,'null','null')"
        values = (self.nombre, self.apellido, self.dni)
        self.db.ejecutar(query, values)

    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE persona SET nombre = ?, apellido = ?, dni = ? WHERE idpersona = ?"
        values = (self.nombre, self.apellido, self.dni, self.idpersona)
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT idpersona, nombre , apellido , dni FROM persona"
        return self.db.ejecutar(query)

    def read(self):
        query = "SELECT idpersona, nombre, apellido, dni FROM persona WHERE idpersona = ?"
        values = (self.idpersona)
        return self.db.ejecutar(query, values)
    
    def delete(self):
        """Elimina uno o todos los registros"""
        query = "DELETE FROM persona WHERE idpersona = ?"
        values = self.idpersona
        return self.db.ejecutar(query, values)