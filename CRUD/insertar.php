<?php

/* incluir la información del archivo conexion.php */
include("conexion.php");

/* mandamos a llamar la funcion conectar para ejecutarla */
$con = conectar();

/* recibir la info del formulario */
$matricula = $_POST['matricula'];
$nombre = $_POST['nombre'];
$apellido_p = $_POST['apellido_p'];
$apellido_m = $_POST['apellido_m'];
$edad = $_POST['edad'];

/* Crear nuestra consulta para insertar los datos en la db*/
$sql = "INSERT INTO alumnos (matricula, nombre, apellido_p, apellido_m, edad) 
VALUES ('$matricula', '$nombre', '$apellido_p', '$apellido_m', '$edad')";

/* Ejecutar la consulta */
$query = mysqli_query($con, $sql);

if($query){
    Header("Location: alumnos.php");
    echo "Alumno insertado";
}else{
    echo "Error al insertar al alumno";
}

?>