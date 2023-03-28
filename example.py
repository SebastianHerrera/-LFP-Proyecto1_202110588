from os import remove
import math
from customtkinter import *
from tkinter import*


with open("entrada.txt","r+") as archivo:
    operacion = ""
    for linea in archivo:
        if "{" in linea:
            operacion = operacion+linea
