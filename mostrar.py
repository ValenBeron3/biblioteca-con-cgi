#!/usr/bin/env python3
import cgi
import mysql.connector

# Conexión a la base de datos y consulta a la misma
conexion = mysql.connector.connect(host="localhost", user="valentin", password="123456789", database="biblioteca")
cursor1 = conexion.cursor()
cursor1.execute("select * from usuario")

# codigo HTML para mostrar la tabla de usuarios
tabla_usuarios_html = """
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
<div class="container">
    <div class="row">
        <div class="col">
            <h1>Tabla de Usuarios</h1>
        </div>
        <div class="col text-end">
            <a class="btn btn-primary" href="alta.py">Alta de Usuario</a>
            <a class="btn btn-danger" href="baja.py">Dar de Baja Usuario</a>
            <a class="btn btn-success" href="modif.py">Modificar Usuario</a>
        </div>
    </div>
    <table class="table table-bordered">
        <tr><th>ID</th><th>Nombre</th><th>Email</th><th>Dirección</th></tr>
"""

# Generar filas de la tabla con datos de la base de datos
for cuadro in cursor1:
    tabla_usuarios_html += "<tr>"
    for dato in cuadro:
        tabla_usuarios_html += f'<td>{dato}</td>'
    tabla_usuarios_html += "</tr>"

# Cierro tabla y el cuerpo del HTML
tabla_usuarios_html += "</table></div></body></html>"

# Imprimo el codigo HTML completo con la tabla de usuarios y sus datos
print("Content-type: text/html\n")
print(tabla_usuarios_html)

# Cierro la conexión a la base de datos
cursor1.close()

