<?php
    //Verifica se o email já foi cadastrado
    function EhMesmoEmail($email, $PDO){
        $CmdSQL = "SELECT `email` FROM `usuarios` WHERE email = :email";

        $Consulta  = $PDO->prepare($CmdSQL);
        $Consulta->bindParam(':email', $email);

        $Consulta->execute();

        if($Consulta->rowCount() == 0):
            return 0;
        else:
            return 1;
        endif;
    }
    
?>
