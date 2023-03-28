from os import remove,system
from os import system
import math
import graphviz

errores = ["#","$","%","&","(",")","*","+","/","^","@","!","¡","?","¿"]

def read(filename):
    colores = ['"Amarillo"','"Rojo"','"Verde"','"Azul"','"Celeste"','"Cyan"','"Blanco"','"Negro"','"Morado"']
    formas = ['"Cuadrado"','"Triangulo"','"Circulo"','"Rombo"']
    with open(filename,mode="r") as archivo:
        text = ""
        counter = 0
        count = 0
        for linea in archivo:
            for fondo in colores:
                if '"Color-Fondo-Nodo":'+fondo in linea:
                    if fondo=='"Amarillo"':
                        background = "yellow"
                    elif fondo=='"Rojo"':
                        background = "red"
                    elif fondo=='"Verde"':
                        background = "green"
                    elif fondo=='"Azul"':
                        background = "blue"
                    elif fondo=='"Celeste"':
                        background = "skyblue"
                    elif fondo=='"Cyan"':
                        background = "cyan"
                    elif fondo=='"Blanco"':
                        background = "white"
                    elif fondo=='"Negro"':
                        background = "black"
                    elif fondo=='"Morado"':
                        background = "purple"

            for fuente in colores:
                if '"Color-Fuente-Nodo":'+fuente in linea:
                    if fuente=='"Amarillo"':
                        font = "yellow"
                    elif fuente=='"Rojo"':
                        font = "red"
                    elif fuente=='"Verde"':
                        font = "green"
                    elif fuente=='"Azul"':
                        font = "blue"
                    elif fuente=='"Celeste"':
                        font = "skyblue"
                    elif fuente=='"Cyan"':
                        font = "cyan"
                    elif fuente=='"Blanco"':
                        font = "white"
                    elif fuente=='"Negro"':
                        font = "black"
                    elif fuente=='"Morado"':
                        font = "purple"
            for forma in formas:
                if '"Forma-Nodo":'+forma in linea:
                    if forma=='"Cuadrado"':
                        form = "square"
                    elif forma=='"Circulo"':
                        form = "circle"
                    elif forma=='"Triangulo"':
                        form = "triangle"
                    elif forma=='"Rombo"':
                        form = "diamond"
        try:
                    remove("specs.txt")
                    file = open("specs.txt", "w")
                    file.write(text)
                    file.close()

        except:
            file = open("specs.txt", "w")
            file.write(text)
            file.close()

    with open(filename,mode="r") as archivo:
        dot = graphviz.Digraph(comment="Example")
        inicial = 0
        text = ""
        for linea in archivo:
            if "{" in linea:
                text = text+linea+"\n"
            if "}" in linea:
                text = text+linea+"\n"
                if '"Operacion":"Suma"' in text:
                    remove("operacion.txt")
                    file = open("operacion.txt", "w")
                    file.write(text)
                    file.close()
                    inicial=inicial+1
                    var1="a"+str(inicial)
                    dot.node(var1,"SUMA"+"\\n",{"color":background,"fontcolor":font,"style":"filled","shape":form})
                    digit = 1
                    num = 0
                    file = open("operacion.txt", "r")
                    for valores in file:
                        const = '"Valor'+str(digit)+'":'
                        if const in valores:
                            digit = digit+1
                            print(valores.rstrip())
                            texto = ""
                            if const+"[" in valores.replace(" ",""):
                                for datos in file:
                                    if "[" in datos:
                                        texto = texto+datos+"\n"
                                    if "]" in datos:
                                        texto = texto+datos+"\n"
                                        remove("operacionNew.txt")
                                        archivo = open("operacionNew.txt", "w")
                                        archivo.write(texto)
                                        archivo.close()

                                        digito = 1
                                        archivo = open("operacionNew.txt","r")
                                        if '"Operacion":"Seno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num+float(math.sin(numero))
                                            texto=""
                                            archivo.close()
                                            break
                                        
                                        elif '"Operacion":"Potencia"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))

                                                    numero2 = float(a.rstrip())
                                                    num = num+(numero**numero2)
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Raiz"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num+(numero**(1/numero2))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Coseno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num+float(math.cos(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Tangente"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num+float(math.tan(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Inverso"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = (1/numero)
                                                    num = num+numero
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Mod"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num+(numero%numero2)
                                            texto=""
                                            archivo.close()
                                            break


                                    else:
                                        texto = texto+datos+"\n"
                                

                            else:
                                a=(valores.replace(const,""))
                                num = num+float(a.rstrip())
                    print("\n Resultado de la suma: \n"+str(num))
                    file.close()
                    text=""

                elif '"Operacion":"Resta"' in text:
                    remove("operacion.txt")
                    file = open("operacion.txt", "w")
                    file.write(text)
                    file.close()
                    print("\n RESTA \n")
                    digit = 1
                    num = 0
                    counter = 0
                    file = open("operacion.txt", "r")
                    for valores in file:
                        const = '"Valor'+str(digit)+'":'
                        if const in valores:
                            digit = digit+1
                            print(valores.rstrip())
                            texto = ""
                            if const+"[" in valores.replace(" ",""):
                                for datos in file:
                                    if "[" in datos:
                                        texto = texto+datos+"\n"
                                    if "]" in datos:
                                        texto = texto+datos+"\n"
                                        remove("operacionNew.txt")
                                        archivo = open("operacionNew.txt", "w")
                                        archivo.write(texto)
                                        archivo.close()

                                        digito = 1
                                        archivo = open("operacionNew.txt","r")
                                        if '"Operacion":"Seno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    if counter==1:
                                                        numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                        numero = numero*(math.pi/180)
                                                        num = num+float(math.sin(numero))
                                                    if counter ==0:
                                                        numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                        numero = numero*(math.pi/180)
                                                        num = num+float(math.sin(numero))
                                                        counter = 1
                                            texto=""
                                            archivo.close()
                                            break
                                        
                                        elif '"Operacion":"Potencia"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num-(numero**numero2)
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Raiz"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num-(numero**(1/numero2))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Coseno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num-float(math.cos(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Tangente"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num-float(math.tan(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Inverso"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = (1/numero)
                                                    num = num-numero
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Mod"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num-(numero%numero2)
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Division"' in texto:
                                            newop=[]
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor1":[' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num-(numero/numero2)
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num-(numero/numero2)
                                                elif '"Valor2":[' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num-(numero/numero2)
                                                else:
                                                    newop.append(linea)
                                            print("==================")
                                            print(newop)
                                            texto=""
                                            archivo.close()
                                            break

                                    else:
                                        texto = texto+datos+"\n"
                                

                            else:
                                a=(valores.replace(const,""))
                                if counter == 0:
                                    num = float(a.rstrip())
                                    counter=1
                                else:
                                    num = num-float(a.rstrip())
                    print("\n Resultado de la resta: \n"+str(num))
                    file.close()
                    text=""
                elif '"Operacion":"Multiplicacion"' in text:
                    remove("operacion.txt")
                    file = open("operacion.txt", "w")
                    file.write(text)
                    file.close()
                    counter=0
                    print("\n MULTIPLICACIÓN \n")
                    digit = 1
                    num = 0
                    file = open("operacion.txt", "r")
                    for valores in file:
                        const = '"Valor'+str(digit)+'":'
                        if const in valores:
                            digit = digit+1
                            print(valores.rstrip())
                            texto = ""
                            if const+"[" in valores.replace(" ",""):
                                for datos in file:
                                    if "[" in datos:
                                        texto = texto+datos+"\n"
                                    if "]" in datos:
                                        texto = texto+datos+"\n"
                                        remove("operacionNew.txt")
                                        archivo = open("operacionNew.txt", "w")
                                        archivo.write(texto)
                                        archivo.close()

                                        digito = 1
                                        archivo = open("operacionNew.txt","r")
                                        if '"Operacion":"Seno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num*float(math.sin(numero))
                                            texto=""
                                            archivo.close()
                                            break
                                        
                                        elif '"Operacion":"Potencia"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":[' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":[' in linea:
                                                    print("We're in")
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num*(numero**numero2)
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Raiz"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num*(numero**(1/numero2))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Coseno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num*float(math.cos(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Tangente"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num*float(math.tan(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Inverso"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = (1/numero)
                                                    num = num*numero
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Mod"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num*(numero%numero2)
                                            texto=""
                                            archivo.close()
                                            break

                                    else:
                                        texto = texto+datos+"\n"
                                

                            else:
                                a=(valores.replace(const,""))
                                if counter == 0:
                                    num = float(a.rstrip())
                                    counter=1
                                else:
                                    num = num*float(a.rstrip())
                    print("\n Resultado de la multiplicación: \n"+str(num))
                    file.close()
                    text=""

                elif '"Operacion":"Division"' in text:
                    remove("operacion.txt")
                    file = open("operacion.txt", "w")
                    file.write(text)
                    file.close()
                    counter=0
                    print("\n DIVISION \n")
                    digit = 1
                    num = 0
                    file = open("operacion.txt", "r")
                    for valores in file:
                        const = '"Valor'+str(digit)+'":'
                        if const in valores:
                            digit = digit+1
                            print(valores.rstrip())
                            texto = ""
                            if const+"[" in valores.replace(" ",""):
                                for datos in file:
                                    if "[" in datos:
                                        texto = texto+datos+"\n"
                                    if "]" in datos:
                                        texto = texto+datos+"\n"
                                        remove("operacionNew.txt")
                                        archivo = open("operacionNew.txt", "w")
                                        archivo.write(texto)
                                        archivo.close()

                                        digito = 1
                                        archivo = open("operacionNew.txt","r")
                                        if '"Operacion":"Seno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num/float(math.sin(numero))
                                            texto=""
                                            archivo.close()
                                            break
                                        
                                        elif '"Operacion":"Potencia"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                    print(numero)
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num/(numero**numero2)
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Raiz"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num/(numero**(1/numero2))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Coseno"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num/float(math.cos(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Tangente"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = numero*(math.pi/180)
                                                    num = num/float(math.tan(numero))
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Inverso"' in texto:
                                            for linea in archivo:
                                                if '"Valor'+str(digito)+'":' in linea:
                                                    numero = float(linea.replace('"Valor'+str(digito)+'":',""))
                                                    numero = (1/numero)
                                                    num = num/numero
                                            texto=""
                                            archivo.close()
                                            break

                                        elif '"Operacion":"Mod"' in texto:
                                            for linea in archivo:
                                                if '"Valor1":' in linea:
                                                    a=(linea.replace('"Valor1":',""))
                                                    numero = float(a.rstrip())
                                                elif '"Valor2":' in linea:
                                                    a=(linea.replace('"Valor2":',""))
                                                    numero2 = float(a.rstrip())
                                                    num = num/(numero%numero2)
                                            texto=""
                                            archivo.close()
                                            break
                                    else:
                                        texto = texto+datos+"\n"
                                

                            else:
                                a=(valores.replace(const,""))
                                if counter == 0:
                                    num = float(a.rstrip())
                                    counter=1
                                else:
                                    num = num/float(a.rstrip())
                    print("\n Resultado de la división: \n"+str(num))
                    file.close()
                    text=""

            else:
                text= text+linea+"\n"
                for error in errores:
                    if error in linea:
                        print("Error ",error)
    
    var2="a2"
    dot.node(var2,"OH YES",{"color":"red","style":"filled","shape":"box"})
    dot.edge(var1,var2)
    print(dot.source)
    r=open("entrys/Report.txt","w")
    r.write(dot.source)
    r.close()
    system("dot -Tpdf entrys/Report.txt -o entrys/Report.pdf")