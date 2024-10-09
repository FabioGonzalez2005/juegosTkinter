import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Juego:
    def __init__(self, nombre):
        self.nombre = nombre

class PiedraPapelTijera(Juego):
    def __init__(self, root):
        super().__init__("Piedra, papel o tijera")
        self.root = root
        self.ventana = tk.Toplevel(self.root)
        self.ventana.title(self.nombre)
        self.ventana.geometry("400x400")

        self.canvas = tk.Canvas(self.ventana, width=400, height=400)
        self.canvas.pack()

        self.crear_fondo('fondoPPT.jpeg')

        self.titulo = ttk.Label(self.canvas, text="Escoge una opción:", background='lightgrey')
        self.canvas.create_window(200, 50, window=self.titulo)

        self.resultado_label = ttk.Label(self.canvas, text="", background='lightgrey')
        self.canvas.create_window(200, 100, window=self.resultado_label)

        self.boton_piedra = ttk.Button(self.canvas, text="Piedra", command=lambda: self.elegir_opcion(0))
        self.canvas.create_window(100, 280, window=self.boton_piedra)

        self.boton_papel = ttk.Button(self.canvas, text="Papel", command=lambda: self.elegir_opcion(1))
        self.canvas.create_window(200, 280, window=self.boton_papel)

        self.boton_tijera = ttk.Button(self.canvas, text="Tijera", command=lambda: self.elegir_opcion(2))
        self.canvas.create_window(300, 280, window=self.boton_tijera)

    def elegir_opcion(self, opcion_jugador):
        opcion_computadora = random.randint(0, 2)
        opciones_nombres = ["Piedra", "Papel", "Tijera"]
        self.resultado_label.config(text=f"Computadora eligió: {opciones_nombres[opcion_computadora]}")

        if opcion_jugador == opcion_computadora:
            mensaje = "Es un empate."
            messagebox.showinfo("¡Empate!", mensaje)
            self.resultado_label.config(text=mensaje)
        elif (opcion_jugador == 0 and opcion_computadora == 2) or (opcion_jugador == 1 and opcion_computadora == 0) or (opcion_jugador == 2 and opcion_computadora == 1):
            mensaje = f"¡Ganaste! {opciones_nombres[opcion_jugador]} gana a {opciones_nombres[opcion_computadora]}."
            messagebox.showinfo("¡Ganaste!", mensaje)
            self.resultado_label.config(text=mensaje)
        else:
            mensaje = f"Perdiste. {opciones_nombres[opcion_computadora]} gana a {opciones_nombres[opcion_jugador]}."
            messagebox.showinfo("Perdiste", mensaje)
            self.resultado_label.config(text=mensaje)

        self.ventana.destroy()
        self.root.deiconify()

    def crear_fondo(self, imagen_fondo):
        img = Image.open(imagen_fondo)
        img = img.resize((400, 400))
        fondo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=fondo)
        self.canvas.image = fondo

    def iniciar(self):
        self.root.withdraw()
        self.ventana.mainloop()
        self.root.deiconify()

class PalabrasEnIngles(Juego):
    def __init__(self, root):
        super().__init__("Palabras en inglés")
        self.root = root
        self.palabras = {
            "cat": "gato",
            "dog": "perro",
            "house": "casa",
            "car": "coche",
            "apple": "manzana",
            "book": "libro",
            "sun": "sol",
            "moon": "luna",
            "water": "agua",
            "fire": "fuego",
            "tree": "árbol",
            "flower": "flor",
            "computer": "computadora",
            "phone": "teléfono",
            "sky": "cielo",
            "mountain": "montaña",
            "river": "río",
            "bread": "pan",
            "milk": "leche",
            "cheese": "queso"
        }

        self.ventana = tk.Toplevel(self.root)
        self.ventana.title(self.nombre)
        self.ventana.geometry("400x300")

        self.canvas = tk.Canvas(self.ventana, width=400, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.crear_fondo('fondoPEI.jpeg')

        self.palabra_label = ttk.Label(self.canvas, text="", font=("Arial", 16), background='lightgrey')
        self.canvas.create_window(200, 80, window=self.palabra_label)

        self.traduccion_entry = ttk.Entry(self.canvas, font=("Arial", 14))
        self.canvas.create_window(200, 120, window=self.traduccion_entry)

        self.boton_comprobar = tk.Button(self.canvas, text="Comprobar", command=self.comprobar_traduccion, bg='lightgrey', borderwidth=0)
        self.canvas.create_window(200, 160, window=self.boton_comprobar)

        self.resultado_label = ttk.Label(self.canvas, text="", font=("Arial", 14), background='lightgrey')
        self.canvas.create_window(200, 200, window=self.resultado_label)

        self.puntaje = 0
        self.intentos = 5
        self.iniciar_juego()

    def crear_fondo(self, imagen_fondo):
        img = Image.open(imagen_fondo)
        img = img.resize((400, 300))
        self.fondo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.fondo)

    def iniciar_juego(self):
        self.palabra_aleatoria = random.choice(list(self.palabras.keys()))
        self.palabra_label.config(text=self.palabra_aleatoria)
        self.traduccion_entry.delete(0, tk.END)
        self.resultado_label.config(text="")

    def comprobar_traduccion(self):
        respuesta = self.traduccion_entry.get().lower()
        traduccion_correcta = self.palabras[self.palabra_aleatoria]

        if respuesta == traduccion_correcta:
            self.puntaje += 1
            messagebox.showinfo("¡Correcto!", "¡Bien hecho!")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta es '{traduccion_correcta}'.")

        self.intentos -= 1
        if self.intentos == 0:
            messagebox.showinfo("Fin del juego", f"Tu puntaje final es {self.puntaje}/{5}.")
            self.ventana.destroy()
            self.root.deiconify()
        else:
            self.iniciar_juego()

    def iniciar(self):
        self.root.withdraw()
        self.ventana.mainloop()
        self.root.deiconify()

