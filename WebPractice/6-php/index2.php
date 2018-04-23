<?php

	$name = "<p>My Name</p>";

	echo $name;

	$part1 = "<p>First part will be connected";
	$part2 = "to the second part.</p>";

	echo $part1." ".$part2;


	$num = 45;

	$calculation = $num * 34 / 12 + 67;

	echo $calculation." is the result";

	$bool = true;
	echo "<p>This sentence is true? ".$bool."</p>";

	$bool2 = false;	
	echo "This sentence is true? ".$bool2."</p>";

	$doubVar = "name";
	echo $$doubVar;


	echo "<p>============ARRAYS===============</p>";

	$arr = ["item1", "item2", "item3"];
	$arrSame = array("item1", "item2", "item3");

	$arr[] = "This adds a new item";

	echo "<p>".$arr."</p>";

	print_r($arr);

	echo "<p>".$arr[1]."</p>";

	$arr2[0] = "firstItem";

	$arr2[1] = "secondItem";

	$arr2[5] = "fifthItem";

	$arr2["pizza"] = "pizzaItem";

	print_r($arr2);

	echo $arr2["pizza"];


	$arr3 = array(
		"France" => "French", 
		"USA" => "English", 
		"Germany" => "German");

	print_r($arr3);

	unset($arr3["France"]);

	echo sizeof($arr3);


	echo "<p>============IF ELSE===============</p>";

	$user = "rob";

	if ($user == "rob" || $user == "andy") {
		echo "Hello Rob! ";

	}else{
		echo "I don't know you";
	}

	$age = 25;
	if ($age >= 18 && $user == 'rob') {
		echo "Proceed";

	}else{
		echo "Too young!";
	}	


	echo "<p>============LOOPS===============</p>";

	for ($i = 2;$i <= 30;$i+=2){
		echo $i."<br>";
	}

	echo "<br>";

	for ($i = 10;$i >= 0;$i--){
		echo $i."<br>";
	}

	echo "<br>";

	$arr = ["item1", "item2", "item3"];

	for ($i = 0;$i < sizeof($arr);$i++){
		echo $arr[$i]."<br>";
	}


	foreach ($arr as $key => $value){
		$value = $value." LAST";
		echo "Array item ".$key." is ".$value."<br>";
	}



	$j = 10;

	while ($j < 10){
		echo $j."<br>";
		$j++;
	}


	$j=0;
	while ($j < sizeof($arr)){
		echo $arr[$j]."<br>";
		$j++;
	}


?>