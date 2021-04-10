<?php
//INICIO A SESSÃO
session_start();
ob_start();
?>

<!DOCTYPE html>
<html>
<header>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Ismael Carlos S. da C. de Azevedo">
    <meta name="author" content="Estevão Vitor G. Naval">
    <meta name="author" content="Kawan P. de Santana">

    <title>Introdução a Informática</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <!-- Estilo CSS -->
    <link href="css/estilo.css" rel="stylesheet">
    <!-- jQuery -->
    <script src="js/jquery.js"></script>
    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</header>

<body>

    <?php

    require_once("funcao/conexao.php");

    //Início função para calcular tempo de resposta
    date_default_timezone_set('America/Sao_Paulo');
    $hora_final = date('H:i:s');
    function calculaTempo($hora_inicial, $hora_final)
    {
        $i = 1;
        $tempo_total;
        $tempos = array($hora_final, $hora_inicial);

        foreach ($tempos as $tempo) {
            $segundos = 0;
            list($h, $m, $s) = explode(':', $tempo);
            $segundos += $h * 3600;
            $segundos += $m * 60;
            $segundos += $s;

            $tempo_total[$i] = $segundos;
            $i++;
        }
        $segundos = $tempo_total[1] - $tempo_total[2];

        $horas = floor($segundos / 3600);
        $segundos -= $horas * 3600;
        $minutos = str_pad((floor($segundos / 60)), 2, '0', STR_PAD_LEFT);
        $segundos -= $minutos * 60;
        $segundos = str_pad($segundos, 2, '0', STR_PAD_LEFT);

        global $tempo_gasto;
        $tempo_gasto = "$horas:$minutos:$segundos";
    }
    //Final função para calcular tempo de resposta

    $hora_inicial = $_POST["hora_inicial"];
    $arquivo = $_POST["arquivo"];
    $obs = $_POST["obs"];
    $ip = $_SERVER["REMOTE_ADDR"];
    $id_usuario = $_SESSION['id_usuario'];
    $rodada = $_SESSION['rodada'];

    calculaTempo($hora_inicial, $hora_final);

    $acertou = 0;
    $errou = 0;

    //Pega as informações do arquivo
    $info = file_get_contents($arquivo);
    $lendo = json_decode($info, true);

    if (!empty($_POST["letra"])) {
        $letra_resp_user = $_POST["letra"];
        $letra_correta = $lendo["atributosquestao"][0]["respostascorretas"];


        if ($letra_resp_user == $letra_correta) {

            $_SESSION["contador"] = $_SESSION["contador"] + 1;
            $_SESSION["correto"] = "Sim";
            
        } else if ($letra_resp_user != $letra_correta) {

            $_SESSION["contador"] = $_SESSION["contador"] + 1;
            $_SESSION["correto"] = "Não";
        }
        switch ($letra_resp_user) {
            case "A":
                $indice = 0;
                break;
            case "B":
                $indice = 1;
                break;
            case "C":
                $indice = 2;
                break;
            case "D":
                $indice = 3;
                break;
            case "E":
                $indice = 4;
                break;
        }

        $tipoerro = $lendo["respostas"][$indice]["tipoerro"];
        $secorreta = $_SESSION["correto"];

        $PDO = CriarConexao();
        $sql = "INSERT INTO resposta(rodada, id_user, questao, selecionada, resposta, correta, tipoerro, obs, tempo_gasto, ip) VALUES 
                                (:rodada, :id_usuario, :arquivo, :letra_resp_user, :letra_correta, :secorreta,
                                 :tipoerro, :obs, :tempo_gasto, :ip)";

        $consulta = $PDO->prepare($sql);

        $consulta->bindParam(":rodada", $rodada);
        $consulta->bindParam(":id_usuario", $id_usuario);
        $consulta->bindParam(":arquivo", $arquivo);
        $consulta->bindParam(":letra_resp_user", $letra_resp_user);
        $consulta->bindParam(":letra_correta", $letra_correta);
        $consulta->bindParam(":secorreta", $secorreta);
        $consulta->bindParam(":tipoerro", $tipoerro);
        $consulta->bindParam(":obs", $obs);
        $consulta->bindParam(":tempo_gasto", $tempo_gasto);
        $consulta->bindParam(":ip", $ip);

        $consulta->execute();

        header("Location: index5.php");

        unset($_SESSION['info']);
    } else {

        $_SESSION["contador"] = $_SESSION["contador"];
        $_SESSION['info'] = $arquivo;
        $_SESSION["correto"] = "Vazio";
        header("Location: index5.php");
    }

    if (count($_SESSION["escolhido"]) == 10) {
        unset($_SESSION["contador"]);
        header("Location: fim.php");
    }

    ?>
</body>

</html>