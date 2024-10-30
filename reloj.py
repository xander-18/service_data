import tkinter as tk
from datetime import datetime

# Crear la ventana principal
root = tk.Tk()
root.title("Reloj en Tiempo Real")

# Configuración de la etiqueta para mostrar la hora
reloj_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
reloj_label.pack(padx=50, pady=50)

# Función para actualizar el reloj en tiempo real
def actualizar_reloj():
    hora_actual = datetime.now().strftime("%I:%M:%S %p")  # Hora en formato AM/PM con segundos
    reloj_label.config(text=hora_actual)
    root.after(1000, actualizar_reloj)  # Actualiza cada segundo

# Iniciar la actualización del reloj
actualizar_reloj()

# Ejecutar el bucle principal de la ventana
root.mainloop()
