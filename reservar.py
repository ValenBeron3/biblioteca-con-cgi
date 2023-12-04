
#!/usr/bin/env python3
import cgi
import mysql.connector

# Conexión a la base de datos y consulta a la misma
conexion = mysql.connector.connect(host="localhost", user="valentin", password="123456789", database="biblioteca")
cursor1 = conexion.cursor()
cursor1.execute("select * from libro")

# Función para reservar un libro
def reservar_libro(valores):
    try:
        # conexión con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="valentin",
            password="123456789",
            database="biblioteca"
        )

        cursor = conexion.cursor()

        # Obtengo el ID del libro a reservar
        id_libro = valores["id_libro"].value

        # Realizo la selección en la base de datos con la consulta correspondiente
        cursor.execute("SELECT * FROM libro WHERE idlibro = %s", (id_libro,))
        libro = cursor.fetchone()

        if libro:
            # Verificar si el libro está disponible para reservar
            if libro[id_libro] == 'disponible':  # Aquí asumo que la columna del estado del libro está en la posición 1
                # Actualizar el estado del libro a "reservado"
                consulta_actualizar = "UPDATE `biblioteca`.`libro` SET `estado` = 'reservado' WHERE (`libro_idlibro` = '%s', (id_libro,));"
                cursor.execute(consulta_actualizar, (id_libro,))
                conexion.commit()
                print("El libro ha sido reservado exitosamente.")
            else:
                print("El libro no está disponible para reservar.")
        else:
            print("No se encontró ningún libro con ese ID.")

        # Cerrar la conexión a la base de datos
        conexion.close()

        # Redirecciono de vuelta a este script después de reservar
        print("Content-type: text/html")
        print("Location: biblio.py")
        print()

    except Exception as e:
        print("Content-type: text/html")
        print()
        print(f"Error: {e}")

# Obtengo los datos del formulario y realizo la operación de baja
datos = cgi.FieldStorage()
if "id_libro" in datos:
    reservar_libro(datos)

print("Content-type: text/html\n")
print("""
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reserva de Libro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <header>
            <h1>Reserva de Libro</h1>
        </header>
        <main>
            <form action="reservar.py" method="post" class="user-form">
                <div class="form-group">
                    <label for="nombre">Id libro</label>
                    <input type="text" id="id_libro" name="id_libro" required>
                </div>

                <div class="form-group">
                    <button type="submit" class="btn btn-success">Reservar libro</button>
                </div>
            </form>
        </main>
        <footer>
            <a href="libros.py" class="btn btn-primary">Volver a la lista de libros</a>
            <a href="biblio.py" class="btn btn-primary">Volver a la pagina principal</a>
        </footer>
    </div>
</body>
</html>
""")
