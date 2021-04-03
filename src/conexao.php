<?php
$servidor = "localhost";
$usuario1 = "root";
$senha1 = "";
$banco = "pibic";

// Conecta-se ao banco de dados MySQL
$mysqli = new mysqli($servidor, $usuario1, $senha1, $banco);

$mysqli->query("SET NAMES 'utf8'");
$mysqli->query("SET character_set_connection=utf8");
$mysqli->query("SET character_set_client=utf8");
$mysqli->query("SET character_set_results=utf8");
?>