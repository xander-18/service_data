import mysql.connector
from mysql.connector import Error


def crear_tabla_estudiantes(conexion):
    try:
        cursor = conexion.cursor()
        tabla_sql = """
        CREATE TABLE IF NOT EXISTS estudiantes_tarde (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombres_apellidos VARCHAR(255) NOT NULL,
            grado VARCHAR(10),
            seccion VARCHAR(5),
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(tabla_sql)
        conexion.commit()
        print("Tabla creada exitosamente")

    except Error as e:
        print(f"Error al crear la tabla: {e}")


def insertar_estudiantes(conexion):
    # Lista de estudiantes

    estudiantes = [
"ALVARADO SALAS JAIRO DANIEL",       
"ALVARES ROSARIO LUIS",
"AMBROSIO PAUCAR MARICIELO",
"BENANCIO BAZAN ALEX ELOY",
"CALDERON CAMARA YUSSER",
"CORNELIO MORALES PEDRO JOSE",       
"CUELLAR TACUCHE ANAHY VICTORIA",    
"DOMINGUEZ CRUZ NAYELI ZARHA",       
"ESPINOZA ORTIZ YEISON JUNIOR",      
"JUSTO FLORES ANYI ESTEFA",
"LAURENCIO BEJARANO SARAI NIKOL",    
"MAJINO SISLEY ARIANO MATIAS",       
"MENDOZA DOMINGUEZ PIERO ARON",      
"MISAICO NAZARIO NATHALY LYZ",       
"MORALES ALBINO CRISTOFER ALEXANDER",
"MORALES CASTAÑEDA YHENYFER LUZ",    
"ORTIZ ISIDRO YANELA EVA",
"RAMOS ENCARNACION DELLY ODDETTDE",
"REYES ROJAS YISELA FELICIANA",
"REYES VALENTIN JAN PAUL",
"ROMERO ALEJANDRO NOE",
"SALAZAR LAYA ROSANGEL ANDREA",
"SALAZAR TEODORO ESKARLETH KARLA",
"SANTIAGO CATALINO LUZ ARIANA",
"SARMIENTO ALCEDO NATHANIEL ANYELA",
"TIBURCIO PINEDA ANYELINA ALEXANDRA",
"TOLENTINO MAUTINO LUZ MARIELA",
"TORRES FERNANDEZ JHEYSON MICHELL"
    ]

    try:
        cursor = conexion.cursor()
        # SQL para insertar estudiantes
        sql = """
        INSERT INTO estudiantes_tarde 
        (nombres_apellidos, grado, seccion)
        VALUES (%s, %s, %s)
        """

        # Insertar cada estudiante
        for estudiante in estudiantes:
            valores = (
                estudiante,
                "2",
                "M",
            )  # Ajusta el grado y sección según necesites
            cursor.execute(sql, valores)

        conexion.commit()
        print(f"Se insertaron {len(estudiantes)} estudiantes exitosamente")

    except Error as e:
        print(f"Error al insertar estudiantes: {e}")


# Conexión principal
try:
    bd = mysql.connector.connect(
        host="127.0.0.1", user="root", password="", database="pruebas"
    )

    if bd.is_connected():
        print("Conectado a la base de datos")

        # Crear tabla si no existe
        crear_tabla_estudiantes(bd)

        # Insertar estudiantes
        insertar_estudiantes(bd)

except Error as e:
    print(f"Error: {e}")

finally:
    if bd.is_connected():
        bd.close()
        print("Conexión cerrada")
