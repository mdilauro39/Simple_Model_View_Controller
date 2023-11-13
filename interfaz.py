import tkinter as ttk
from person import Persona
def crear_usuario():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dni = dni_entry.get()
    genero = genero_entry.get()


    persona = Persona()
    persona.nombre = nombre
    persona.apellido = apellido
    persona.dni = dni
    persona.genero = genero
    persona.create()



ventana = ttk.Tk()
ventana.title("Formulario de Usuario")

nombre_label = ttk.Label(ventana, text="Nombre:")
nombre_label.pack()
nombre_entry = ttk.Entry(ventana)
nombre_entry.pack()

apellido_label = ttk.Label(ventana, text="Apellido:")
apellido_label.pack()
apellido_entry = ttk.Entry(ventana)
apellido_entry.pack()

dni_label = ttk.Label(ventana, text="DNI:")
dni_label.pack()
dni_entry = ttk.Entry(ventana)
dni_entry.pack()

genero_label = ttk.Label(ventana, text="Genero:")
genero_label.pack()
genero_entry = ttk.Entry(ventana)
genero_entry.pack()

# Botón para guardar los datos
guardar_button = ttk.Button(ventana, text="Guardar", command=crear_usuario)
guardar_button.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()