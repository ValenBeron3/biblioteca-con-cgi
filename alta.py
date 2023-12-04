#!/usr/bin/env python3
import cgi
import mysql.connector

# Función para agregar un nuevo usuario

def agregar_usuario(valores):
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
        nombre = valores["nombre"].value
        email = valores["email"].value
        direccion = valores["direccion"].value

        # Realizo la inserción en la base de datos con la consulta
        cursor.execute("INSERT INTO usuario (nombre, correo, direccion) VALUES (%s, %s, %s)", (nombre, email, direccion))

        # Confirmo la operación
        conexion.commit()

        cursor.close()

        # Redirecciono de vuelta a este script después de agregar
        
        print("Content-type: text/html")
        print("Location: mostrar.py")
        print()

    except Exception as e:
        print("Content-type: text/html")
        print()
        print(f"Error: {e}")

# Obtengo los datos del formulario y realizo la operación de alta
datos = cgi.FieldStorage()
if "nombre" in datos and "email" in datos and "direccion" in datos:
    agregar_usuario(datos)

# codigo HTML para el formulario de alta de usuario


print("Content-type: text/html\n")
print("""
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alta de Usuario</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <header>
            <h1>Alta de Usuario</h1>
        </header>
        <main>
            <form action="alta.py" method="post" class="user-form">
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" name="nombre" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
      
                <div class="form-group">
                    <label for="direccion">Direccion:</label>
                    <input type="text" id="direccion" name="direccion" required>
                </div>
      
                <div class="form-group">
                    <button type="submit" class="btn btn-success">Agregar Usuario</button>
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

