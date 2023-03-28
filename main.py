
from customtkinter import *
from tkinter import*
from analizador import read
from errores import errors
import webbrowser
from tkinter import *
from customtkinter import *
import tkinter
root = CTk()
root.title("Analizador")
icon = PhotoImage(file="./imgs/logo.png")
root.iconphoto(False,icon)

global filename

def nuevo():
    mensaje.set('Nuevo archivo')
    texto.delete(1.0, END)  

def abrir():
    global filename
    mensaje.set("Abrir archivo")
    filename = filedialog.askopenfilename(initialdir="./entrys")
    print(filename)
    if filename != "":  
        fichero = open(filename, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')           # Nos aseguramos de que esté vacío
        texto.insert('insert', contenido)  # Le insertamos el contenido
        fichero.close()                    # Cerramos el fichero
        name  = str(os.path.basename(filename))
        root.title(name + " - Analizador") 

def guardar():
    global filename
    if filename != "":
        contenido = texto.get(1.0, 'end')  # Recuperamos el texto
        fichero = open(filename, 'w+')         # Creamos el fichero o abrimos
        fichero.write(contenido)           # Escribimos el texto
        fichero.close()
        mensaje.set('Archivo guardado correctamente')

def guardar_como():
    global ruta
    fichero = filedialog.asksaveasfile(title="Guardar archivo", mode='w',
            defaultextension=".txt")
    ruta = fichero.name  # El atributo name es la ruta, si está abierto
    if fichero is not None:
        contenido = texto.get(1.0, 'end-1c')  # recuperamos el texto
        fichero = open(ruta, 'w+') # creamos el fichero o abrimos
        fichero.write(contenido)  # escribimos el texto
        fichero.close()
        mensaje.set('Archivo guardado correctamente')
    else:
        mensaje.set('Guardado cancelado')

def analisis():
    global filename
    read(filename)

def error():
    global filename
    errors(filename)

def info():
    nueva_ventana = tkinter.Toplevel(root) 
    nueva_ventana.title("Información del Desarrollador")   
    ancho_cargar_archivo= 500
    alto_cargar_archivo= 600
    x_cargar_archivo = root.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = root.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

    #LABELS
    a=150

    #IMAGEN

    #LABEL IMG
    perfil = tkinter.PhotoImage(file="./imgs/perfil.png")
    ima = tkinter.Label(nueva_ventana, image=perfil, width=150,height=150, bg="#212F3C")
    ima.place(x=125,y=105, anchor=tkinter.CENTER)

    #nombres


    nombre = tkinter.Label(nueva_ventana, text="Geovanny Sebastián", font=("Helvetica", 28, "bold"))
    nombre.config(bg="#212F3C", fg="white",anchor=tkinter.W)
    nombre.place(x=40,y=50+a)

    #apellidos

    apellidos = tkinter.Label(nueva_ventana, text="Herrera Claudio", font=("Helvetica", 28, "bold"))
    apellidos.config(bg="#212F3C", fg="white",anchor=tkinter.W)
    apellidos.place(x=40,y=100+a)

    #carne

    carne = tkinter.Label(nueva_ventana, text="Carné: 202110588", font=("Helvetica", 14, "bold"))
    carne.config(bg="#212F3C", fg="#D0D3D4",anchor=tkinter.W)
    carne.place(x=40,y=160+a)

    #cui

    cui = tkinter.Label(nueva_ventana, text="CUI: 3556794340101", font=("Helvetica", 14, "bold"))
    cui.config(bg="#212F3C", fg="#D0D3D4",anchor=tkinter.W)
    cui.place(x=40,y=195+a)

    #curso

    cui = tkinter.Label(nueva_ventana, text="Lab. Introducción a la Programación y Computación 2", font=("Helvetica", 11, "bold"))
    cui.config(bg="#212F3C", fg="#B3B6B7",anchor=tkinter.W)
    cui.place(x=40,y=230+a)

    #github

    def github():
        webbrowser.open_new_tab("https://github.com/SebastianHerrera")

    button = CTkButton(master=nueva_ventana, text="GitHub", command=github,fg_color=("#17202A"),hover_color="#5D6D7E")
    button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#212F3C")
    nueva_ventana.resizable(0,0)

def manualDeUsuario():
     webbrowser.open_new_tab("C:/Users/sebas/Documents/USAC/Primer Semestre 2023/Lab LFP/Proyecto 1/manuals/ManualDeUsuario.pdf")
def manualTecnico():
     webbrowser.open_new_tab("C:/Users/sebas/Documents/USAC/Primer Semestre 2023/Lab LFP/Proyecto 1/manuals/ManualTecnico.pdf")

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_command(label="Analizar",command=analisis)
filemenu2.add_command(label="Errores",command=error)
menubar.add_cascade(label="Análisis", menu=filemenu2)

filemenu3 = Menu(menubar, tearoff=0)
filemenu3.add_command(label="Temas de Ayuda",command=info)
filemenu3.add_command(label="Manual de Usuario",command=manualDeUsuario)
filemenu3.add_command(label="Manual Técnico",command=manualTecnico)
menubar.add_cascade(label="Ayuda", menu=filemenu3)

# Caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(padx=6, pady=4, bd=0, font=("Roboto", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar=mensaje, justify='right',bg="#242424",fg="white")
monitor.pack(side='left')

# Menu y bucle de la aplicación
root.config(menu=menubar)
root.mainloop()