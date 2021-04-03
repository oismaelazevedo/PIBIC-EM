<?php
session_start();
ob_start();
require_once("funcao/conexao.php");
//unset($_SESSION['escolhido'] );
?>
<!DOCTYPE html>
<html>
<header><meta http-equiv="Content-Type" content="text/html; charset=euc-jp">
        
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="Marcus Paulo de Q. Amorim">

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
            <h3 class="panel-title"><?php echo "Nome: ".$_SESSION['nome']."</br>";?></h3>
        </div>
        <div class="panel-body">
            <div class="row">
                <div class="col-md-7" style="border-left:1px solid #ccc;height:300px">
                    <fieldset>
                        <div class="spacing"><br/></div>

                        
                        <?php
                            //consulta as resposta da rodada
                            $rodada = $_SESSION['rodada'];

                            $PDO = CriarConexao();
                            $sql = "SELECT * FROM `usuarios`, `respostas` WHERE `respostas`.`id_user` = `usuarios`.`id` and `respostas`.`rodada` = :rodada";

                            $consulta = $PDO->prepare($sql);
                            $consulta->bindParam(":rodada",$rodada);
                            $consulta->execute();

                            $total = $consulta->rowCount();
                            $questao = 0;
                            //echo "Total: ".$total."</br>";
                            ?>
                            <table border="1px">
                                
                                            <tr>
                                                <th style="width:50px;">Questão</th>
                                                <th style="width:50px;">E1</th>
                                                <th style="width:50px;">E2</th>
                                                <th style="width:50px;">E3</th>
                                                <th style="width:50px;">E4</th>
                                                <th style="width:50px;">E5</th>
                                                <th style="width:50px;">E6</th>
                                                <th style="width:50px;">E7</th>
                                                <th style="width:250px;">Correta 1</th>
                                                <th style="width:250px;">Correta 2</th>
                                                <th style="width:50px;">Acertou</th>

                                            </tr>

                            <?php

                            while($total > 0){
                                $questao = $questao +1;
                                $linha = $consulta->fetch(PDO::FETCH_ASSOC);
                                $nome = $linha['nome'];
                                //$questao = $linha['questao'];
                                $minterms0 = $linha['minterms0'];
                                $minterms1 = $linha['minterms1'];
                                $minterms2 = $linha['minterms2'];
                                $minterms3 = $linha['minterms3'];
                                $minterms4 = $linha['minterms4'];
                                $minterms5 = $linha['minterms5'];
                                $minterms6 = $linha['minterms6'];
                                $correta1 = $linha['correta1'];
                                $correta2 = $linha['correta2'];
                                $correta = $linha['correta'];

                                
                                ?>

                                            <tr>
                                                <td style="width:50px;"><?php echo $questao; ?></td>
                                                <td style="width:50px;"><?php echo $minterms0; ?></td>
                                                <td style="width:50px;"><?php echo $minterms1; ?></td>
                                                <td style="width:50px;"><?php echo $minterms2; ?></td>
                                                <td style="width:50px;"><?php echo $minterms3; ?></td>
                                                <td style="width:50px;"><?php echo $minterms4; ?></td>
                                                <td style="width:50px;"><?php echo $minterms5; ?></td>
                                                <td style="width:50px;"><?php echo $minterms6; ?></td>
                                                <td style="width:250px;"><?php echo $correta1; ?></td>
                                                <td style="width:250px;"><?php echo $correta2; ?></td>
                                                <td style="width:50px;"><?php echo $correta; ?></td>
                                            </tr>
 

                                <?php
                                
                                $total = $total -1;
                            }
                            
                        ?>
                            </table>
                        <?php session_destroy();?>
                        <a href="index.php" class="btn btn-info btn-sm pull-right">Finalizar</a>
                    </fieldset>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>

