#!/usr/bin/env python3
import cgi
import mysql.connector

# Conexión a la base de datos y consulta a la misma
conexion = mysql.connector.connect(host="localhost", user="valentin", password="123456789", database="biblioteca")
cursor1 = conexion.cursor()
cursor1.execute("select * from libro")

# HTML para el menú
menu_html = """
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="index.py">Biblioteca</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="libros.py">Libros</a>
                </li>
                <!-- Agrega más opciones de menú según tus necesidades -->
            </ul>
        </div>
    </div>
</nav>
"""

# HTML para la pantalla principal con imágenes ilustrativas
libros = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biblioteca</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body>
    <header>
        {menu}
    </header>
    <main class="container mt-5">
        <h1 class="text-center">Bienvenido a la Biblioteca Virtual</h1>
        <p class="lead text-center">Reserva tu libro !</p>
        <div>

        </div>
    </main>
    <footer class="text-center mt-5">
        <p>&copy; 2023 Biblioteca</p>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</body>
</html>
""".format(menu=menu_html)

# Imprimir el HTML completo
print("Content-type: text/html\n")
print(libros)
