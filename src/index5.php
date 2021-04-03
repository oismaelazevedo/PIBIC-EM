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

    <title>Matemática</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.5.0/css/all.css' integrity='sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU' crossorigin='anonymous'>


    <!-- Estilo CSS -->
    <link href="css/estilo.css" rel="stylesheet">
    <!-- jQuery -->
    <script src="js/jquery.js"></script>
    <!--Bootstrap Core JavaScript-->
    <script src="js/bootstrap.min.js"></script>

</header>

<body>
    <!--inicia a mensagem de informações-->
    <!-- Modal -->
    <div class="modal fade" id="Observacao" tabindex="-1" role="dialog" aria-labelledby="TituloModalCentralizado" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="TituloModalCentralizado">Sinta-se a vontade para discursar livremente sobre a questão.</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <ul>
                        <li>Por exemplo: </li>
                        <li>Quais as dificuldades encontradas? </li>
                        <li>Como você resolveu a questão? </li>
                        <li>Você usou o mapa de Karnaugh? </li>
                        <li>Quantos blocos encontrou no mapa? </li>
                        <li>Ficou com alguma dúvida? Qual?</li>
                    </ul>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Fechar</button>
                </div>
            </div>
        </div>
    </div>
    <!--finaliza a mensagem de informações-->
    <div class="modal fade" id="responda">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Campos em branco!</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Marque alguma questão!</p>
                </div>
                <div class="modal-footer">
                    <a href="index5.php" onclick="$('#responda').modal('hide')"><button type="button" class="btn btn-primary">Próxima Questão</button></a>
                </div>
            </div>
        </div>
    </div>
    </div>
    <!--inicia a mensagem do primeiro erro-->
    <div class="modal fade" id="erro1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Resposta Incorreta!</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Tente na próxima questão!</p>
                </div>
                <div class="modal-footer">
                    <a href="#" onclick="$('#erro1').modal('hide')"><button type="button" class="btn btn-primary">Ok</button></a>
                </div>
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
                    <h5 class="modal-title">Correto!</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Parabéns. Você acertou!</p>
                </div>
                <div class="modal-footer">

                    <a href="#" onclick="$('#acerto').modal('hide')"><button type="button" class="btn btn-primary">Ok</button></a>
                </div>
            </div>
        </div>
    </div>
    <!--finaliza a mensagem do acerto-->

    <?php
    require_once("funcao/conexao.php");
    require_once("funcao/validacao.php");

    //pegando hora atual
    date_default_timezone_set('America/Sao_Paulo');
    $hora_inicial = date('H:i:s');

    //Cadastra o usuário no banco de dados
    if (isset($_POST['nome'])) {
        $nome = $_POST['nome'];
        $email = $_POST['email'];
        $_SESSION['nome'] = $nome;

        //verifica se já existe esse usuário e seleciona o seu id
        /*//versão de hospedagem
    $sql = "SELECT * FROM usuarios WHERE nome = '$nome' and email = '$email'";
    $consulta = $mysqli->query($sql);*/

        //versão local
        $PDO = CriarConexao();
        $EhMesmoEmail = EhMesmoEmail($email, $PDO);

        if ($EhMesmoEmail != 0) {
            $sql = "SELECT * FROM usuarios WHERE email = :email";

            $consulta = $PDO->prepare($sql);
            $consulta->bindParam(":email", $email);
            $consulta->execute();

            $linha = $consulta->fetch(PDO::FETCH_ASSOC);

            $id_usuario = $linha['id'];
        } else { // Caso não exista... esse usuário é inserido e depois selecionado seu id

            $sql = "INSERT INTO usuarios(nome, email) VALUE (:nome, :email)";

            $consulta = $PDO->prepare($sql);
            $consulta->bindParam(":nome", $nome);
            $consulta->bindParam(":email", $email);
            $consulta->execute();

            $sql = "SELECT * FROM usuarios WHERE nome = :nome and email = :email";
            
            $consulta = $PDO->prepare($sql);
            $consulta->bindParam(":nome", $nome);
            $consulta->bindParam(":email", $email);
            $consulta->execute();

            $linha = $consulta->fetch(PDO::FETCH_ASSOC);

            $id_usuario = $linha['id'];
        }
        $_SESSION['id_usuario'] = $id_usuario;
    }


    if (!isset($_SESSION['escolhido'])) {
        $_SESSION['escolhido'] = array();

        //Cria a sessão que irá armazenar a rodada de exercícios
        $sql = "SELECT MAX(rodada) FROM respostas";
        
        $consulta = $PDO->prepare($sql);
        $consulta->execute();

        $linha = $consulta->fetch();
        $rod = $linha[0];

        $_SESSION['rodada'] = $rod + 1;
    }
    if (!isset($_GET['note'])) {
        $note = 0;
    } else {
        $note = $_GET['note'];
    }

    switch ($note) {
        case 0:
            //Monta a questão
            $arquivo = "json/Gerador1/questao" . rand(1, 200) . ".json";
            $info = file_get_contents($arquivo);
            $_SESSION['info'] = $arquivo;

        case 1:
    ?>
            <script>
                $('#acerto').modal({
                    backdrop: 'static',
                    keyboard: false
                });
            </script>
        <?php
            //Monta a questão
            $arquivo = "json/Gerador1/questao" . rand(1, 200) . ".json";
            $info = file_get_contents($arquivo);
            $_SESSION['info'] = $arquivo;

        case 2:
        ?>
            <!--chamando modal erro1-->
            <script>
                $('#erro1').modal({
                    backdrop: 'static',
                    keyboard: false
                });
            </script>
        <?php
            $arquivo = "json/Gerador1/questao" . rand(1, 200) . ".json";
            $info = file_get_contents($arquivo);
            $_SESSION['info'] = $arquivo;
        case 3:
        ?>
            <script>
                $('#responda').modal({
                    backdrop: 'static',
                    keyboard: false
                });
            </script>
    <?php
            $info = file_get_contents($_SESSION['info']);
            $_SESSION['info'] = $arquivo;
    }








    $lendo = json_decode($info);

    foreach ($lendo->atributosquestao as $campo) {
        $enunciado[] = $campo->enunciado;
    }


    foreach ($lendo->respostas as $campo) {
        $alt[] = $campo->letra;
        $resp[] = $campo->resposta;
    }

    ?>

    <!-- container pagina -->

    <div class="container-all">
        <!-- container do top -->
        <div class="container-top">

            <!-- Titulo ou Pergunta da interação -->
            <div class="title-top">
                <label class="label-inter">
                    Resolvendo Equações Exponenciais
                </label>
            </div>

            <!-- logo da RNP -->
            <div class="rnp-logo">
                <img class="logo-rnp" src="./teste_files/RNP-marca-principal-RGB_1.png">
            </div>
        </div> <!-- end container do top -->

        <!-- container do corpo da pagina -->
        <div class="container-body">
            <!-- container com grupos -->
            <div id="container-group" class="container-group">
                <!-- conteudo do grupo 3 -->
                <div class="content-group3" style="margin-left: 6px">
                    Observações sobre a questão:
                    <a data-toggle="modal" href="#Observacao"><i class='fas fa-question' style='font-size:18px'></i></a>
                </div>



                <!-- container com perguntas globais -->
                <div class="container-answers">
                    <!-- box das intruções -->
                    <div class="box-quest">
                        <!-- Icon da pergunta -->
                        <div class="quest-icon">
                            <img class="double-arrow" src="images/setadupla.png" height="25" width="25">
                        </div><!-- end Icon da pergunta -->
                        <!-- pergunta em si -->
                        <div class="quest-str">
                            <label class="question-info"><b>Enunciado: </b></label>
                            <label class="question-info">
                                <center>
                                    <?php
                                    echo $enunciado[0];
                                    ?>
                                </center>
                            </label>
                        </div><!-- end pergunta em si -->
                    </div><!-- end box das intruções -->
                </div>
                <!--end container com perguntas globais -->
                <!-- grupos A -->
                <div class="group-a">
                    <!-- Titulo A -->
                    <div class="title-group">
                        <label style="font-family: Verdana; "><b>Alternativas</b></label>
                    </div>


                    <!-- conteudo do grupo 2 -->
                    <div class="content-group2" style="margin-left: 0px; width: 898px">


                        <!-- container2 de respostas -->
                        <!-- conteudo de respostas -->
                        <form action="confere_resp.php" method="post">


                            <div class="title-legenda" style="margin-left: 13px">
                                <div class="content-textarea" style="margin-left: 0px;">
                                    <textarea rows="4" cols="55" name="obs" id="obs"></textarea>
                                </div>
                            </div>

                            <input type="hidden" name="hora_inicial" id="hora_inicial" value="<?php echo $hora_inicial; ?>">
                            <input type="hidden" name="arquivo" id="arquivo" value="<?php echo $arquivo; ?>">
                            <div data-toggle="buttons">
                                <div class="btn-group-toggle">
                                    <label class="btn btn-secondary">
                                        <input type="radio" value="A" name="letra" autocomplete="off"> <?php echo $alt[0] . ") " . $resp[0]; ?>
                                    </label>
                                </div>
                                <div class="btn-group-toggle">
                                    <label class="btn btn-secondary">
                                        <input type="radio" value="B" name="letra" autocomplete="off"> <?php echo $alt[1] . ") " . $resp[1]; ?>
                                    </label>
                                </div>
                                <div class="btn-group-toggle">
                                    <label class="btn btn-secondary">
                                        <input type="radio" value="C" name="letra" autocomplete="off"> <?php echo $alt[2] . ") " . $resp[2]; ?>
                                    </label>
                                </div>
                                <div class="btn-group-toggle">
                                    <label class="btn btn-secondary">
                                        <input type="radio" value="D" name="letra" autocomplete="off"> <?php echo $alt[3] . ") " . $resp[3]; ?>
                                    </label>
                                </div>
                                <div class="btn-group-toggle">
                                    <label class="btn btn-secondary">
                                        <input type="radio" value="E" name="letra" autocomplete="off"> <?php echo $alt[4] . ") " . $resp[4]; ?>
                                    </label>
                                </div>
                            </div>
                            <div class=text-right>
                                <button type="submit" class="btn btn-primary">Verificar</button>
                            </div>
                            <!-- Botão para acionar modal -->




                    </div>



                    </form>
                </div> <!-- end grupos A -->
            </div>
        </div>
    </div>

</body>

</html>