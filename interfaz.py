import tkinter as tk
from tkinter import Tk, Label, Entry, Button, Toplevel, StringVar, OptionMenu
from person import Persona

# Función para guardar los datos
def guardar_datos(nombre, apellido, dni, genero):

    persona = Persona()
    persona.nombre = nombre
    persona.apellido = apellido
    persona.dni = dni
    persona.genero = genero
    persona.create()

    ventana_emergente.destroy()

def crear_vista_usuario():
    global ventana_emergente
    ventana_emergente = Toplevel(ventana)
    ventana_emergente.title("Ingresar Datos de Nueva Persona")

    nombre_label = Label(ventana_emergente, text="Nombre:")
    nombre_label.pack()
    nombre_entry = Entry(ventana_emergente)
    nombre_entry.pack()

    apellido_label = Label(ventana_emergente, text="Apellido:")
    apellido_label.pack()
    apellido_entry = Entry(ventana_emergente)
    apellido_entry.pack()

    dni_label = Label(ventana_emergente, text="DNI:")
    dni_label.pack()
    dni_entry = Entry(ventana_emergente)
    dni_entry.pack()

    genero_label = Label(ventana_emergente, text="Género:")
    genero_label.pack()
    genero_var = StringVar()
    genero_var.set("Masculino")
    genero_options = ["Masculino", "Femenino", "Otro"]
    genero_menu = OptionMenu(ventana_emergente, genero_var, *genero_options)
    genero_menu.pack()

    guardar_button = Button(ventana_emergente, text="Guardar Persona", command=lambda: guardar_datos(nombre_entry.get(), apellido_entry.get(), dni_entry.get(), genero_var.get()))
    guardar_button.pack()
    ventana_emergente.mainloop()


# Función para ver el listado de personas
def ver_listado():
    listado_ventana = tk.Toplevel(ventana)
    listado_ventana.title("Listado de Personas")

    listado_personas = Persona().read_all()

    listado_texto = tk.Text(listado_ventana, height=10, width=40)
    listado_texto.pack()

    for registro in listado_personas:
        id_persona, nombre, apellido, dni, genero = registro
        listado_texto.insert(tk.END, f"ID: {id_persona}\n")
        listado_texto.insert(tk.END, f"Nombre: {nombre}\n")
        listado_texto.insert(tk.END, f"Apellido: {apellido}\n")
        listado_texto.insert(tk.END, f"DNI: {dni}\n")
        listado_texto.insert(tk.END, f"Género: {genero}\n\n")
        listado_texto.insert(tk.END, f"--------------------\n\n")
    listado_texto.configure(state='disabled')

# Función para eliminar una persona
def crear_vista_eliminar():
    ver_listado()
    global ventana_eliminar
    ventana_eliminar = tk.Toplevel(ventana)
    ventana_eliminar.title('Eliminar Persona por id')
    id_label = Label(ventana_eliminar, text="Ingrese un id de la lista:")
    id_label.pack()
    id_entry = Entry(ventana_eliminar)
    id_entry.pack()
    eliminar_button = Button(ventana_eliminar, text="Eliminar Persona", command=lambda: eliminar_datos(id_entry.get()))
    eliminar_button.pack()
    ventana_eliminar.mainloop()

def eliminar_datos(id):
    try:
        persona = Persona()
        persona.idpersona = id
        persona.delete()
        ventana_ok = tk.Tk()
        ventana_ok.title(f"Persona con ID {id} eliminada")
    except ValueError:
            ventana_error = tk.Tk()
            ventana_error.title(f"Error")


ventana = tk.Tk()
ventana.title("Gestion de Usuarios")

# Barra de menú
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Menú "Acciones"
acciones_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Acciones", menu=acciones_menu)
acciones_menu.add_command(label="Crear usuario", command=crear_vista_usuario)
acciones_menu.add_command(label="Ver Listado", command=ver_listado)
acciones_menu.add_command(label="Eliminar Persona", command=crear_vista_eliminar)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
