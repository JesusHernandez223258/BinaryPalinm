#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import tkinter as tk
from tkinter import messagebox

# Función para generar palíndromos
def generar_palindromo(numero, palindromo):
    pal = ""

    if numero > 1:
        numero -= 2
        for i in palindromo:
            if i != "s":
                pal += i
            else:
                opc = random.randint(0, 1)
                if opc:
                    pal += "0s0"
                else:
                    pal += "1s1"
        return generar_palindromo(numero, pal)
    else:
        eps = False
        for j in palindromo:
            if j != "s":
                pal += j
            else:
                opc = random.randint(1, 3)
                if opc == 1:
                    pal += "0"
                elif opc == 2:
                    pal += "1"
                else:
                    eps = True
                    continue
        if eps:
            pal += "    Se agregó la cadena vacía ε"
        return pal

# Función para verificar si una cadena es palíndromo
def es_palindromo(cadena):
    return cadena == cadena[::-1]

# Función principal para controlar la interfaz
def main(option):
    with open("Historial.txt", "a") as historial:
        if option == 1:  # Generar palíndromo con un número aleatorio
            size = random.randint(1, 20)
            palindrome = generar_palindromo(size, "s")
            result_text.set("El palíndromo generado es: " + palindrome)
            historial.write("El palíndromo generado es: " + palindrome + "\n")

        elif option == 2:  # Generar palíndromo con un tamaño específico
            try:
                size = int(entry_size.get())
                if size < 1:
                    messagebox.showerror("Error", "El número debe ser mayor que 0.")
                    return
                palindrome = generar_palindromo(size, "s")
                result_text.set("El palíndromo generado es: " + palindrome)
                historial.write("El palíndromo generado es: " + palindrome + "\n")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa un número válido.")
                
        elif option == 3:  # Verificar si una cadena ingresada es palíndromo
            cadena = entry_palindrome.get()
            if es_palindromo(cadena):
                result_text.set("La cadena ingresada ES un palíndromo.")
            else:
                result_text.set("La cadena ingresada NO es un palíndromo.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador y Verificador de Palíndromos")
root.geometry("400x400")

# Título
label_title = tk.Label(root, text="--PROGRAMA DE GENERACIÓN Y VERIFICACIÓN DE PALÍNDROMOS--", font=("Arial", 14), pady=10)
label_title.pack()

# Opciones para generar
button_random = tk.Button(root, text="Generar cadena con número aleatorio", command=lambda: main(1), font=("Arial", 12))
button_random.pack(pady=5)

label_size = tk.Label(root, text="Tamaño de la cadena:", font=("Arial", 12))
label_size.pack(pady=5)

entry_size = tk.Entry(root, font=("Arial", 12), width=10)
entry_size.pack(pady=5)

button_generate = tk.Button(root, text="Generar cadena con tamaño ingresado", command=lambda: main(2), font=("Arial", 12))
button_generate.pack(pady=5)

# Opciones para verificar
label_palindrome = tk.Label(root, text="Ingrese una cadena para verificar:", font=("Arial", 12))
label_palindrome.pack(pady=5)

entry_palindrome = tk.Entry(root, font=("Arial", 12), width=20)
entry_palindrome.pack(pady=5)

button_verify = tk.Button(root, text="Verificar si es palíndromo", command=lambda: main(3), font=("Arial", 12))
button_verify.pack(pady=5)

# Resultado
result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text, font=("Arial", 12), pady=20, wraplength=350)
label_result.pack()

# Botón para salir
button_exit = tk.Button(root, text="Salir", command=root.quit, font=("Arial", 12))
button_exit.pack(pady=10)

root.mainloop()
