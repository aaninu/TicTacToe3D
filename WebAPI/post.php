<?PHP

    /** Include Files */
    include("./config.php");
    include("./functions.php");

    /** Code */
    $api_player = GPost("api_player");
    $api_win = GPost("api_win");
    $api_fail = GPost("api_fail");
    $api_mode = GPost("api_mode");

    /** Record dates */
    if ($api_player != "" and $api_win != "" and $api_fail != "" and $api_mode != ""){
        if (db_CreateHistory($api_player, $api_win, $api_fail, $api_mode)){
            echo "Datele au fost inregistrate"; 
        }else{
            echo "Ceva nu functioneaza.";
        }
    }else{
        echo "Date incomplete.";
    }
