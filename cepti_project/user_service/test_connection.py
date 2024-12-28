import psycopg2
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv('DATABASE_URL')

try:
    # Establecer la conexión a la base de datos utilizando la URL cargada desde el .env
    conn = psycopg2.connect(DATABASE_URL)
    print("Conexión exitosa a PostgreSQL!")

    # Crear un cursor para realizar operaciones con la base de datos
    cur = conn.cursor()

    # Realizar una consulta simple para verificar la conexión
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    print("Resultado de la consulta:", result)

    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()

except Exception as e:
    print(f"Error al conectar a PostgreSQL: {e}")
