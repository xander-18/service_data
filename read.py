import pandas as pd

# Especifica el nombre del archivo y las hojas que deseas leer
# file_path = 'studientsMorning.xlsx'
file_path = 'studientsAfter.xlsx'
# sheets_to_read = ['3A']
# sheets_to_read = ['3B']
# sheets_to_read = ['3C']
# sheets_to_read = ['3D']
# sheets_to_read = ['3E']
# sheets_to_read = ['3F']
# sheets_to_read = ['3G']
# sheets_to_read = ['3H']
# sheets_to_read = ['3I']
# sheets_to_read = ['3J']
# sheets_to_read = ['3K']
# sheets_to_read = ['3L']
# sheets_to_read = ['4A']
# sheets_to_read = ['4B']
# sheets_to_read = ['4C']
# sheets_to_read = ['4D']
# sheets_to_read = ['4E']
# sheets_to_read = ['4F']
# sheets_to_read = ['4G']
# sheets_to_read = ['4H']
# sheets_to_read = ['4I']
# sheets_to_read = ['4J']
# sheets_to_read = ['5A']
# sheets_to_read = ['5B']
# sheets_to_read = ['5C']
# sheets_to_read = ['5D']
# sheets_to_read = ['5E']
# sheets_to_read = ['5F']
# sheets_to_read = ['5G']
# sheets_to_read = ['5H']
# sheets_to_read = ['5I']
# sheets_to_read = ['5J']
# sheets_to_read = ['1A']
# sheets_to_read = ['1B']
# sheets_to_read = ['1B']
# sheets_to_read = ['1C']
# sheets_to_read = ['1D']
# sheets_to_read = ['1E']
# sheets_to_read = ['1G']
# sheets_to_read = ['1H']
# sheets_to_read = ['1I']
# sheets_to_read = ['1J']
# sheets_to_read = ['1K']
# sheets_to_read = ['1L']
# sheets_to_read = ['1M']
# sheets_to_read = ['2A']
# sheets_to_read = ['2B']
# sheets_to_read = ['2C']
# sheets_to_read = ['2D']
# sheets_to_read = ['2E']
# sheets_to_read = ['2F']
# sheets_to_read = ['2G']
# sheets_to_read = ['2H']
# sheets_to_read = ['2I']
# sheets_to_read = ['2J']
# sheets_to_read = ['2K']
# sheets_to_read = ['2L']
sheets_to_read = ['2M']

# Leer las hojas específicas
dfs = pd.read_excel(file_path, sheet_name=sheets_to_read, engine='openpyxl', header=4)

# Mostrar solo la columna de nombres y apellidos para cada hoja
for sheet_name, df in dfs.items():
    print(f"\nLista de estudiantes de la hoja '{sheet_name}':")
    
    # Usar el nombre exacto de la columna que vemos en los datos y filtrar valores no nulos
    nombres = df['Unnamed: 1'].dropna()
    
    # Obtener la lista de nombres válidos, reemplazando las comas por espacios
    nombres_validos = [nombre.strip().replace(", ", " ") for nombre in nombres if isinstance(nombre, str)]
    
    # Imprimir todos los nombres excepto el último con coma al final
    for nombre in nombres_validos[:-1]:
        print(f'"{nombre}",')
    
    # Imprimir el último nombre sin coma al final
    if nombres_validos:
        print(f'"{nombres_validos[-1]}"')