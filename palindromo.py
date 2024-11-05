import tkinter as tk
from tkinter import messagebox
import re

class MaquinaDeTuring:
    def __init__(self, cadena):
        self.cadena = self.limpiar_cadena(cadena)  # Limpiar la cadena
        self.tamano = len(self.cadena)
        self.indice_izquierda = 0
        self.indice_derecha = self.tamano - 1

    def limpiar_cadena(self, cadena):
        # Eliminar caracteres especiales, acentos y espacios, y convertir a minúsculas
        # Primero eliminamos los acentos
        cadena = cadena.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        cadena = cadena.replace('Á', 'a').replace('É', 'e').replace('Í', 'i').replace('Ó', 'o').replace('Ú', 'u')
        # Luego eliminamos caracteres no alfanuméricos
        cadena = re.sub(r'[^a-zA-Z0-9]', '', cadena)
        return cadena.lower()  # Convertir a minúsculas

    def es_palindromo(self):
        while self.indice_izquierda < self.indice_derecha:
            if self.cadena[self.indice_izquierda] != self.cadena[self.indice_derecha]:
                return False
            self.indice_izquierda += 1
            self.indice_derecha -= 1
        return True

def verificar_palindromo():
    frase = entrada.get()
    maquina = MaquinaDeTuring(frase)
    if maquina.es_palindromo():
        messagebox.showinfo("Resultado", f"La frase \"{frase}\" es un palíndromo.")
    else:
        messagebox.showinfo("Resultado", f"La frase \"{frase}\" no es un palíndromo.")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Verificador de Palíndromos - Máquina de Turing")
ventana.geometry("400x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresa una palabra o frase:")
etiqueta.pack(pady=10)

# Entrada de texto
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=10)

# Botón para verificar
boton = tk.Button(ventana, text="Verificar", command=verificar_palindromo)
boton.pack(pady=20)

# Iniciar la aplicación
ventana.mainloop()
