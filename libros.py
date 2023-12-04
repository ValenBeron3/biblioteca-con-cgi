#!/usr/bin/env python3
import cgi
import mysql.connector

# Conexión a la base de datos y consulta a la misma
conexion = mysql.connector.connect(host="localhost", user="valentin", password="123456789", database="biblioteca")
cursor1 = conexion.cursor()
cursor1.execute("select * from libro")
    
# HTML para la tabla de libros
tabla_libros_html = """
<table class="table table-bordered">
    <thead>
        <tr>
            <th>ID Libro</th>
            <th>Condicion</th>
            <th>Nombre</th>
            <th>Editorial</th>
            <th>Ano de Lanzamiento</th>
            <th>ID Autor</th>
            <th>Estado</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
"""

for libro in cursor1:
    libro_id, condicion, nombre, editorial, ano_lanzamiento, autor_id, estado = libro  # Ajusta esto según tu estructura de tabla
    tabla_libros_html += f"""
        <tr>
            <td>{libro_id}</td>
            <td>{condicion}</td>
            <td>{nombre}</td>
            <td>{editorial}</td>
            <td>{ano_lanzamiento}</td>
            <td>{autor_id}</td>
            <td>{estado}</td>
            <td>
                <form action="reservar.py" method="post">
                    <input type="hidden" name="id_libro" value="{libro_id}">
                    <button type="submit" class="btn btn-primary">Reservar <a href="reservar.py"</a></button>
                </form>
            </td>
        </tr>
    """

tabla_libros_html += """
    </tbody>
</table>
"""

# Imprimir el HTML completo
print("Content-type: text/html\n")
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Libros</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-5">
        <h1>Lista de Libros</h1>
        <td>Recuerda el numero de "ID libro" para poder reservar! </td>
        {tabla_libros_html}
        <footer>
            <a href="biblio.py" class="btn btn-primary">Volver a la pagina principal</a>
        </footer>   
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</body>
</html>
""")
