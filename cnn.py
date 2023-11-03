import pyodbc

# Define la cadena de conexión a SQL Server
# Reemplaza 'ServerName', 'DatabaseName', 'Username' y 'Password' con tus valores reales
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=VANQUISH\\SQLTESTER;"
    "DATABASE=chatdatabase;"
    "UID=sa;"
    "PWD=PandaRey_2023;"
)

try:
    # Conectar a la base de datos de SQL Server
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    print("Conexión exitosa a SQL Server")

    # Ejecutar una consulta SQL simple
    cursor.execute("SELECT * FROM Clientes")

    # Recorrer los resultados de la consulta
    """ for row in cursor.fetchall():
        print(row) """

except pyodbc.Error as e:
    print(f"Error al conectar o ejecutar la consulta en SQL Server: {str(e)}")
finally:
    # Asegurarse de cerrar la conexión, independientemente del resultado
    connection.close()
