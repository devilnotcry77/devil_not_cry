<?php
    $servername = 'elener8b.beget.tech';  //Имя сервера
    $database = 'elener8b_44';  //Имя базы данных
    $username = 'elener8b_44';  //Логин
    $password = 'auf4418@';  //Пароль


$conn = mysqli_connect($servername, $username, $password, $database);  //Создание подключения


if(!$conn) {
 //Инициализация ошибки
	die("Connection error: " . mysqli_connect_error());

}
echo "Connection success";  //Сообщение об успехе
mysql_close($conn);  //Закрыть подключение
?>