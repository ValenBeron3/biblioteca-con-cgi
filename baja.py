#!/usr/bin/env python3
import cgi
import mysql.connector

# Función para dar de baja a un usuario
def dar_de_baja_usuario(valores):
    try:
        # conexión con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="valentin",
            password="123456789",
            database="biblioteca"
        )

        cursor = conexion.cursor()

        # Obtengo el ID del usuario a dar de baja
        id_usuario = valores["id_usuario"].value

        # Realizo la eliminación en la base de datos con la consulta correspondiente
        cursor.execute("DELETE FROM usuario WHERE idusuario = %s", (id_usuario,))

        # Confirmo la operación
        conexion.commit()

        cursor.close()

        # Redirecciono de vuelta a este script después de eliminar
        print("Content-type: text/html")
        print("Location: mostrar.py")
        print()

    except Exception as e:
        print("Content-type: text/html")
        print()
        print(f"Error: {e}")

# Obtengo los datos del formulario y realizo la operación de baja
datos = cgi.FieldStorage()
if "id_usuario" in datos:
    dar_de_baja_usuario(datos)

# codigo HTML para el formulario de baja de usuario
print("Content-type: text/html\n")
print("""
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dar de Baja Usuario</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <header>
            <h1>Dar de Baja Usuario</h1>
        </header>
        <main>
            <form action="baja.py" method="post" class="user-form">
                <div class="form-group">
                    <label for="id_usuario">ID del Usuario a Dar de Baja:</label>
                    <input type="number" id="id_usuario" name="id_usuario" required>
                </div>
                <div class="form-group">
                    <button type="submit" class="btn btn-danger">Dar de Baja Usuario</button>
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
