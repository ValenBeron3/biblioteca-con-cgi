import cgi
import mysql.connector

conexion=mysql.connector.connect(host="localhost",user="valentin",password="123456789",database="biblioteca")
cursor1=conexion.cursor()
cursor1.execute("select * from usuario")

print("Content-type: text/html")


print("""
<html>
      <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
      </head>
      <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <h1>Tabla de Usuarios</h1>
        <table class="table table bordered">
        <tr><th>ID</th><th>Nombre</th><th>Email</th><th>Direccion</th></tr>""")
for cuadro in cursor1:
    print("<tr>")
    for dato in cuadro:
        print(f'<td>{dato}</td>')
    print("</tr>")
print("</body>")

  
print("</table>")

cursor1.close()
