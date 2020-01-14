<?PHP

    function GPost($val){
       global $_POST;
        return (isset($_POST[$val]))?$_POST[$val]:"";
    }

	function db_Connect(){
    	$mdb = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
		if ($mdb){
			mysqli_set_charset($mdb, "utf8");
			return $mdb;
		}else{
			return 0;
		}
    }
	function db_Escape($val){
		return db_Connect()->real_escape_string($val);
	}
	function db_Create($sql){
		return mysqli_query(db_Connect(), $sql);
	}
	function db_Get($sql){
		return mysqli_fetch_array(mysqli_query(db_Connect(), $sql), MYSQLI_ASSOC);
	}
	function db_CreateHistory($player, $win, $fail, $mode){
		return db_Create("INSERT INTO PyTicTacToe3D SET pName = '".db_Escape($player)."', gWin = '".db_Escape($win)."', gFail = '".db_Escape($fail)."', gMode = '".db_Escape($mode)."';");
    }
	function db_GetInfo($player){
		return db_Get("SELECT SUM(gWin) AS gWin, SUM(gFail) AS gFail FROM PyTicTacToe3D WHERE pName = '".db_Escape($player)."';");
	}
