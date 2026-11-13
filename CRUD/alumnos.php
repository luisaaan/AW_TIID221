<?php

/* incluir la información del archivo conexion.php */
include("conexion.php");

/* mandamos a llamar la funcion conectar para ejecutarla */
$con = conectar();

/*dame todo lo que tengas de alumnos*/
$sql = "SELECT * FROM alumnos";

/* ejecutar la consulta y tendremos acceso a la conexión */
$query = mysqli_query($con,$sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table{
            width: 100%;
            text-align: center;
        }
        .contenedor{
            display: grid;
            grid-template-columns: 20% 60% 20%;
            margin: 30px;
            padding: 30px;
        }
        .form-control{
            width: 150px;
            height: 20px;
            margin: 10px;
        }
    </style>
</head>
<body>
    <div class="contenedor">
        <div class="div1"></div>
        <div class="div2">
            <table border="2">
                <thead>
                    <tr>
                        <th><h2>ID</h2></th>
                        <th><h2>Matricula</h2></th>
                        <th><h2>Nombre</h2></th>
                        <th><h2>Apellido Paterno</h2></th>
                        <th><h2>Apellido Materno</h2></th>
                        <th><h2>Edad</h2></th>
                        <th><h2>Acciones</h2></th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                        while($row = mysqli_fetch_array($query)){
                    ?>
                    <tr>
                        <td><h3><?php echo $row['id']; ?></h3></td>
                        <td><h3><?php echo $row['matricula']; ?></h3></td>
                        <td><h3><?php echo $row['nombre']; ?></h3></td>
                        <td><h3><?php echo $row['apellido_p']; ?></h3></td>
                        <td><h3><?php echo $row['apellido_m']; ?></h3></td>
                        <td><h3><?php echo $row['edad']; ?></h3></td>
                        <th>
                            <h3>
                                <a href="delete.php?id=<?php echo $row['id']; ?>">Eliminar</a>
                                <br>
                                <a href="edit.php?id=<?php echo $row['id']; ?>">Editar</a>
                            </h3>
                        </th>
                    </tr>
                    <?php
                        }
                    ?>
                </tbody>
            </table>
            <h1>FORMULARIO</h1>
            <form action="insertar.php" method="POST">
                <input type="text" class="form-control" name="matricula" placeholder="Matrícula">
                <input type="text" class="form-control" name="nombre" placeholder="Nombre">
                <input type="text" class="form-control" name="apellido_p" placeholder="Apellido Paterno">
                <input type="text" class="form-control" name="apellido_m" placeholder="Apellido Materno">
                <input type="text" class="form-control" name="edad" placeholder="Edad">
                <button type="submit">Guardar</button>
            </form>

        </div>
        <div class="div3"></div>
    </div>
</body>
</html>