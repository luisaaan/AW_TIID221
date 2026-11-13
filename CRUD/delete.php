<?php

/* incluir la información del archivo conexion.php */
include("conexion.php");

/* mandamos a llamar la funcion conectar para ejecutarla */
$con = conectar();

/* recibimos el id enviado por la url */
$id = $_GET['id'];

/* eliminamos al alumno de la tabla */
$sql = "DELETE FROM alumnos WHERE id = '$id'";

/* Ejecutar la consulta */
$query = mysqli_query($con, $sql);

if($query){
    Header("Location: alumnos.php");
    echo "Alumno eliminado";
    exit();
}else{
    echo "Error al eliminar al alumno";
}

?>