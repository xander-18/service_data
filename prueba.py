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
"AGUILAR CHAGUA ANGELLO LEONEL",    
"AGUILAR MORENO RODRIGO ALESSANDRO",
"AGUIRRE GONZALES DARLIN YEYSON",   
"ALVARADO LEON MELODY BRITNEY",     
"ALVAREZ LEIVA AVIGAIL",
"ARISTA TRUJILLO KELY CLARISA",     
"ARO ROBLES ALEJANDRO JAVIER",
"BERAUN JUSTO SAHORI LIZETH",
"CASIO HUAMAN CRISTIAN PAOLO",
"ESPINOZA MARTINEZ ROMEL",
"GAVINO ROBLES JHEYRO ALEJANDRO",
"GONZALES SALAZAR MOISES ARIEL",
"HILARIO URBANO MICHAEL DAYIRO",
"HURTADO FABIAN JORDAN ALEX",
"JUIPA BERRIOS ERIK NEYMAR",
"JUIPA SALAZAR JHANYURI NAIR",
"LAZARO PORTA LINDA ABIGAIL",
"LINO MINAYA LUIS ENRIQUE",
"MENDOZA NOLASCO EDILVERTO TIMOTEO",
"MORALES IBARRA JOSE SANTINO",
"OBREGON MENDOZA NICOLLE ASTRID",
"ORIZANO CAYCO NADIN RUBI",
"PUENTE SERRANO ROSMERY JIMENA",
"REYES QUISPE GIAN ALI",
"SARMIENTO CHAVEZ SHARON NOEMI",
"SILVESTRE GOMEZ SHARILEY LIZ",
"TRUJILLO CASTRO XIOMARA MAYLITH",
"TRUJILLO FIGUEREDO ESTRELLA LUCIA",
"TUCTO ESTEBAN YUNSU CIELO",
"VALENTIN NOLASCO ANGELO AGUSTIN",
"VILCA CECILIO JEAN JEREMIAS"
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
                "1",
                "B",
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
