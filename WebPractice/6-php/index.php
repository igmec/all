<?php

	#http://imech.site/php/?name=igor&pass=1234&gender=male
	#print_r($_GET);

	if($_GET){
		$num = $_GET["number"];
		$isPrime = true;

		for($i = 1;$i <= ($num/2)+1;$i++){
			if($num % $i == 0 && $i != 1){
				$isPrime = false;
				echo "The number ".$num." is NOT a prime.<br>".$i." x ".$num/$i." = ".$num;
				break;
			}
		}
		if ($isPrime) {
			echo "The number ".$num." is a prime.";
		}

	}	

?>

<p>Type a number to check if it's a prime</p>

<form>
	
	<input type="text" name="number">

	<input type="submit" value="Check">

</form>