class AdivinaElNumero(Juego):
    def __init__(self, root):
        super().__init__("Adivina el número")
        self.root = root
        self.ventana = tk.Toplevel(self.root)
        self.ventana.title(self.nombre)
        self.ventana.geometry("400x400")

        self.numero_secreto = random.randint(0, 200)
        self.intentos = 0

        self.canvas = tk.Canvas(self.ventana, width=400, height=400)
        self.canvas.pack()

        self.crear_fondo('fondoAEN.jpeg')

        self.instrucciones_label = ttk.Label(self.canvas, text="Adivina un número entre 0 y 200.", background='lightgrey')
        self.canvas.create_window(200, 50, window=self.instrucciones_label)

        self.intento_entry = ttk.Entry(self.canvas)
        self.canvas.create_window(200, 100, window=self.intento_entry)

        self.comprobar_button = ttk.Button(self.canvas, text="Comprobar", command=self.comprobar_numero)
        self.canvas.create_window(200, 150, window=self.comprobar_button)

        self.resultado_label = ttk.Label(self.canvas, text="", background='lightgrey')
        self.canvas.create_window(200, 200, window=self.resultado_label)

    def comprobar_numero(self):
        try:
            valor_jugador = int(self.intento_entry.get())
            self.intentos += 1

            if valor_jugador < 0 or valor_jugador > 200:
                messagebox.showwarning("Advertencia", "Por favor, ingresa un número entre 0 y 200.")
                return

            if valor_jugador == self.numero_secreto:
                self.resultado_label.config(text="¡Correcto!")
                messagebox.showinfo("Resultado", "¡Has adivinado el número!")
                self.ventana.destroy()
                self.root.deiconify()
            elif self.intentos >= 3:
                self.resultado_label.config(text=f"¡Perdiste! El número era {self.numero_secreto}.")
                messagebox.showinfo("Resultado", f"¡Perdiste! El número era {self.numero_secreto}.")
                self.ventana.destroy()
                self.root.deiconify()
            else:
                if valor_jugador < self.numero_secreto:
                    self.resultado_label.config(text="¡El número secreto es mayor!")
                else:
                    self.resultado_label.config(text="¡El número secreto es menor!")

        except ValueError:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un número válido.")

    def crear_fondo(self, imagen_fondo):
        img = Image.open(imagen_fondo)
        img = img.resize((400, 400))
        fondo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=fondo)
        self.canvas.image = fondo

    def iniciar(self):
        self.root.withdraw()
        self.ventana.mainloop()
        self.root.deiconify()

class JuegoPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Juegos de Fabio")
        self.root.geometry("350x350")

        self.canvas = tk.Canvas(self.root, width=350, height=350)
        self.canvas.pack()
        self.crear_fondo('fondo.jpeg')

        self.titulo_main = ttk.Label(self.canvas, text="Escoge un juego:", background='lightgrey')
        self.canvas.create_window(175, 50, window=self.titulo_main)

        self.boton_ppt = ttk.Button(self.canvas, text="Piedra, papel o tijera.", command=self.jugar_ppt)
        self.canvas.create_window(175, 120, window=self.boton_ppt)

        self.boton_palabras = ttk.Button(self.canvas, text="Palabras en inglés.", command=self.jugar_palabras)
        self.canvas.create_window(175, 160, window=self.boton_palabras)

        self.boton_adivina = ttk.Button(self.canvas, text="Adivina el número", command=self.jugar_adivina)
        self.canvas.create_window(175, 200, window=self.boton_adivina)

    def crear_fondo(self, imagen_fondo):
        img = Image.open(imagen_fondo)
        img = img.resize((350, 350))
        fondo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=fondo)
        self.canvas.image = fondo

    def jugar_ppt(self):
        juego = PiedraPapelTijera(self.root)
        juego.iniciar()

    def jugar_palabras(self):
        juego = PalabrasEnIngles(self.root)
        juego.iniciar()

    def jugar_adivina(self):
        juego = AdivinaElNumero(self.root)
        juego.iniciar()

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = JuegoPrincipal()
    app.iniciar()