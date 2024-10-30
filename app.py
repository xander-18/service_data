import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from tkinter import simpledialog
import webbrowser
import requests
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import io
import mysql.connector
# Definición de variables globales
usuarios = ["admin", "user1", "user2"]
alumnos = ["Alumno 1", "Alumno 2", "Alumno 3"]
auxiliares = ["Auxiliar 1", "Auxiliar 2", "Auxiliar 3"]
reportes = []

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pruebas"
    )
    cursor = conexion.cursor()
    print("se conecto correctamente")
except mysql.connector.Error as err:
    print(f"Error no se conecto con la base de datos:{err}")
    conexion = None
# Funciones para manejar enlaces a redes sociales
def abrir_facebook():
    webbrowser.open("https://www.facebook.com/ieensmhco")


def abrir_twitter():
    webbrowser.open("https://twitter.com/ieensmhco")


def abrir_instagram():
    webbrowser.open("https://www.instagram.com/ieensmhco")


# URL de la imagen
url_imagen = "https://scontent.fhuu1-1.fna.fbcdn.net/v/t39.30808-6/419116578_897131662422370_3250676543048656656_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=E3XXyAu_94gQ7kNvgEP5ER-&_nc_ht=scontent.fhuu1-1.fna&_nc_gid=AZ4VHAjd4W1J_NsEmatWC9L&oh=00_AYA-OFnw6zQtOn2VT6UuX3BewDkl21NT5q8loKAgbEgqnQ&oe=66F9521A"


