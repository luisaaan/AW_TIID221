<?php
/*creamos una funcion llamada conectar*/
function conectar(){
    /* info del servidor */
    $host = "localhost";
    $user = "root";
    $pass = "";

    /*base de datos*/
    $db = "aw221";

    /*permitir conectarnos a MySQL*/
    $con = mysqli_connect($host,$user,$pass);

    /*le vamos a decir que BD y la información de con*/
    mysqli_select_db($con,$db);

    return $con;
}
?>