#!/usr/bin/env python3
import cgi
import mysql.connector

# Función para modificar los datos de un usuario
def modificar_usuario(valores):
    try:
        # conexión con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="valentin",
            password="123456789",
            database="biblioteca"
        )

        cursor = conexion.cursor()

        # Obtengo los datos del formulario
        id_usuario = valores["id_usuario"].value
        nuevo_nombre = valores["nuevo_nombre"].value
        nuevo_email = valores["nuevo_email"].value
        nueva_direccion = valores["nueva_direccion"].value

        # Realizo la actualización en la base de datos
        cursor.execute("UPDATE usuario SET nombre = %s, correo = %s, direccion = %s WHERE idusuario = %s", (nuevo_nombre, nuevo_email, nueva_direccion, id_usuario))

        # Confirmo la operación
        conexion.commit()

        cursor.close()

        # Redirecciono de vuelta a este script después de modificar
        print("Content-type: text/html")
        print("Location: mostrar.py")
        print()

    except Exception as e:
        print("Content-type: text/html")
        print()
        print(f"Error: {e}")

# Obtengo los datos del formulario y realizo la operación de modificación
datos = cgi.FieldStorage()
if "id_usuario" in datos and "nuevo_nombre" in datos and "nuevo_email" in datos and "nueva_direccion" in datos:
    modificar_usuario(datos)

# codigo HTML para el formulario de modificación de usuario
print("Content-type: text/html\n")
print("""
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modificar Usuario</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <header>
            <h1>Modificar Usuario</h1>
        </header>
        <main>
            <form action="modif.py" method="post" class="user-form">
                <div class="form-group">
                    <label for="id_usuario">ID del Usuario a Modificar:</label>
                    <input type="number" id="id_usuario" name="id_usuario" required>
                </div>
                <div class="form-group">
                    <label for="nuevo_nombre">Nuevo Nombre:</label>
                    <input type="text" id="nuevo_nombre" name="nuevo_nombre" required>
                </div>
                <div class="form-group">
                    <label for="nuevo_email">Nuevo Email:</label>
                    <input type="email" id="nuevo_email" name="nuevo_email" required>
                </div>
                <div class="form-group">
                    <label for="nueva_direccion">Nueva Direccion:</label>
                    <input type="text" id="nueva_direccion" name="nueva_direccion" required>
                </div>
                <div class="form-group">
                    <button type="submit" class="btn btn-warning">Modificar Usuario</button>
                </div>
            </form>
        </main>
        <footer>
            <a href="mostrar.py" class="btn btn-primary">Volver a la Lista de Usuarios</a>
        </footer>
    </div>
</body>
</html>
""")
