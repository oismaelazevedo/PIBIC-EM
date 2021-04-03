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
    <meta name="author" content="Marcus Paulo de Q. Amorim">

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
    <!--inicia a mensagem do segundo erro3-->
    <div class="modal fade" id="erro3">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Incorreta Novamente</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>As questões possuem apenas uma opção correta!</p>
                </div>
                <div class="modal-footer">

                    <a href="index5.php" onclick="$('#erro3').modal('hide')"><button type="button" class="btn btn-primary">Próxima Questão</button></a>
                </div>
            </div>
        </div>
    </div>
    <!--finaliza a mensagem do primeiro erro3-->
    <!--inicia a mensagem do segundo erro2-->
    <div class="modal fade" id="erro2">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Incorreta Novamente</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Vamos tentar uma outra questão</p>
                </div>
                <div class="modal-footer">

                    <a href="index5.php" onclick="$('#erro2').modal('hide')"><button type="button" class="btn btn-primary">Próxima Questão</button></a>
                </div>
            </div>
        </div>
    </div>
    <!--finaliza a mensagem do primeiro erro-->
    <!--inicia a mensagem do acerto-->
    <div class="modal fade" id="acerto">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Correto</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Parabéns. Você acertou!</p>
                </div>
                <div class="modal-footer">

                    <a href="index5.php" onclick="$('#acerto').modal('hide')"><button type="button" class="btn btn-primary">Próxima Questão</button></a>
                </div>
            </div>
        </div>
    </div>
    <!--finaliza a mensagem do acerto-->

    <?php

    include "conexao.php";

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

    if (isset($_POST["letra"])) {

        $letra_resp_user = $_POST["letra"];
        
        $letra_correta = $lendo["atributosquestao"][0]["respostascorretas"];

        if ($letra_resp_user == $letra_correta) {
            $resp_corr = "Sim";
        } else {
            $resp_corr = "Não";
        }

            
        if ($resp_corr == "Sim") {
            unset($_SESSION['info']);
            unset($_SESSION['primatent']);
    ?>
            <!--chamando modal acerto-->
            <script>
                $('#acerto').modal({
                    backdrop: 'static',
                    keyboard: false
                });
            </script>
    <?php
        } elseif ($resp_corr == "Não") {
            $resp_corr = "Não";
            $_SESSION['info'] = $arquivo;
            $_SESSION['primatent'];
            header("Location: index5.php");
            ?>
            <script>
                $('#erro3').modal({
                    backdrop: 'static',
                    keyboard: false
                });
            </script>
    <?php
        }
    }


    $sql = "INSERT INTO respostas(rodada, id_user, questao, resposta, correta, selecionada, tipoerro, obs, tempo_gasto, ip) VALUE 
                            ($rodada, $id_usuario, '$arquivo', '$resp_correta', '$resp_corr', 
                            '$selecionada', '$tipoerro', '$obs', '$tempo_gasto', '$ip')";
    $sql_gravar = mysqli_query($mysqli, $sql1);

    //echo $qtd_resp;

    //Verifica se todas as questões já foram selecionadas
    if (count($_SESSION["escolhido"]) == 10) {
        //echo "<script  language=javascript>alert('escolhido - ']');</script>";
        header("Location: fim.php");
    }

    ?>

</body>

</html>