# Función para cargar la imagen de fondo
def cargar_imagen(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        return ImageTk.PhotoImage(image)
    except requests.exceptions.RequestException as e:
        print(f"Error al cargar la imagen: {e}")
        return None
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return None


# Función para mostrar la hora en formato AM/PM
def actualizar_reloj():
    # hora_actual = datetime.now().strftime("%I:%M %p")  # Hora en formato AM/PM
    hora_actual = datetime.now().strftime("%I:%M:%S %p")  # Hora en formato AM/PM con segundos
    reloj_label.config(text=hora_actual)
    root.after(1000, actualizar_reloj)  # Actualiza cada segundo


# Función para cargar la imagen de fondo
def cargar_imagen(url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(io.BytesIO(image_data))
    return ImageTk.PhotoImage(image)


# Función para abrir el formulario de registro de asistencia de alumnos

def mostrar_alumnos():
    if conexion is None:
        messagebox.showerror("Error", "No hay conexión con la base de datos")
        return
        
    alumnos_window = tk.Toplevel(root)
    alumnos_window.title("Lista de Alumnos")
    alumnos_window.geometry("800x600")
    alumnos_window.configure(bg="#D3E4CD")

    # Título
    titulo_label = tk.Label(
        alumnos_window,
        text="Lista de Alumnos Registrados",
        font=("Helvetica", 14, "bold"),
        bg="#D3E4CD",
        fg="#2E4A62"
    )
    titulo_label.pack(pady=10)

    # Frame para el Treeview
    frame = ttk.Frame(alumnos_window)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Crear Treeview
    tree = ttk.Treeview(frame)
    tree["columns"] = ("ID", "Nombre y Apellidos", "Grado", "Seccion")

    # Configurar columnas
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("ID", anchor=tk.CENTER, width=100)
    tree.column("Nombre y Apellidos", anchor=tk.W, width=150)
    tree.column("Grado", anchor=tk.CENTER, width=100)
    tree.column("Seccion", anchor=tk.CENTER, width=100)

    # Configurar encabezados
    tree.heading("#0", text="")
    tree.heading("ID", text="ID", anchor=tk.CENTER)
    tree.heading("Nombre y Apellidos", text="Nombre", anchor=tk.CENTER)
    tree.heading("Grado", text="Grado", anchor=tk.CENTER)
    tree.heading("Seccion", text="Sección", anchor=tk.CENTER)

    # Agregar scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(fill="both", expand=True)

    try:
        # Ejecutar consulta SQL
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, nombres_apellidos, grado, seccion 
            FROM estudiantes
        """)
        
        # Insertar datos en el Treeview
        for alumno in cursor.fetchall():
            tree.insert("", "end", values=alumno)

        # Mostrar total de alumnos
        total_label = tk.Label(
            alumnos_window,
            text=f"Total de alumnos: {tree.get_children().__len__()}",
            font=("Helvetica", 10),
            bg="#D3E4CD",
            fg="#2E4A62"
        )
        total_label.pack(pady=10)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al obtener los datos: {err}")
def agregar_boton_mostrar_alumnos():
    # Crear el botón en el bottom_frame existente
    btn_mostrar_alumnos = tk.Button(
        text="Mostrar Alumnos",
        command=mostrar_alumnos,
        font=("Helvetica", 12, "bold"),
        bg="#2196F3",
        fg="white"
    )
    btn_mostrar_alumnos.pack(side="left", padx=10)

# Llamar a esta función después de crear bottom_frame en abrir_aplicacion_usuario()
agregar_boton_mostrar_alumnos()     
        
def abrir_formulario_asistencia_alumnos():
    asistencia_window = tk.Toplevel(root)
    asistencia_window.title("Registrar Asistencia de Alumnos")
    asistencia_window.geometry("600x400")
    asistencia_window.configure(bg="#D3E4CD")

    # Título del formulario
    titulo_label = tk.Label(
        asistencia_window,
        text="Registrar Asistencia de Alumnos",
        font=("Helvetica", 14, "bold"),
        bg="#D3E4CD",
        fg="#2E4A62",
    )
    titulo_label.pack(pady=10)

    # Frame para organizar los campos
    frame = tk.Frame(asistencia_window, bg="#D3E4CD")
    frame.pack(pady=20)

    # Selección de grado
    tk.Label(
        frame, text="Grado:", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    ).grid(row=0, column=0, sticky="e", padx=10, pady=5)
    grados = ["Primero", "Segundo", "Tercero", "Cuarto", "Quinto"]
    grado_combobox = ttk.Combobox(frame, values=grados, state="readonly")
    grado_combobox.grid(row=0, column=1, padx=10, pady=5)

    # Selección de sección
    tk.Label(
        frame, text="Sección:", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    ).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    secciones = ["A", "B", "C", "D"]
    seccion_combobox = ttk.Combobox(frame, values=secciones, state="readonly")
    seccion_combobox.grid(row=1, column=1, padx=10, pady=5)

    # Lista de alumnos
    tk.Label(
        frame, text="Alumnos:", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    ).grid(row=2, column=0, sticky="e", padx=10, pady=5)
    lista_alumnos = ttk.Combobox(frame, values=alumnos, state="readonly")
    lista_alumnos.grid(row=2, column=1, padx=10, pady=5)

    # Selección de fecha
    tk.Label(
        frame, text="Fecha:", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    ).grid(row=3, column=0, sticky="e", padx=10, pady=5)
    fecha_calendario = DateEntry(
        frame, width=12, background="darkblue", foreground="white", borderwidth=2
    )
    fecha_calendario.grid(row=3, column=1, padx=10, pady=5)

    # Recuadro para mostrar la información de la asistencia
    info_label = tk.Label(
        asistencia_window, text="", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    )
    info_label.pack(pady=10)

    # Función para marcar asistencia
    def marcar_asistencia():
        alumno = lista_alumnos.get()
        fecha = fecha_calendario.get_date()
        if alumno:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            asistencia_info = f"Asistencia marcada para {alumno} el {fecha} a las {fecha_hora.split()[1]}"
            info_label.config(text=asistencia_info)
            reportes.append(asistencia_info)  # Guardar reporte de asistencia
        else:
            messagebox.showerror("Error", "Por favor, selecciona un alumno")

    # Botón para registrar asistencia
    btn_registrar = tk.Button(
        frame,
        text="Marcar Asistencia",
        command=marcar_asistencia,
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50",
        fg="white",
    )
    btn_registrar.grid(row=4, columnspan=2, pady=10)


# Función para abrir el formulario de registro de asistencia de auxiliares
def abrir_formulario_asistencia_auxiliares():
    asistencia_window = tk.Toplevel(root)
    asistencia_window.title("Registrar Asistencia de Auxiliares")
    asistencia_window.geometry("600x400")
    asistencia_window.configure(bg="#D3E4CD")

    # Título del formulario
    titulo_label = tk.Label(
        asistencia_window,
        text="Registrar Asistencia de Auxiliares",
        font=("Helvetica", 14, "bold"),
        bg="#D3E4CD",
        fg="#2E4A62",
    )
    titulo_label.pack(pady=10)

    # Frame para organizar los campos
    frame = tk.Frame(asistencia_window, bg="#D3E4CD")
    frame.pack(pady=20)

    # Lista de auxiliares
    tk.Label(
        frame, text="Auxiliares:", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    ).grid(row=0, column=0, sticky="e", padx=10, pady=5)
    lista_auxiliares = ttk.Combobox(frame, values=auxiliares, state="readonly")
    lista_auxiliares.grid(row=0, column=1, padx=10, pady=5)

    # Selección de fecha
    tk.Label(
        frame, text="Fecha:", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    ).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    fecha_calendario = DateEntry(
        frame, width=12, background="darkblue", foreground="white", borderwidth=2
    )
    fecha_calendario.grid(row=1, column=1, padx=10, pady=5)

    # Recuadro para mostrar la información de la asistencia
    info_label = tk.Label(
        asistencia_window, text="", font=("Helvetica", 10), bg="#D3E4CD", fg="#2E4A62"
    )
    info_label.pack(pady=10)

    # Función para marcar asistencia
    def marcar_asistencia():
        auxiliar = lista_auxiliares.get()
        fecha = fecha_calendario.get_date()
        if auxiliar:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            asistencia_info = f"Asistencia marcada para {auxiliar} el {fecha} a las {fecha_hora.split()[1]}"
            info_label.config(text=asistencia_info)
            reportes.append(asistencia_info)  # Guardar reporte de asistencia
        else:
            messagebox.showerror("Error", "Por favor, selecciona un auxiliar")

    # Botón para registrar asistencia
    btn_registrar = tk.Button(
        frame,
        text="Marcar Asistencia",
        command=marcar_asistencia,
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50",
        fg="white",
    )
    btn_registrar.grid(row=2, columnspan=2, pady=10)



# Función para abrir el panel de opciones del administrador
def abrir_panel_administrador():
    # Solicitar contraseña antes de abrir el panel
    contraseña = simpledialog.askstring(
        "Contraseña", "Por favor, ingrese la contraseña:", show="*"
    )

    # Verificar si la contraseña es correcta
    if contraseña == "admin123":  # Cambia "admin123" por la contraseña que desees
        admin_window = tk.Toplevel(root)
        admin_window.title("Opciones de Administrador")
        admin_window.geometry("600x400")
        admin_window.configure(bg="#D3E4CD")

        # Código para crear el panel de administrador...
    else:
        messagebox.showerror("Error", "Contraseña incorrecta.")
    # Título del panel
    titulo_label = tk.Label(
        admin_window,
        text="Opciones de Administrador",
        font=("Helvetica", 14, "bold"),
        bg="#D3E4CD",
        fg="#2E4A62",
    )
    titulo_label.pack(pady=10)

    # Frame para organizar los botones
    frame = tk.Frame(admin_window, bg="#D3E4CD")
    frame.pack(pady=20)

    # Botón para gestionar usuarios
    def gestionar_usuarios():
        admin_action_window = tk.Toplevel(admin_window)
        admin_action_window.title("Gestionar Usuarios")
        admin_action_window.geometry("400x300")
        admin_action_window.configure(bg="#D3E4CD")

        tk.Label(
            admin_action_window,
            text="Gestión de Usuarios",
            font=("Helvetica", 12, "bold"),
            bg="#D3E4CD",
            fg="#2E4A62",
        ).pack(pady=10)

        # Lista de usuarios
        usuario_listbox = tk.Listbox(admin_action_window)
        usuario_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        for usuario in usuarios:
            usuario_listbox.insert(tk.END, usuario)

        # Función para añadir un usuario
        def añadir_usuario():
            nuevo_usuario = entry_usuario.get()
            if nuevo_usuario:
                usuarios.append(nuevo_usuario)
                usuario_listbox.insert(tk.END, nuevo_usuario)
                entry_usuario.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario")

        # Función para eliminar un usuario
        def eliminar_usuario():
            seleccion = usuario_listbox.curselection()
            if seleccion:
                usuario_a_eliminar = usuario_listbox.get(seleccion[0])
                usuarios.remove(usuario_a_eliminar)
                usuario_listbox.delete(seleccion[0])
            else:
                messagebox.showerror("Error", "Por favor, selecciona un usuario")

        # Campo para añadir nuevo usuario
        tk.Label(
            admin_action_window,
            text="Nuevo Usuario:",
            font=("Helvetica", 10),
            bg="#D3E4CD",
            fg="#2E4A62",
        ).pack(pady=5)
        entry_usuario = tk.Entry(admin_action_window)
        entry_usuario.pack(pady=5)

        # Botones para añadir y eliminar usuarios
        tk.Button(
            admin_action_window,
            text="Añadir Usuario",
            command=añadir_usuario,
            font=("Helvetica", 10, "bold"),
            bg="#4CAF50",
            fg="white",
        ).pack(pady=5)
        tk.Button(
            admin_action_window,
            text="Eliminar Usuario",
            command=eliminar_usuario,
            font=("Helvetica", 10, "bold"),
            bg="#F44336",
            fg="white",
        ).pack(pady=5)

    tk.Button(
        frame,
        text="Gestionar Usuarios",
        command=gestionar_usuarios,
        font=("Helvetica", 12, "bold"),
        bg="#FFC107",
        fg="black",
    ).pack(pady=5)

    # Botón para ver reportes
    def ver_reportes():
        reportes_window = tk.Toplevel(admin_window)
        reportes_window.title("Ver Reportes")
        reportes_window.geometry("600x400")
        reportes_window.configure(bg="#D3E4CD")

        tk.Label(
            reportes_window,
            text="Reportes de Asistencia",
            font=("Helvetica", 12, "bold"),
            bg="#D3E4CD",
            fg="#2E4A62",
        ).pack(pady=10)

        # Mostrar reportes
        reportes_text = tk.Text(reportes_window, wrap=tk.WORD)
        reportes_text.pack(pady=10, fill=tk.BOTH, expand=True)
        for reporte in reportes:
            reportes_text.insert(tk.END, reporte + "\n")

    tk.Button(
        frame,
        text="Ver Reportes",
        command=ver_reportes,
        font=("Helvetica", 12, "bold"),
        bg="#03A9F4",
        fg="white",
    ).pack(pady=5)

    # Botón para ajustar configuraciones
    def ajustar_configuraciones():
        configuraciones_window = tk.Toplevel(admin_window)
        configuraciones_window.title("Ajustar Configuraciones")
        configuraciones_window.geometry("600x400")
        configuraciones_window.configure(bg="#D3E4CD")

        tk.Label(
            configuraciones_window,
            text="Ajustar Configuraciones",
            font=("Helvetica", 12, "bold"),
            bg="#D3E4CD",
            fg="#2E4A62",
        ).pack(pady=10)

        # Opciones de configuración
        tk.Label(
            configuraciones_window,
            text="Aquí puedes ajustar las configuraciones de la aplicación",
            bg="#D3E4CD",
            fg="#2E4A62",
        ).pack(pady=10)

    tk.Button(
        frame,
        text="Ajustar Configuraciones",
        command=ajustar_configuraciones,
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
    ).pack(pady=5)

    # Botón para ver registros de actividad
    def ver_registros():
        registros_window = tk.Toplevel(admin_window)
        registros_window.title("Ver Registros de Actividad")
        registros_window.geometry("600x400")
        registros_window.configure(bg="#D3E4CD")

        tk.Label(
            registros_window,
            text="Registros de Actividad",
            font=("Helvetica", 12, "bold"),
            bg="#D3E4CD",
            fg="#2E4A62",
        ).pack(pady=10)

        # Mostrar registros de actividad
        registros_text = tk.Text(registros_window, wrap=tk.WORD)
        registros_text.pack(pady=10, fill=tk.BOTH, expand=True)
        registros_text.insert(tk.END, "Aquí se mostrarán los registros de actividad.")

    tk.Button(
        frame,
        text="Ver Registros de Actividad",
        command=ver_registros,
        font=("Helvetica", 12, "bold"),
        bg="#9C27B0",
        fg="white",
    ).pack(pady=5)


# Función para abrir la aplicación principal para usuarios
def abrir_aplicacion_usuario():
    global root
    root = tk.Tk()
    root.title("IEE Nuestra Señora de las Mercedes - Huánuco")
    root.geometry("800x600")
    root.configure(bg="#D3E4CD")

    # Crear un frame para el título y el reloj
    top_frame = tk.Frame(root, bg="#D3E4CD")
    top_frame.pack(side="top", fill="x", pady=10)

    # Título de la aplicación
    titulo_label = tk.Label(
        top_frame,
        text="Bienvenido a la Aplicación de Registro de Asistencia",
        font=("Helvetica", 16, "bold"),
        bg="#D3E4CD",
        fg="#2E4A62",
    )
    titulo_label.pack(pady=10)

    # Reloj
    global reloj_label
    reloj_label = tk.Label(
        top_frame, text="", font=("Helvetica", 14), bg="#D3E4CD", fg="#2E4A62"
    )
    reloj_label.pack()

    # Crear un frame para los botones en la parte baja
    bottom_frame = tk.Frame(root, bg="#D3E4CD")
    bottom_frame.pack(side="bottom", fill="x", pady=10)

    # Botón para registrar asistencia de alumnos
    btn_asistencia_alumnos = tk.Button(
        bottom_frame,
        text="Registrar Asistencia de Alumnos",
        command=abrir_formulario_asistencia_alumnos,
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
    )
    btn_asistencia_alumnos.pack(side="left", padx=10)

    # Botón para registrar asistencia de auxiliares
    btn_asistencia_auxiliares = tk.Button(
        bottom_frame,
        text="Registrar Asistencia de Auxiliares",
        command=abrir_formulario_asistencia_auxiliares,
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50",
        fg="white",
    )
    btn_asistencia_auxiliares.pack(side="left", padx=10)

    # Botón especial solo para administradores, en la parte inferior derecha
    if "admin" in usuarios:
        btn_admin_options = tk.Button(
            bottom_frame,
            text="Opciones de Administrador",
            command=abrir_panel_administrador,
            font=("Helvetica", 12, "bold"),
            bg="#FF5722",
            fg="white",
        )
        btn_admin_options.pack(side="right", padx=10)

    # Enlaces a redes sociales
    social_frame = tk.Frame(root, bg="#D3E4CD")
    social_frame.pack(side="bottom", fill="x", pady=10)

    fb_button = tk.Button(
        social_frame,
        text="Facebook",
        command=abrir_facebook,
        font=("Helvetica", 10, "bold"),
        bg="#4267B2",
        fg="white",
    )
    fb_button.pack(side="left", padx=5)

    twitter_button = tk.Button(
        social_frame,
        text="Twitter",
        command=abrir_twitter,
        font=("Helvetica", 10, "bold"),
        bg="#1DA1F2",
        fg="white",
    )
    twitter_button.pack(side="left", padx=5)

    instagram_button = tk.Button(
        social_frame,
        text="Instagram",
        command=abrir_instagram,
        font=("Helvetica", 10, "bold"),
        bg="#C13584",
        fg="white",
    )
    instagram_button.pack(side="left", padx=5)

    actualizar_reloj()
    root.mainloop()


# Iniciar la aplicación
abrir_aplicacion_usuario()
