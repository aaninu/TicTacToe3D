<?PHP

    /** Include Files */
    include("./config.php");
    include("./functions.php");

    /** Code */

?>

<html>
    <head>
        <title>Clasament Joc </title>
        <style>
            #customers {
            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            border-collapse: collapse;
            width: 100%;
            }

            #customers td, #customers th {
            border: 1px solid #ddd;
            padding: 8px;
            }

            #customers tr:nth-child(even){background-color: #f2f2f2;}

            #customers tr:hover {background-color: #ddd;}

            #customers th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
            }
            </style>
    </head>
    <body>
        <center>
            <h1> TicTacToe3D </h1>
            <hr>
            <table id="customers">
                <tr>
                    <th>Nr.</th>
                    <th>Player</th>
                    <th>Jocuri castigate</th>
                    <th>Jocuri pierdute</th>
                </tr>
<?PHP
    if($conect = mysqli_query(db_Connect(), "SELECT DISTINCT p.pName AS pName FROM PyTicTacToe3D p ORDER BY p.pName ASC;")){ 
        while($load=mysqli_fetch_object($conect)){ 
        $info = db_GetInfo($load->pName);
?>    
                <tr>
                    <td>1</td>
                    <td><?=$load->pName;?></td>
                    <td><?=$info["gWin"];?></td>
                    <td><?=$info["gFail"];?></td>
                </tr>
<?PHP } } ?>
            </table>
        </center>
    </body>
</html>