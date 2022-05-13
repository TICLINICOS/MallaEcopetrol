# Server Name: DESKTOP-QF6AULF
import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-QF6AULF;DATABASE=test1;Trusted_Connection=yes;')
    print("Conexion exitosa")
except Exception as ex:
    print(ex)
# finally:
#     connection.close()    
#     print("Conexion Finalizada")

#Consulta en la base de datos

cursor = connection.cursor()
cursor.execute("SELECT * FROM persona;")

personas = cursor.fetchall()

for persona in personas:
    print (persona)

cursor.close()
connection.close()