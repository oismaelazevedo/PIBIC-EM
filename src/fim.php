<?php
session_start();
ob_start();
require_once("funcao/conexao.php");
//unset($_SESSION['escolhido'] );
?>
<!DOCTYPE html>
<html>
<header>
    <meta http-equiv="Content-Type" content="text/html; charset=euc-jp">

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Ismael Carlos S. da C. de Azevedo">
    <meta name="author" content="Estevão Vitor G. Naval">
    <meta name="author" content="Kawan P. de Santana">

    <!-- Estilo CSS -->
    <!--<link href="css/estilo.css" rel="stylesheet">  -->

    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <!--<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/css/materialize.min.css">-->
    <!------ Include the above in your HEAD tag ---------->

    <link href='http://fonts.googleapis.com/css?family=Raleway:500' rel='stylesheet' type='text/css'>
    <!-- Estilo CSS -->
    <link href="css/inicial.css" rel="stylesheet">
</header>

<body>
    <div class="middlePage">
        <div class="relative">
            <h1 class="logo">Resultado!</h1>
        </div>
        <div class="panel panel-info" class="col-md-10">
            <div class="panel-heading">
                <h3 class="panel-title"><?php echo "Nome: " . $_SESSION['nome'] . "</br>"; ?></h3>
            </div>
            <div class="panel-body">
                <div class="row">
                    <div class="col-md-7" style="border-left:1px solid #ccc;display:flex; flex-direction: row; justify-content: center; align-items: center">
                        <fieldset>
                            <div class="spacing"><br /></div>


                            <?php
                            //consulta as resposta da rodada
                            $rodada = $_SESSION['rodada'];

                            $PDO = CriarConexao();
                            $sql = "SELECT nome, resposta, selecionada, correta FROM `usuarios`, `resposta` WHERE `resposta`.`id_user` = `usuarios`.`id` and `resposta`.`rodada` = :rodada";

                            $consulta = $PDO->prepare($sql);
                            $consulta->bindParam(":rodada", $rodada);
                            $consulta->execute();

                            $total = $consulta->rowCount();
                            $questao = 0;
                            //echo "Total: ".$total."</br>";
                            ?>
                            <table border="1px">

                                <tr>
                                    <th style="width:50px;">Questão</th>
                                    <th style="width:250px;">Correta</th>
                                    <th style="width:250px;">Selecionada</th>
                                    <th style="width:50px;">Acertou</th>

                                </tr>

                                <?php

                                while ($total > 0) {
                                    $questao = $questao + 1;
                                    $linha = $consulta->fetch(PDO::FETCH_ASSOC);
                                    $nome = $linha['nome'];
                                    //$questao = $linha['questao'];
                                    $correta = $linha['resposta'];
                                    $selec = $linha['selecionada'];
                                    $conclusao = $linha['correta'];

                                ?>

                                    <tr>
                                        <td style="width:50px;"><?php echo $questao; ?></td>
                                        <td style="width:50px;"><?php echo $correta; ?></td>
                                        <td style="width:50px;"><?php echo $selec; ?></td>
                                        <td style="width:50px;"><?php echo $conclusao; ?></td>
                                    </tr>


                                <?php

                                    $total = $total - 1;
                                }

                                ?>
                            </table>
                            <br>
                            <p>
                                <strong>Total de acertos:</strong> <?php ?>
                            </p>
                            <a href="funcao/logout.php" class="btn btn-info btn-sm pull-right">Finalizar</a>
                        </fieldset>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>

</html>