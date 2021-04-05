<?php
//INICIO A SESSÃO
session_start();
ob_start();
session_unset($_SESSION);
$_SESSION['resperrada'] = 0;
?>

<!DOCTYPE html>
<html>
<header>
  <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="">
  <meta name="author" content="Marcus Paulo de Q. Amorim">

  <script src="js/jquery.js"></script>
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
  <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
  <!------ Include the above in your HEAD tag ---------->

  <link href='http://fonts.googleapis.com/css?family=Raleway:500' rel='stylesheet' type='text/css'>
  <!-- Estilo CSS -->

  <link href="css/inicial.css" rel="stylesheet">
</header>

<body>
  <!--inicia a mensagem de informações-->
  <!-- Modal -->
  <div class="modal fade" id="ExemploModalCentralizado" tabindex="-1" role="dialog" aria-labelledby="TituloModalCentralizado" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="TituloModalCentralizado">Objetivo</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <ul>
            <li>O objetivo desses exercícios é ajudar na compreenssão do conteúdo de Equação Exponencial.</li>
            <li>O exercício é composto por 10 questões, podendo ter apenas 1 resposta correta em cada questão.</li>
            <li>Caso ao verificar a questão e a mesma estiver incorreta, será exibida a mensagem informando que a questão está incorreta e será permitida mais uma oportunidade para que responda corretamente a questão.</li>
            <li>Ao final será exibido um relatório sobre o seu desempenho.</li>
            <li>Para dúvidas ou sujestões, entre em contato com o email: oismaelazevedo@gmail.com!</li>
          </ul>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Fechar</button>
        </div>
      </div>
    </div>
  </div>
  <!--finaliza a mensagem de informações-->

  <div class="middlePage">
    <div class="page-header">
      <h1 class="logo">Sejam bem vindos!</h1>
    </div>

    <div class="panel panel-info">
      <div class="panel-heading">
        <h3 class="panel-title">Identificação do Usuário</h3>
      </div>
      <div class="panel-body">

        <div class="row">

          <div class="col-md-5">
            Exercícios de fixação para melhor entendimento em Equação Exponencial no Ensino Médio.
          </div>

          <div class="col-md-7" style="border-left:1px solid #ccc;height:160px">
            <form class="form-horizontal" action="index5.php" method="post">
              <fieldset>

                <input id="nome" name="nome" type="text" placeholder="Entre com seu nome completo" class="form-control input-md">
                <div class="spacing"><br /></div>
                <input id="email" name="email" type="text" placeholder="Entre com seu email" class="form-control input-md">
                <div class="spacing"><br /></div>
                <button id="iniciar" name="iniciar" class="btn btn-info btn-sm pull-right">Iniciar Exercícios</button>

              
              </fieldset>
            </form>
          </div>

        </div>

      </div>
    </div>

    <a data-toggle="modal" href="#ExemploModalCentralizado">Informações</a>

  </div>
</body>

</html>