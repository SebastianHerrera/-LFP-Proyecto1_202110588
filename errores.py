from os import remove

def errors(filename):
    errores = ["#","$","%","&","(",")","*","+","/","^","@","!","¡","?","¿"]
    with open(filename,mode="r") as archivo:
        text = ""
        counter = 0
        count = 0
        text=text+"{\n"
        for linea in archivo:
            counter=counter+1
            for error in errores:
                if error in linea:
                    count = count+1
                    text=text+'{\n"No.":'+str(count)+"\n"+'"Descripcion-Token":{\n'+'"Lexema":'+error+"\n"+'"Tipo":Error\n'+'"Linea":'+str(counter)+"\n}\n}\n"
        text=text+"}"
        try:
                    remove("ERRORES_202110588.txt")
                    file = open("ERRORES_202110588.txt", "w")
                    file.write(text)
                    file.close()

        except:
            file = open("ERRORES_202110588.txt", "w")
            file.write(text)
            file.close()